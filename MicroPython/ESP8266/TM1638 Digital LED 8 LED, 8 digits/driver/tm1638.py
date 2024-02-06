from machine import Pin
from time import sleep_us, sleep_ms

TM1638_CMD1 = 64   # 0x40 data command
TM1638_CMD2 = 192  # 0xC0 address command
TM1638_CMD3 = 128  # 0x80 display control command
TM1638_DSP_ON = 8  # 0x08 display on
TM1638_READ = 2    # 0x02 read key scan data
TM1638_FIXED = 4   # 0x04 fixed address mode

_SEGMENTS = bytearray(b'\x3F\x06\x5B\x4F\x66\x6D\x7D\x07\x7F\x6F\x77\x7C\x39\x5E\x79\x71\x3D\x76\x06\x1E\x76\x38\x55\x54\x3F\x73\x67\x50\x6D\x78\x3E\x1C\x2A\x76\x6E\x5B\x00\x40\x63')

class TM1638(object):
    def __init__(self, stb, clk, dio, brightness=7):
        self.stb = Pin(stb, Pin.OUT)
        self.clk = Pin(clk, Pin.OUT)
        self.dio = Pin(dio, Pin.OUT)

        if not 0 <= brightness <= 7:
            raise ValueError("Brightness out of range")
        self._brightness = brightness

        self._on = TM1638_DSP_ON

        self.clk.init(Pin.OUT, value=1)
        self.dio.init(Pin.OUT, value=0)
        self.stb.init(Pin.OUT, value=1)

        self.clear()
        self._write_dsp_ctrl()

    def _write_data_cmd(self):
        self._command(TM1638_CMD1)

    def _set_address(self, addr=0):
        self._byte(TM1638_CMD2 | addr)

    def _write_dsp_ctrl(self):
        self._command(TM1638_CMD3 | self._on | self._brightness)

    def _command(self, cmd):
        self.stb(0)
        self._byte(cmd)
        self.stb(1)

    def _byte(self, b):
        for i in range(8):
            self.clk(0)
            self.dio((b >> i) & 1)
            self.clk(1)

    def _scan_keys(self):
        pressed = 0
        self.dio.init(Pin.IN, Pin.PULL_UP)
        for i in range(8):
            self.clk(0)
            if self.dio.value():
                pressed |= 1 << i
            self.clk(1)
        self.dio.init(Pin.OUT)
        return pressed

    def power(self, val=None):
        if val is None:
            return self._on == TM1638_DSP_ON
        self._on = TM1638_DSP_ON if val else 0
        self._write_dsp_ctrl()

    def brightness(self, val=None):
        if val is None:
            return self._brightness
        if not 0 <= val <= 7:
            raise ValueError("Brightness out of range")
        self._brightness = val
        self._write_dsp_ctrl()

    def clear(self):
        self._write_data_cmd()
        self.stb(0)
        self._set_address(0)
        for i in range(16):
            self._byte(0x00)
        self.stb(1)

    def write(self, data, pos=0):
        if not 0 <= pos <= 15:
            raise ValueError("Position out of range")
        self._write_data_cmd()
        self.stb(0)
        self._set_address(pos)
        for b in data:
            self._byte(b)
        self.stb(1)

    def led(self, pos, val):
        self.write([val], (pos << 1) + 1)

    def leds(self, val):
        self._write_data_cmd()
        pos = 1
        for i in range(8):
            self.stb(0)
            self._set_address(pos)
            self._byte((val >> i) & 1)
            pos += 2
            self.stb(1)

    def segments(self, segments, pos=0):
        if not 0 <= pos <= 7:
            raise ValueError("Position out of range")
        self._write_data_cmd()
        for seg in segments:
            self.stb(0)
            self._set_address(pos << 1)
            self._byte(seg)
            pos += 1
            self.stb(1)

    def keys(self):
        keys = 0
        self.stb(0)
        self._byte(TM1638_CMD1 | TM1638_READ)
        for i in range(4):
            keys |= self._scan_keys() << i
        self.stb(1)
        return keys

    def qyf_keys(self):
        keys = 0
        self.stb(0)
        self._byte(TM1638_CMD1 | TM1638_READ)
        for i in range(4):
            i_keys = self._scan_keys()
            for k in range(2):
                for j in range(2):
                    x = (0x04 >> k) << j*4
                    if i_keys & x == x:
                        keys |= (1 << (j + k*8 + 2*i))
        self.stb(1)
        return keys

    def encode_digit(self, digit):
        return _SEGMENTS[digit & 0x0f]

    def encode_string(self, string):
        string = string.replace('.', '')[:8]

        segments = bytearray(len(string))

        for i in range(len(string)):
            if string[i] == ':':
                if i > 0:
                    segments[i - 1] |= (1 << 7)
                segments[i] = _SEGMENTS[10]
            else:
                segments[i] = self.encode_char(string[i])

        return segments

    def encode_char(self, char):
        o = ord(char)
        if o == 32:
            return _SEGMENTS[36] # space
        if o == 42:
            return _SEGMENTS[38] # star/degrees
        if o == 45:
            return _SEGMENTS[37] # dash
        if o >= 65 and o <= 90:
            return _SEGMENTS[o-55] # uppercase A-Z
        if o >= 97 and o <= 122:
            return _SEGMENTS[o-87] # lowercase a-z
        if o >= 48 and o <= 57:
            return _SEGMENTS[o-48] # 0-9
        raise ValueError("Character out of range: {:d} '{:s}'".format(o, chr(o)))

    def hex(self, val):
        string = '{:08x}'.format(val & 0xffffffff)
        self.segments(self.encode_string(string))

    def number(self, num):
        num = max(-9999999, min(num, 99999999))
        string = '{0: >8d}'.format(num)
        self.segments(self.encode_string(string))

    def temperature(self, num, pos=0):
        if num < -9:
            self.show('lo', pos) # low
        elif num > 99:
            self.show('hi', pos) # high
        else:
            string = '{0: >2d}'.format(num)
            self.segments(self.encode_string(string), pos)
        self.show('*C', pos + 2) # degrees C

    def humidity(self, num, pos=4):
        if num < -9:
            self.show('lo', pos) # low
        elif num > 99:
            self.show('hi', pos) # high
        else:
            string = '{0: >2d}'.format(num)
            self.segments(self.encode_string(string), pos)
        self.show('rh', pos + 2) # relative humidity

    def show(self, string, pos=0):
        segments = self.encode_string(string)
        self.segments(segments[:8], pos)

    def scroll(self, string, delay=250):
        segments = string if isinstance(string, list) else self.encode_string(string)
        data = [0] * 16
        data[8:0] = list(segments)
        for i in range(len(segments) + 9):
            self.segments(data[0+i:8+i])
            sleep_ms(delay)
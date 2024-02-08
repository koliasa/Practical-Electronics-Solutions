from machine import Pin, UART
import time

class GY_GPS6MV2:
    def __init__(self, tx_pin, rx_pin, led_pin):
        self.uart = UART(1, baudrate=9600, tx=tx_pin, rx=rx_pin)
        self.led = Pin(led_pin, Pin.OUT)
        self.led.off()

    def blink_led(self):
        self.led.on()
        time.sleep(0.5)
        self.led.off()

    def read_sentence(self):
        sentence = b""
        while True:
            if self.uart.any():
                char = self.uart.read(1)
                sentence += char
                if char == b'\n':
                    return sentence.decode('utf-8')

    def parse_gga(self, sentence):
        data = sentence.split(',')
        if data[0] == "$GPGGA" and data[6] != '0':
            latitude = self.convert_coordinates(data[2], data[3])
            longitude = self.convert_coordinates(data[4], data[5])
            return latitude, longitude
        else:
            return None

    def convert_coordinates(self, value, direction):
        degrees = int(value[:2])
        minutes = float(value[2:])
        coordinates = degrees + minutes / 60.0
        if direction == 'S' or direction == 'W':
            coordinates = -coordinates
        return coordinates

    def get_coordinates(self):
        while True:
            sentence = self.read_sentence()
            if sentence.startswith("$GPGGA"):
                coordinates = self.parse_gga(sentence)
                if coordinates:
                    self.led.on()
                    return coordinates
            else:
                self.blink_led()

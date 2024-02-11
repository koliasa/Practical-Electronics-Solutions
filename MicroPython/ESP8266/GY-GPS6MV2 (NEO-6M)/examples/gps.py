import machine
import utime

class GPS:
    def __init__(self, uart, tx_pin, rx_pin):
        self.uart = uart
        self.uart.init(baudrate=9600, tx=tx_pin, rx=rx_pin)
        self.fix = False
        self.latitude = 0.0
        self.longitude = 0.0
        self.altitude = 0.0
        self.speed = 0.0
        self.course = 0.0
        self.satellites = 0

    def parse_nmea(self, sentence):
        parts = sentence.split(',')
        if parts[0] == '$GPGGA' and len(parts) >= 15:
            fix = int(parts[6])
            if fix in (1, 2):
                self.fix = True
                self.latitude = self._parse_lat_lon(parts[2], parts[3])
                self.longitude = self._parse_lat_lon(parts[4], parts[5])
                self.altitude = float(parts[9])
            else:
                self.fix = False

        elif parts[0] == '$GPVTG' and len(parts) >= 9:
            self.course = float(parts[1])

        elif parts[0] == '$GPRMC' and len(parts) >= 12:
            self.speed = float(parts[7])

        elif parts[0] == '$GPGSV' and len(parts) >= 7:
            self.satellites = int(parts[3])

    def _parse_lat_lon(self, value, direction):
        degrees = float(value[:2])
        minutes = float(value[2:])
        coordinate = degrees + minutes / 60.0
        if direction == 'S' or direction == 'W':
            coordinate = -coordinate
        return coordinate

    def read(self):
        while self.uart.any():
            sentence = self.uart.readline().decode('utf-8')
            self.parse_nmea(sentence)

    def get_coordinates(self):
        return self.latitude, self.longitude

    def get_altitude(self):
        return self.altitude

    def get_speed(self):
        return self.speed

    def get_course(self):
        return self.course

    def get_satellites(self):
        return self.satellites
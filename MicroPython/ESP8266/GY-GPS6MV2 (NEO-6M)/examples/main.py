from machine import UART, Pin
from gps import GPS
import utime

# Ініціалізація UART та GPS
uart = UART(0)
gps = GPS(uart, tx_pin=Pin(18), rx_pin=Pin(19))

while True:
    gps.read()
    if gps.fix:
        latitude, longitude = gps.get_coordinates()
        altitude = gps.get_altitude()
        speed = gps.get_speed()
        course = gps.get_course()
        satellites = gps.get_satellites()

        print(f"Latitude: {latitude}, Longitude: {longitude}")
        print(f"Altitude: {altitude} meters")
        print(f"Speed: {speed} km/h")
        print(f"Course: {course} degrees")
        print(f"Satellites: {satellites}")

    utime.sleep(1)

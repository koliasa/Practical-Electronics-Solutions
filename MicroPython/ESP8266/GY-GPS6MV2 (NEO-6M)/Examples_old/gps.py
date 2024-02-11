# main.py

import time
import machine
from micropyGPS import MicropyGPS

# Читання даних GPS з UART
def read_gps_data(uart, gps):
    while uart.any():
        sentence = uart.readline()
        for char in sentence:
            gps.update(chr(char))

# Отримання поточних трикутних координат
def get_current_coordinates(gps):
    lat = gps.latitude[0] + gps.latitude[1]/60.0
    lon = gps.longitude[0] + gps.longitude[1]/60.0
    return lat, lon

# Оновлення та виведення координат кожної секунди
while True:
    read_gps_data(uart=gps_uart, gps=gps)
    lat, lon = get_current_coordinates(gps)
    print("Поточні координати: Широта {}, Довгота {}".format(lat, lon))
    time.sleep(1)
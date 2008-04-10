# boot.py

import network
import machine
import time
import micropython

# Встановлення з'єднання Wi-Fi
def connect_wifi(ssid, password):
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    if not sta_if.isconnected():
        print('Підключення до Wi-Fi...')
        sta_if.connect(ssid, password)
        while not sta_if.isconnected():
            pass
    print('Підключено до Wi-Fi:', sta_if.ifconfig())

# Ініціалізація UART для GY-GPS6MV2
def init_gps_uart():
    uart = machine.UART(1, baudrate=9600, tx=5, rx=4)
    return uart

# Очікування наявності GPS-сигналу
def wait_for_gps_fix(gps):
    while not gps.fix_stat:
        pass

# Виклик функцій для ініціалізації
ssid = "You_SID"
password = "YouPassword"
connect_wifi(ssid, password)

gps_uart = init_gps_uart()

# Використання бібліотеки micropyGPS для обробки GPS-даних
micropython.alloc_emergency_exception_buf(100)
from micropyGPS import MicropyGPS
gps = MicropyGPS()

# Очікування отримання GPS-даних
wait_for_gps_fix(gps)
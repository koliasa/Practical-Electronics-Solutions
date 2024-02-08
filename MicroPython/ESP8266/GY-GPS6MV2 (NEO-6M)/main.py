from GY_GPS6MV2 import GY_GPS6MV2
from machine import Pin
import time

# Пін для LED на NodeMCU
led_pin = 0  # Змініть на відповідний, якщо потрібно

# Піни для GY-GPS6MV2
gps_tx_pin = 5
gps_rx_pin = 4

# Створення об'єкта GY_GPS6MV2
gps = GY_GPS6MV2(gps_tx_pin, gps_rx_pin, led_pin)

# Основний код
try:
    while True:
        coordinates = gps.get_coordinates()
        print("Coordinates:", coordinates)
        time.sleep(1)
except KeyboardInterrupt:
    print("Program terminated by user")
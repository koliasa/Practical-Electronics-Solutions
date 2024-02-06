import machine
import time

# Визначення пінів для LED-діодів
led_pin_1 = machine.Pin(5, machine.Pin.OUT)  # D1
led_pin_2 = machine.Pin(4, machine.Pin.OUT)  # D2

# Функція стробоскопічного мерехтіння LED-діода
def strobe_flash(led_pin, duration=0.1):
    led_pin.on()
    time.sleep(duration)
    led_pin.off()
    time.sleep(duration)

# Безкінечний цикл стробоскопічного мерехтіння
while True:
    strobe_flash(led_pin_1)
    strobe_flash(led_pin_2)
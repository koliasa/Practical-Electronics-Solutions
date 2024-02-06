import machine
import time

# Визначення пінов для LED-діодів
led_pin_1 = machine.Pin(5, machine.Pin.OUT)  # D1
led_pin_2 = machine.Pin(4, machine.Pin.OUT)  # D2
led_pin_3 = machine.Pin(0, machine.Pin.OUT)  # D3

# Функція для стробоскопічного мерехтіння LED-діода 10 разів
def strobe_flash(led_pin, flashes=10, duration=0.05):
    for _ in range(flashes):
        led_pin.on()
        time.sleep(duration)
        led_pin.off()
        time.sleep(duration)

# Безкінечний цикл стробоскопічного мерехтіння для трьох LED-діодів
while True:
    strobe_flash(led_pin_1)
    time.sleep(0.5)  # Затримка перед переходом до наступного LED
    strobe_flash(led_pin_2)
    time.sleep(0.5)  # Затримка перед переходом до наступного LED
    strobe_flash(led_pin_3)
    time.sleep(0.5)  # Затримка перед повторенням циклу

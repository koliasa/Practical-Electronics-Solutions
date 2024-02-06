import machine
import time

# Визначення пінів для LED-діодів
led_pin_1 = machine.Pin(5, machine.Pin.OUT)  # D1
led_pin_2 = machine.Pin(4, machine.Pin.OUT)  # D2
led_pin_3 = machine.Pin(0, machine.Pin.OUT)  # D3

# Функція стробоскопічного мерехтіння LED-діода 10 разів
def strobe_flash(led_pin, flashes=10, duration=0.05):
    for _ in range(flashes):
        led_pin.on()
        time.sleep(duration)
        led_pin.off()
        time.sleep(duration)

# Функція для відтворення сигналу SOS
def sos_signal():
    for _ in range(3):  # Відтворити SOS 3 рази
        strobe_flash(led_pin_1, flashes=3)  # "S"
        time.sleep(1)  # Затримка між літерами
        strobe_flash(led_pin_2, flashes=3)  # "O"
        time.sleep(1)  # Затримка між літерами
        strobe_flash(led_pin_3, flashes=3)  # "S"
        time.sleep(2)  # Затримка між повторами

# Безкінечний цикл для відтворення сигналу SOS
while True:
    sos_signal()
    time.sleep(4)  # Затримка перед повторенням циклу

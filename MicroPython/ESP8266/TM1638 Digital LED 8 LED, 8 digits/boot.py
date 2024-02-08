import network
import utime
import machine
import ntptime

def connect_wifi():
    ssid = "Логін мережі"
    password = "Ваш пароль"

    # Світлодіод, який зазвичай приєднаний до піна GPIO 2
    led_pin = machine.Pin(2, machine.Pin.OUT)

    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect(ssid, password)

    while not sta_if.isconnected():
        led_pin.on()  # Увімкнення світлодіода
        utime.sleep(0.2)
        led_pin.off()  # Вимкнення світлодіода
        utime.sleep(0.2)

    led_pin.off()  # Вимкнення світлодіода після підключення

def sync_ntp():
    try:
        ntptime.settime()
        print("Time synchronized")
    except Exception as e:
        print("Failed to synchronize time:", e)

connect_wifi()
sync_ntp()

import network
import utime

def connect_wifi():
    ssid = "Ваша мережа"
    password = "пароль"

    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect(ssid, password)

    while not sta_if.isconnected():
        pass

def sync_ntp():
    import ntptime

    try:
        ntptime.settime()
        print("Time synchronized")
    except Exception as e:
        print("Failed to synchronize time:", e)

connect_wifi()
sync_ntp()
from machine import Pin, RTC
from tm1638 import TM1638
from utime import sleep, localtime, time

# Оголошення об'єкту класу TM1638
tm = TM1638(stb=Pin(13), clk=Pin(14), dio=Pin(12))

# Оголошення об'єкту RTC
rtc = RTC()

# Отримання різниці часу для Києва (літній та зимовий час)
def get_kyiv_time_offset():
    return 2  # Зазначте відповідну різницю часу (години) для Києва

# Відображення поточного часу на LED-дисплеї
while True:
    # Отримання UTC часу
    utc_time = time()

    # Отримання різниці часу для Києва
    kyiv_offset = get_kyiv_time_offset()

    # Отримання локального часу для Києва
    kyiv_time = localtime(utc_time + kyiv_offset * 3600)

    # Отримання годин, хвилин та секунд
    current_time = kyiv_time[3:6]

    # Форматування часу у рядок "HHMMSS"
    time_str = "{:02}-{:02}-{:02}".format(current_time[0], current_time[1], current_time[2])

    # Відображення часу на дисплеї
    tm.show(time_str)

    # Чекаємо 1 секунду перед оновленням
    sleep(1)

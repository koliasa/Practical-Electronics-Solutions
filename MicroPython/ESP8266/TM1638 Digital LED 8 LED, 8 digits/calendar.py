from machine import Pin, RTC
from tm1638 import TM1638
from utime import sleep, localtime

# Оголошення об'єкту класу TM1638
tm = TM1638(stb=Pin(13), clk=Pin(14), dio=Pin(12))

# Оголошення об'єкту RTC
rtc = RTC()

# Відображення поточної дати на LED-дисплеї
while True:
    # Синхронізація з RTC
    rtc.datetime(localtime())
    
    # Отримання поточної дати
    current_date = localtime()[:3]
    
    # Форматування дати у рядок "YYYYMMDD"
    date_str = "{:04}{:02}{:02}".format(current_date[0], current_date[1], current_date[2])
    
    # Відображення дати на дисплеї
    tm.show(date_str)
    
    # Чекаємо 1 секунду
    sleep(1)
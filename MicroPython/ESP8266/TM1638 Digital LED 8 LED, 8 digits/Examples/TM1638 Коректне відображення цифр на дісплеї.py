from machine import Pin
from tm1638 import TM1638
from utime import sleep

# Оголошення об'єкту класу TM1638
tm = TM1638(stb=Pin(13), clk=Pin(14), dio=Pin(12))

# Відображення поточної дати на LED-дисплеї
while True:
    tm.show("20240206")  # Замініть "20240206" поточною датою (рік, місяць, день)
    sleep(1)

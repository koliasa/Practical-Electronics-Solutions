# Імпортуємо необхідні модулі
from math import pi

# Функція для перетворення градусів у радіани
def deg2rad(degrees):
  return degrees * pi / 180

# Функція для обчислення трикутних координат
def compute_triangulation_coordinates(latitude, longitude):
  # Перетворюємо широту та довготу в радіани
  latitude_rad = deg2rad(latitude)
  longitude_rad = deg2rad(longitude)

  # Обчислюємо трикутні координати
  x = longitude_rad * cos(latitude_rad)
  y = latitude_rad

  # Виводимо дані
  print(f'Трикутна координата X: {x}')
  print(f'Трикутна координата Y: {y}')

# Отримуємо поточні дані GPS
latitude = input('Введіть широту: ')
longitude = input('Введіть довготу: ')

# Обчислюємо трикутні координати
compute_triangulation_coordinates(latitude, longitude)

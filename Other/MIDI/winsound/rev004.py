import winsound
import time

# Оголошення нот та їх довжини
G4 = 391
A4 = 440
B4 = 493
C5 = 523
D5 = 587
E5 = 659
F5 = 698
G5 = 783

quarter_note = 400  # довжина чвертової ноти в мілісекундах

# Послідовність нот для пісні
notes = [G5, F5, G5, A4, G5, F5, G5, B4, A4, G5, D5, B4,
         G5, F5, G5, A4, G5, F5, G5, B4, A4, G5, D5, B4, G5]

# Послідовність довжин нот для пісні
lengths = [1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1,
           1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 2, 4]

# Програвання послідовності нот та їх довжини
for i in range(len(notes)):
    duration = lengths[i] * quarter_note
    winsound.Beep(notes[i], duration)
    time.sleep(0.05)  # пауза між нотами

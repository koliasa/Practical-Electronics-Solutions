import winsound
import time

# Оголошення нот та їх довжини
C4 = 261
D4 = 293
E4 = 329
F4 = 349
G4 = 391
A4 = 440
B4 = 493
C5 = 523

quarter_note = 500  # довжина чвертової ноти в мілісекундах

# Послідовність нот для пісні
notes = [E4, D4, C4, D4, E4, E4, E4, D4, D4, D4, E4, G4, G4,
         E4, D4, C4, D4, E4, E4, E4, E4, D4, D4, E4, D4, C4]

# Послідовність довжин нот для пісні
lengths = [1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 2,
           1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 2]

# Програвання послідовності нот та їх довжини
for i in range(len(notes)):
    duration = lengths[i] * quarter_note
    winsound.Beep(notes[i], duration)
    time.sleep(0.05)  # пауза між нотами

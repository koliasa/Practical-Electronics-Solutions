import time
import winsound

# Оголошення нот та їх довжини
C4 = 262
D4 = 294
E4 = 330
F4 = 349
G4 = 392
A4 = 440
B4 = 494
C5 = 523

quarter_note = 500  # довжина чвертової ноти в мілісекундах

# Послідовність нот для коломийки
notes = [G4, F4, E4, F4, G4, G4, G4, F4, F4, F4, G4, B4, B4,
         G4, F4, E4, F4, G4, G4, G4, G4, F4, F4, G4, F4, E4]

# Послідовність довжин нот для коломийки
lengths = [1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 2,
           1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 2]

# Програвання послідовності нот та їх довжини
for i in range(len(notes)):
    duration = lengths[i] * quarter_note
    winsound.Beep(notes[i], duration)
    time.sleep(0.05)  # пауза між нотами

import random
import winsound
import time

# Оголошення можливих нот та їх довжини
notes = [261, 293, 329, 349, 391, 440, 493, 523]
quarter_note = 500  # довжина чвертової ноти в мілісекундах

# Послідовність нот для пісні
melody = []
for i in range(16):
    melody.append(random.choice(notes))

# Послідовність довжин нот для пісні
lengths = [1, 2, 1, 1, 2, 1, 1, 2]

# Програвання послідовності нот та їх довжини
for i in range(len(melody)):
    duration = random.choice(lengths) * quarter_note
    winsound.Beep(melody[i], duration)
    time.sleep(0.05)  # пауза між нотами

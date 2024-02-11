# Імпортуємо модуль для роботи з MIDI
import midi

# Створюємо новий файл MIDI
file = midi.Pattern()

# Створюємо новий трек
track = midi.Track()
file.append(track)

# Визначаємо темп (в мілісекундах на чвертьноту)
tempo = midi.SetTempoEvent(tick=0, bpm=120)
track.append(tempo)

# Визначаємо тональність (в цьому випадку - до мажор)
key = midi.KeySignatureEvent(tick=0, data=[0, 0])
track.append(key)

# Визначаємо інструмент (в цьому випадку - сопілка)
instrument = midi.ProgramChangeEvent(tick=0, channel=0, data=[73])
track.append(instrument)

# Створюємо список нот для мелодії (в MIDI форматі)
notes = [72, 74, 76, 77, 79, 81, 83, 84]

# Створюємо функцію для додавання ноти до треку
def add_note(tick, pitch, duration):
    # Додаємо подію включення ноти
    on = midi.NoteOnEvent(tick=tick, channel=0, data=[pitch, 100])
    track.append(on)
    # Додаємо подію виключення ноти
    off = midi.NoteOffEvent(tick=duration, channel=0, data=[pitch, 100])
    track.append(off)

# Створюємо функцію для генерації випадкового числа в заданому діапазоні
import random
def rand(min, max):
    return random.randint(min, max)

# Генеруємо мелодію у стилі коломийки
tick = 0 # Початковий час
for i in range(16): # Кількість тактів
    for j in range(4): # Кількість нот в такті
        # Вибираємо випадкову ноту зі списку
        pitch = notes[rand(0, len(notes) - 1)]
        # Вибираємо випадкову тривалість ноти (в тиках)
        duration = rand(50, 200)
        # Додаємо ноту до треку
        add_note(tick, pitch, duration)
        # Збільшуємо час на тривалість ноти
        tick += duration

# Додаємо подію кінця треку
eot = midi.EndOfTrackEvent(tick=1)
track.append(eot)

# Зберігаємо файл MIDI
midi.write_midifile("kolomyika.mid", file)
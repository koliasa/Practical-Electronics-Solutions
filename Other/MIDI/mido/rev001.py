import mido
from mido import Message, MidiFile, MidiTrack

# Створення нового MIDI-файлу
mid = MidiFile(type=0)

# Створення нового треку
track = MidiTrack()
mid.tracks.append(track)

# Налаштування темпу та нотного значення
tempo = mido.bpm2tempo(120)
time_per_tick = int(mido.tick2second(1, mid.ticks_per_beat, tempo) * 1000)
note_value = mid.ticks_per_beat // 4

# Створення мелодії
notes = ['C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5', 'C6']
durations = [2, 2, 2, 2, 2, 2, 2, 4]

# Додавання нот до треку
time = 0
for note, duration in zip(notes, durations):
    note_number = mido.note_name_to_number(note)
    track.append(Message('note_on', note=note_number, velocity=64, time=time))
    track.append(Message('note_off', note=note_number, velocity=64, time=note_value * duration))
    time = 0

# Збереження MIDI-файлу
mid.save('melody.mid')

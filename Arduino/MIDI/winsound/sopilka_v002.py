import pygame
from pygame.locals import *

pygame.init()
pygame.mixer.init()

sample_rate = 44100
tempo = 150
notes = [("E5", 4), ("D5", 4), ("C5", 4), ("D5", 4),
         ("E5", 4), ("E5", 4), ("E5", 4), ("D5", 4),
         ("D5", 4), ("D5", 4), ("E5", 4), ("G5", 4), ("G5", 4),
         ("E5", 4), ("D5", 4), ("C5", 4), ("D5", 4),
         ("E5", 4), ("E5", 4), ("E5", 4), ("D5", 4),
         ("D5", 4), ("E5", 4), ("D5", 4), ("C5", 4)]

note_durations = []
for note in notes:
    duration = 60 / tempo * 4 / note[1]
    note_durations.append(duration)

sound_buffer = []
for i in range(len(notes)):
    note = notes[i][0]
    duration = note_durations[i]

    frequency = 0
    if note == "C5":
        frequency = 523.25
    elif note == "D5":
        frequency = 587.33
    elif note == "E5":
        frequency = 659.25
    elif note == "F5":
        frequency = 698.46
    elif note == "G5":
        frequency = 783.99
    elif note == "A5":
        frequency = 880.00
    elif note == "B5":
        frequency = 987.77

    samples = []
    for t in range(int(duration * sample_rate)):
        sample = 32767 * 0.5 * (1 + pygame.math.lerp(-1, 1, math.sin(2 * math.pi * frequency * t / sample_rate)))
        samples.append(sample)

    sound_buffer.extend(samples)

pygame.mixer.Sound(sound_buffer).play()

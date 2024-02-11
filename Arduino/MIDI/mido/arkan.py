import time
import random
import rtmidi

# Set up MIDI output
midiout = rtmidi.MidiOut()
midiout.open_port(0)

# Set the tempo (in beats per minute)
tempo = 120

# Set the note duration (in seconds)
note_duration = 0.5

# Define the melody
melody = [
    ('A', 4), ('B', 4), ('C#', 5), ('D', 5),
    ('E', 5), ('D', 5), ('C#', 5), ('B', 4),
    ('A', 4), ('B', 4), ('C#', 5), ('D', 5),
    ('E', 5), ('D', 5), ('C#', 5), ('B', 4),
    ('C#', 5), ('D', 5), ('E', 5), ('F#', 5),
    ('G#', 5), ('A', 5), ('G#', 5), ('F#', 5),
    ('E', 5), ('D', 5), ('C#', 5), ('B', 4),
    ('A', 4), ('B', 4), ('C#', 5), ('D', 5),
    ('E', 5), ('D', 5), ('C#', 5), ('B', 4)
]

# Define a function to play a note
def play_note(note, velocity=127):
    note_number = 60 + note[1] * 12 + {'C': 0, 'C#': 1, 'D': 2, 'D#': 3, 'E': 4, 'F': 5, 'F#': 6, 'G': 7, 'G#': 8, 'A': 9, 'A#': 10, 'B': 11}[note[0]]
    on = [0x90 | 0, note_number, velocity]
    off = [0x80 | 0, note_number, 0]
    midiout.send_message(on)
    time.sleep(note_duration)
    midiout.send_message(off)

# Play the melody
for note in melody:
    play_note(note)

# Close the MIDI output
midiout.close_port()
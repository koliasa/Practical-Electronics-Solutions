import numpy as np
import simpleaudio as sa

# Define the audio parameters
sample_rate = 44100  # Hertz
duration = 0.5  # Seconds
frequency = 440  # Hertz
t = np.linspace(0, duration, int(duration * sample_rate), False)

# Define the waveform for each note
waveforms = {
    ('C', 4): np.sin(frequency * t * 2 * np.pi),
    ('D', 4): np.sin(587.33 * t * 2 * np.pi),
    ('E', 4): np.sin(659.26 * t * 2 * np.pi),
    ('F', 4): np.sin(698.46 * t * 2 * np.pi),
    ('G', 4): np.sin(783.99 * t * 2 * np.pi),
    ('A', 4): np.sin(880.00 * t * 2 * np.pi),
    ('B', 4): np.sin(987.77 * t * 2 * np.pi),
    ('C', 5): np.sin(1046.50 * t * 2 * np.pi),
}

# Define the melody
melody = [
    ('C', 4), ('D', 4), ('E', 4), ('F', 4),
    ('G', 4), ('A', 4), ('B', 4), ('C', 5),
    ('B', 4), ('A', 4), ('G', 4), ('F', 4),
    ('E', 4), ('D', 4), ('C', 4)
]

# Concatenate the waveforms for each note in the melody
melody_waveform = np.concatenate([waveforms[note] for note in melody])

# Scale the waveform to 16-bit range
normalized_waveform = np.int16(melody_waveform * (2**15 - 1))

# Play the melody
play_obj = sa.play_buffer(normalized_waveform, 1, 2, sample_rate)
play_obj.wait_done()

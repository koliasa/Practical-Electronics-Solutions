from machine import Pin
import tm1638
import utime

# Define TM1638 pin mappings
stb_pin = 13  # D7
clk_pin = 14  # D5
dio_pin = 12  # D6

# Initialize TM1638 display
display = tm1638.TM1638(stb_pin, clk_pin, dio_pin)

# Function to turn on all segments on a TM1638 display
def turn_on_all_segments(display):
    display.clear()
    display.write([0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF])
    display.write([0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF], pos=8)

# Turn on all segments
turn_on_all_segments(display)

# Wait for a moment before exiting
utime.sleep(5)

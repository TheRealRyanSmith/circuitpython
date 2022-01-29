# Temperature
# Is CPU temp getting warmer or colder?
import time
import board
import microcontroller
from adafruit_macropad import MacroPad

macropad = MacroPad()

def convertF(celsius):
    fahrenheit = (celsius * 1.8) + 32

# Set initial temp value
tprev = microcontroller.cpu.temperature

while True:
    # Get current temp value
    t = microcontroller.cpu.temperature
    # Find difference i ntemp values
    d = t - tprev
    print(t, d)
    # Use difference to control brightness
    macropad.pixels.brightness = abs(d)
    if d < 0:
        # getting colder
        macropad.pixels[3] = (0, 0, 255)
    else:
        # getting warmer
        macropad.pixels[0] = (255, 0, 0)
    # Update previous temp
    tprev = t
    time.sleep(5.0)
    # Turn off pixels
    macropad.pixels.fill((0, 0, 0))
# Temperature
# Is CPU temp getting warmer or colder?
import time
import board
import displayio
import microcontroller
from adafruit_display_text import label
from adafruit_macropad import MacroPad

macropad = MacroPad()

def convertToFahrenheit(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit

# Set initial temp value
tprev = convertToFahrenheit(microcontroller.cpu.temperature)

text_lines = macropad.display_text(title="TEMPRATURE")
text_lines.show()

while True:

    # Get current temp value
    t = convertToFahrenheit(microcontroller.cpu.temperature)
    # Find difference i ntemp values
    d = t - tprev
    text_lines[0].text = (str(t).split(".")[0])
    text_lines[1].text = (str(d).split(".")[0])

    if t > 90:
        macropad.pixels[4] = (255, 0, 0)
    elif t > 80:
        macropad.pixels[4] = (255, 25, 0)
    elif t > 70:
        macropad.pixels[4] = (255, 50, 0)
    elif t > 60:
        macropad.pixels[4] = (150, 50, 0)
    elif t > 50:
        macropad.pixels[4] = (0, 150, 255)
    elif t <= 40:
        macropad.pixels[4] = (0, 0, 255)

    # Use difference to control brightness
    macropad.pixels.brightness = abs(d)
    if d < 0:
        # getting colder
        macropad.pixels[7] = (0, 0, 255)
    else:
        # getting warmer
        macropad.pixels[1] = (255, 0, 0)
    # Update previous temp
    tprev = t
    time.sleep(30.0)
    # Turn off pixels
    macropad.pixels[1] = (0, 0, 0)
    macropad.pixels[7] = (0, 0, 0)
# Temperature
# Is CPU temp getting warmer or colder?
import time
import board
import microcontroller
from adafruit_macropad import MacroPad

macropad = MacroPad()

# Set initial temp value
tprev = microcontroller.cpu.temperature
print("Nostromo")
print("180924609")

macropad.pixels.brightness = 0.6
macropad.pixels[6] = (255, 50, 0)
macropad.pixels[7] = (255, 50, 0)
macropad.pixels[8] = (255, 0, 0)
macropad.pixels[9] = (0, 0, 125)
macropad.pixels[10] = (0, 0, 125)
macropad.pixels[11] = (0, 0, 125)

x = 1

blinkOnDuration = 0.5
blinkOffDuration = 0.25
lastTimeBlinked = -1
pixelFourOn = False
pixelSevenOn = False

while True:


    now = time.monotonic()
    if not pixelFourOn:
        if now >= lastTimeBlinked + blinkOffDuration:
            pixelFourOn = True
            macropad.pixels[4] = (255, 0, 0)
            lastTimeBlinked = now
    if pixelFourOn:
        if now >= lastTimeBlinked + blinkOnDuration:
            pixelFourOn = False
            macropad.pixels[4] = (0, 0, 0)
            # lastTimeBlinked = now

    if not pixelSevenOn:
        if now >= lastTimeBlinked + blinkOffDuration:
            pixelSevenOn = True
            macropad.pixels[7] = (255, 0, 255)
            lastTimeBlinked = now
    if pixelSevenOn:
        if now >= lastTimeBlinked + blinkOnDuration:
            pixelSevenOn = False
            macropad.pixels[7] = (0, 0, 0)
            lastTimeBlinked = now

    # Get current temp value
    t = microcontroller.cpu.temperature
    # Find difference i ntemp values
    d = t - tprev
    # Use difference to control brightness
    # macropad.pixels.brightness = abs(d)
    if d < 0:
        # getting colder
        macropad.pixels[3] = (0, 0, 255)
        macropad.pixels[0] = (0, 0, 0)
    else:
        # getting warmer
        macropad.pixels[0] = (255, 0, 0)
        macropad.pixels[3] = (0, 0, 0)
    macropad.pixels[1] = (0, 200, 50)
    if x > 3:
        macropad.pixels[8] = (0, 0, 0)
        time.sleep(0.2)
        macropad.pixels[8] = (255, 0, 0)
        time.sleep(0.2)
    time.sleep(2)
    macropad.pixels[1] = (0, 0, 0)
    macropad.pixels[2] = (0, 200, 50)
    time.sleep(2)
    macropad.pixels[2] = (0, 0, 0)
    # Update previous temp
    tprev = t
    time.sleep(1)
    print(t)

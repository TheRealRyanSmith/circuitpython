# Blinking randomly, functions, if statement
import board
import microcontroller
import time
import random
from adafruit_macropad import MacroPad

macropad = MacroPad()

print("Light it up")
macropad.pixels.brightness = 1

# Get a random color (redish-orange)
def randomColor():
    a = random.randint(200, 255)
    b = random.randint(0, 50)
    c = random.randint(0, 0)
    return (a, b, c)

# Light up a random pixel
def randomPixel():
    a = random.randint(0, 11)
    macropad.pixels[a] = (randomColor())

x = 0
while True:
    # Choose a random key/pixel and light up
    randomPixel()

    time.sleep(0.5)

    # Get a random pixel and turn it off
    a = random.randint(0, 11)
    macropad.pixels[a] = (0, 0, 0)

    # Making a delay before starting to turn pixels off
    # x += 1
    # if x > 1:
    #     a = random.randint(0, 11)
    #     macropad.pixels[a] = (0, 0, 0)

# Learning random, flow control
import board
import microcontroller
import time
import random
from adafruit_macropad import MacroPad

macropad = MacroPad()

print("Light it up")
macropad.pixels.brightness = 0.2

def randomColor():
    a = random.randint(0, 255)
    b = random.randint(0, 255)
    return (b, 0, a)

while True:

    for i in range(0, 12):
       macropad.pixels[i] = (randomColor())

    time.sleep(4)

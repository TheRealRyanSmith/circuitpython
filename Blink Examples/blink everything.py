# Learning random, flow control
import board
import microcontroller
import time
import random
from adafruit_macropad import MacroPad

macropad = MacroPad()

print("Light it up")
macropad.pixels.brightness = 0.2

def rando():
    return random.randint(0, 50)

def randoColor():
    a = random.randint(50, 255)
    b = random.randint(50, 255)
    c = random.randint(50, 255)
    return (a, b, c)

def randomColor():
    x = random.randint(1, 3)
    if x == 1:
        a = random.randint(0, 255)
        b = 0
        c = 0
        return (a, b, c)
    if x == 2:
        a = 0
        b = random.randint(0, 255)
        c = 0
        return (a, b, c)
    else:
        a = 0
        b = 0
        c = random.randint(0, 255)
        return (a, b, c)
k = 1
def rainbow():
    if k == 1:
        return (255)

while True:

    for i in range(0, 11):
       macropad.pixels[i] = (randomColor())

    time.sleep(1)

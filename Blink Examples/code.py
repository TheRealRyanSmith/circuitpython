# Blinky
import time
import board
import microcontroller
import random
from adafruit_macropad import MacroPad

macropad = MacroPad()

print("Blinky")

macropad.pixels.brightness = 0.2

x = 1

blinkOnDuration = 2
blinkOffDuration = 1
lastTimeBlinked = -1
pixelOn = False
pixelFourOn = False

while True:

    # Randomly turn a pixel on and off
    now = time.monotonic()
    randomKeyA = random.randint(0, 11)
    randomKeyB = random.randint(0, 11)
    randomKeyC = random.randint(0, 11)
    def randomColor():
        randomR = random.randint(0, 255)
        randomG = random.randint(0, 255)
        randomB = random.randint(0, 255)
        randColor = [randomR, randomG, randomB]
        print(randColor)
        return randColor
    if not pixelOn:
        if now >= lastTimeBlinked + blinkOffDuration:
            pixelOn = True
            previousKeyA = randomKeyA
            previousKeyB = randomKeyB
            previousKeyC = randomKeyC
            macropad.pixels[randomKeyA] = (255, 0, 100)
            macropad.pixels[randomKeyB] = (255, 50, 100)
            macropad.pixels[randomKeyC] = (100 , 0, 255)
            # print(randomR, randomG, randomB)
            lastTimeBlinked = now
    if pixelOn:
        if now >= lastTimeBlinked + blinkOnDuration:
            pixelOn = False
            macropad.pixels[previousKeyA] = (0, 0, 0)
            macropad.pixels[previousKeyB] = (0, 0, 0)
            macropad.pixels[previousKeyC] = (0, 0, 0)
            # lastTimeBlinked = now

    # time.sleep(0.5)

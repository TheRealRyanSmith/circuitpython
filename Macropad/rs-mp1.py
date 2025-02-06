# RS–MP1 // First iteration of macropad; using encoder to switch keysets
'''
Macropad
1Finder
2Media
3Figma
4Teams
5Xcode
'''
import time
import board
import displayio
import terminalio
import random
# from adafruit_display_shapes.rect import Rect
from adafruit_display_text import label
# from rainbowio import colorwheel
from adafruit_macropad import MacroPad

macropad = MacroPad()

# ---Display setup--
display = board.DISPLAY
main_group = displayio.Group()
display.show(main_group)

# create the label
row1Label = label.Label(
    font=terminalio.FONT, text="Ready", scale=1
)
row2Label = label.Label(
    font=terminalio.FONT, text="", scale=1
)
row3Label = label.Label(
    font=terminalio.FONT, text="", scale=1
)
row4Label = label.Label(
    font=terminalio.FONT, text="", scale=1
)
row5Label = label.Label(
    font=terminalio.FONT, text="", scale=1
)

# set label position on the display
row1Label.anchor_point = (0, 0)
row1Label.anchored_position = (2, -2)
row2Label.anchor_point = (0, 0)
row2Label.anchored_position = (2, 14)
row3Label.anchor_point = (0, 0)
row3Label.anchored_position = (2, 26)
row4Label.anchor_point = (0, 0)
row4Label.anchored_position = (2, 38)
row5Label.anchor_point = (0, 0)
row5Label.anchored_position = (2, 52)

# add label to group that is showing on display
main_group.append(row1Label)
main_group.append(row2Label)
main_group.append(row3Label)
main_group.append(row4Label)
main_group.append(row5Label)


# --- COLORS (WHITE 0xFFFFFF)
brightness_value = 0.1
def set_brightness_to(brightness_value):
    macropad.pixels.brightness = brightness_value
set_brightness_to(0.2)

# Color Variables
no_fill = 0, 0, 0
cool_white = 60, 160, 200
white = 200, 200, 200
warm_white = 247, 142, 49
red = 205, 0, 0
green = 0, 235, 0
blue = 0, 0, 255
light_blue = 12, 162, 179
orange = 255, 60, 0
yellow = 255, 240, 0
pink = 255, 20, 112
purple = 220, 22, 255
light_purple = 120, 33, 128
sand = 40, 20, 0

# Define macro key colors
def pixels_off():
    for i in range(0, 12):
        macropad.pixels[i] = 0, 0, 0

def defaultColors():
    macropad.pixels[0] = (blue)
    macropad.pixels[1] = (purple)
    macropad.pixels[2] = (purple)
    macropad.pixels[3] = (purple)
    macropad.pixels[4] = (purple)
    macropad.pixels[5] = (purple)
    macropad.pixels[6] = (purple)
    macropad.pixels[7] = (purple)
    macropad.pixels[8] = (purple)
    macropad.pixels[9] = (purple)
    macropad.pixels[10] = (purple)
    macropad.pixels[11] = (purple)

# ---BLINK FUNCTIONS---
def randomColor():
    red = random.randint(0, 0)
    green = random.randint(0, 0)
    blue = random.randint(255, 255)
    return (red, green, blue)

# Light up a random pixel
def randomPixel():
    a = random.randint(0, 11)
    macropad.pixels[a] = (randomColor())

last_position = 0
current_position = last_position
# For blink, switch to decide if pixels should be turned off
turnPixelsOff = True

while True:

    # print(macropad.encoder)
    macropad.encoder_switch_debounced.update()
    if macropad.encoder_switch_debounced.pressed:
        print("Pressed!")
    if macropad.encoder_switch_debounced.released:
        print("Released!")
    if macropad.encoder > last_position:
        last_position = macropad.encoder
    set_brightness_to(brightness_value)
    key_event = macropad.keys.events.get()

    # --- Index ---- ---- ---- ---- ---- ---- ---- ---- ---- ----
    if current_position == 0:
        row1Label.text = "Select Keyset"
        row2Label.text = "[CXL] [Fig] [Colors]"
        row3Label.text = "[BLNK]"
        defaultColors()

        if key_event:
            if key_event.pressed:
                if key_event.key_number == 0:
                    macropad.keyboard.release_all()
                if key_event.key_number == 1:
                    current_position = 1
                    macropad.keyboard.release_all()
                if key_event.key_number == 2:
                    current_position = 2
                    macropad.keyboard.release_all()
                if key_event.key_number == 3:
                    current_position = 3
                    macropad.keyboard.release_all()
                if key_event.key_number == 4:
                    current_position = 4
                    macropad.keyboard.release_all()
                if key_event.key_number == 5:
                    current_position = 5
                    macropad.keyboard.release_all()
                if key_event.key_number == 6:
                    current_position = 6
                    macropad.keyboard.release_all()
                if key_event.key_number == 7:
                    current_position = 7
                    macropad.keyboard.release_all()
                if key_event.key_number == 8:
                    current_position = 8
                    macropad.keyboard.release_all()

    # --- Figma ---- ---- ---- ---- ---- ---- ---- ---- ---- ----
    if current_position == 1:
        # Display and colors
        row1Label.text = "100" + " FIGMA"
        defaultColors()

        if key_event:
            if key_event.pressed:
                if key_event.key_number == 0:
                    current_position = 0
                    macropad.keyboard.release_all()
                if key_event.key_number == 1:
                    macropad.keyboard.send()
                    macropad.keyboard.release_all()

    # --- Sample Colors---- ---- ---- ---- ---- ---- ---- ---- ---- ----
    if current_position == 2:
        # Display and colors
        row1Label.text = "200" + " TRACER 2000"
        row2Label.text = "RED    GREEN  BLUE"
        row3Label.text = "ORANGE YELLOW PINK"
        row4Label.text = "SAND   PURPLE LTBLUE"
        row5Label.text = "COOL   WHITE  WARM"
        defaultColors()

        if key_event:
            if key_event.pressed:
                if key_event.key_number == 0:
                    previous_position = current_position
                    current_position = 0
                    macropad.keyboard.release_all()

    # --- Blink  ---- ---- ---- ---- ---- ---- ---- ---- ---- ----
    if current_position >= 3:
        # Display and colors
        row1Label.text = "300" + " BLINK"
        row2Label.text = "."
        row3Label.text = "."
        row4Label.text = "."
        row5Label.text = "."
        defaultColors()

        if key_event:
            if key_event.pressed:
                if key_event.key_number == 0:
                    current_position = 0
                    macropad.keyboard.release_all()

        # Turn pixels off first loop only
        if turnPixelsOff is True:
            pixels_off()
            turnPixelsOff = False
        # Choose a random key/pixel and light up
        randomPixel()
        time.sleep(0.4)
        # Get a random pixel and turn it off
        a = random.randint(0, 11)
        macropad.pixels[a] = (0, 0, 0)



    # --- Four  ---- ---- ---- ---- ---- ---- ---- ---- ---- ----
    if current_position >= 4:
        # Display and colors
        row1Label.text = "400" + " TEAMS"
        row2Label.text = "."
        row3Label.text = "."
        row4Label.text = "."
        defaultColors()

        if key_event:
            if key_event.pressed:
                if key_event.key_number == 0:
                    current_position = 0
                    macropad.keyboard.release_all()

    # ---Update macroset if encoder position has changed---
    if current_position != last_position:
        last_position = current_position
        turnPixelsOff = True
        row1Label.text = ""
        row2Label.text = ""
        row3Label.text = ""
        row4Label.text = ""
        row5Label.text = ""

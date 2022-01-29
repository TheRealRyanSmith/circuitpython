'''
Macropad
mk2.4
'''
import time
import board
import displayio
import terminalio
import random
from adafruit_display_shapes.rect import Rect
from adafruit_display_text import label
from rainbowio import colorwheel
from adafruit_macropad import MacroPad

macropad = MacroPad()

# ---Display setup--
display = board.DISPLAY
main_group = displayio.Group()
display.show(main_group)

# create the label
row1Label = label.Label(
    font=terminalio.FONT, text="BaseCamp", scale=1
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
brightness_value = 0.5
def set_brightness_to(brightness_value):
    macropad.pixels.brightness = brightness_value
set_brightness_to(0.5)

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
light_purple = 170, 80, 170
sand = 40, 20, 0

''' Color Key
Navigation =
Copy/Paste =

'''

# Define macro key colors
def pixels_off():
    for i in range(0, 12):
        macropad.pixels[i] = 0, 0, 0

def finder_colors():
    macropad.pixels[0] = (blue)
    macropad.pixels[1] = (blue)
    macropad.pixels[2] = (no_fill)
    macropad.pixels[3] = (no_fill)
    macropad.pixels[4] = (no_fill)
    macropad.pixels[5] = (no_fill)
    macropad.pixels[6] = (no_fill)
    macropad.pixels[7] = (no_fill)
    macropad.pixels[8] = (no_fill)
    macropad.pixels[9] = (no_fill)
    macropad.pixels[10] = (no_fill)
    macropad.pixels[11] = (red)

def figma_colors():
    macropad.pixels[0] = (green)
    macropad.pixels[1] = (green)
    macropad.pixels[2] = (orange)
    macropad.pixels[3] = (no_fill)
    macropad.pixels[4] = (no_fill)
    macropad.pixels[5] = (orange)
    macropad.pixels[6] = (blue)
    macropad.pixels[7] = (blue)
    macropad.pixels[8] = (red)
    macropad.pixels[9] = (green)
    macropad.pixels[10] = (green)
    macropad.pixels[11] = (no_fill)

def microsoft_teams_colors():
    macropad.pixels[0] = (no_fill)
    macropad.pixels[1] = (no_fill)
    macropad.pixels[2] = (no_fill)
    macropad.pixels[3] = (no_fill)
    macropad.pixels[4] = (no_fill)
    macropad.pixels[5] = (no_fill)
    macropad.pixels[6] = (no_fill)
    macropad.pixels[7] = (no_fill)
    macropad.pixels[8] = (no_fill)
    macropad.pixels[9] = (orange)
    macropad.pixels[10] = (yellow)
    macropad.pixels[11] = (red)

def calculator_colors():
    macropad.pixels[0] = (white)
    macropad.pixels[1] = (warm_white)
    macropad.pixels[2] = (cool_white)
    macropad.pixels[3] = (white)
    macropad.pixels[4] = (warm_white)
    macropad.pixels[5] = (cool_white)
    macropad.pixels[6] = (white)
    macropad.pixels[7] = (warm_white)
    macropad.pixels[8] = (cool_white)
    macropad.pixels[9] = (white)
    macropad.pixels[10] = (red)
    macropad.pixels[11] = (green)

def win_man_colors():
    macropad.pixels[0] = (no_fill)
    macropad.pixels[1] = (no_fill)
    macropad.pixels[2] = (no_fill)
    macropad.pixels[3] = (green)
    macropad.pixels[4] = (green)
    macropad.pixels[5] = (no_fill)
    macropad.pixels[6] = (green)
    macropad.pixels[7] = (green)
    macropad.pixels[8] = (red)
    macropad.pixels[9] = (blue)
    macropad.pixels[10] = (blue)
    macropad.pixels[11] = (pink)

def sample_colors():
    macropad.pixels[0] = (red)
    macropad.pixels[1] = (green)
    macropad.pixels[2] = (blue)
    macropad.pixels[3] = (orange)
    macropad.pixels[4] = (yellow)
    macropad.pixels[5] = (pink)
    macropad.pixels[6] = (sand)
    macropad.pixels[7] = (purple)
    macropad.pixels[8] = (light_blue)
    macropad.pixels[9] = (cool_white)
    macropad.pixels[10] = (white)
    macropad.pixels[11] = (warm_white)

def brightness_colors():
    macropad.pixels[0] = (blue)
    macropad.pixels[1] = (blue)
    macropad.pixels[2] = (blue)
    macropad.pixels[3] = (blue)
    macropad.pixels[4] = (blue)
    macropad.pixels[5] = (blue)
    macropad.pixels[6] = (blue)
    macropad.pixels[7] = (blue)
    macropad.pixels[8] = (blue)
    macropad.pixels[9] = (blue)
    macropad.pixels[10] = (blue)
    macropad.pixels[11] = (no_fill)

def intensity_ramp():
    macropad.pixels[0] = (0)
    macropad.pixels[1] = (0.1)
    macropad.pixels[2] = (0.2)
    macropad.pixels[3] = (0.3)
    macropad.pixels[4] = (0.4)
    macropad.pixels[5] = (0.5)
    macropad.pixels[6] = (0.6)
    macropad.pixels[7] = (0.7)
    macropad.pixels[8] = (0.8)
    macropad.pixels[9] = (0.9)
    macropad.pixels[10] = (1)

def xcode_colors():
    macropad.pixels[0] = (light_blue)
    macropad.pixels[1] = (light_blue)
    macropad.pixels[2] = (light_blue)
    macropad.pixels[3] = (no_fill)
    macropad.pixels[4] = (no_fill)
    macropad.pixels[5] = (no_fill)
    macropad.pixels[6] = (no_fill)
    macropad.pixels[7] = (no_fill)
    macropad.pixels[8] = (no_fill)
    macropad.pixels[9] = (red)
    macropad.pixels[10] = (no_fill)
    macropad.pixels[11] = (no_fill)

#---BLINK FUNCTIONS---
# Get a random color (redish-orange)
def randomColor():
    a = random.randint(225, 255)
    b = random.randint(0, 50)
    c = random.randint(0, 0)
    return (a, b, c)

# Light up a random pixel
def randomPixel():
    a = random.randint(0, 11)
    macropad.pixels[a] = (randomColor())

last_position = 1
# For blink, switch to decide if pixels should be turned off
turnPixelsOff = True

while True:

    # Set encoder position
    current_position = macropad.encoder

    set_brightness_to(brightness_value)
    key_event = macropad.keys.events.get()

    # --- Brightness  ---- ---- ---- ---- ---- ---- ---- ---- ---- ----
    if current_position == -1:
        # Display and colors
        row1Label.text = "{}".format(macropad.encoder) + " Set Brightness"
        row2Label.text = "OFF    10%    20%"
        row3Label.text = "30%    40%    50%"
        row4Label.text = "60%    70%    80%"
        row5Label.text = "90%   100%    --"
        brightness_colors()
        if key_event:

            if key_event.pressed:
                if key_event.key_number == 0:
                    brightness_value = 0
                    set_brightness_to(brightness_value)
                if key_event.key_number == 1:
                    brightness_value = 0.1
                    set_brightness_to(brightness_value)
                if key_event.key_number == 2:
                    brightness_value = 0.2
                    set_brightness_to(brightness_value)
                if key_event.key_number == 3:
                    brightness_value = 0.3
                    set_brightness_to(brightness_value)
                if key_event.key_number == 4:
                    brightness_value = 0.4
                    set_brightness_to(brightness_value)
                if key_event.key_number == 5:
                    brightness_value = 0.5
                    set_brightness_to(brightness_value)
                if key_event.key_number == 6:
                    brightness_value = 0.6
                    set_brightness_to(brightness_value)
                if key_event.key_number == 7:
                    brightness_value = 0.7
                    set_brightness_to(brightness_value)
                if key_event.key_number == 8:
                    brightness_value = 0.8
                    set_brightness_to(brightness_value)
                if key_event.key_number == 9:
                    brightness_value = 0.9
                    set_brightness_to(brightness_value)
                if key_event.key_number == 10:
                    brightness_value = 1
                    set_brightness_to(brightness_value)

    # --- Finder ---- ---- ---- ---- ---- ---- ---- ---- ---- ----
    if current_position == 0:

        row1Label.text = "{}".format(macropad.encoder) + " Finder"
        row2Label.text = "NAME DATE --"
        row3Label.text = "--"
        row4Label.text = "--"
        row5Label.text = "--     --     DWNLD"

        finder_colors()
        if key_event:
            if key_event.pressed:
                if key_event.key_number == 0:
                    macropad.keyboard.send(
                        macropad.Keycode.CONTROL,
                        macropad.Keycode.OPTION,
                        macropad.Keycode.COMMAND,
                        macropad.Keycode.ONE,
                    )
                    macropad.keyboard.release_all()
                if key_event.key_number == 1:
                    macropad.keyboard.send(
                        macropad.Keycode.CONTROL,
                        macropad.Keycode.OPTION,
                        macropad.Keycode.COMMAND,
                        macropad.Keycode.FOUR,
                    )
                    macropad.keyboard.release_all()
                if key_event.key_number == 11:
                    macropad.keyboard.send(
                        macropad.Keycode.OPTION,
                        macropad.Keycode.COMMAND,
                        macropad.Keycode.L,
                    )
                    macropad.keyboard.release_all()

    # --- Figma ---- ---- ---- ---- ---- ---- ---- ---- ---- ----
    if current_position == 1:
        # Display and colors
        row1Label.text = "{}".format(macropad.encoder) + " Figma"
        row2Label.text = "LAYER  ASSET  PG UP"
        row3Label.text = "SRT X  --     PG DWN"
        row4Label.text = "PREV   NEXT   GOTOMC"
        row5Label.text = "PNG    LINK   --"
        figma_colors()

        if key_event:
            if key_event.pressed:
                if key_event.key_number == 0:
                    macropad.keyboard.send(
                        macropad.Keycode.OPTION, macropad.Keycode.ONE
                    )
                    macropad.keyboard.release_all()
                if key_event.key_number == 1:
                    macropad.keyboard.send(
                        macropad.Keycode.OPTION, macropad.Keycode.TWO
                    )
                    macropad.keyboard.release_all()
                if key_event.key_number == 2:
                    macropad.keyboard.send(macropad.Keycode.PAGE_UP)
                if key_event.key_number == 3:
                    macropad.keyboard.send(
                        macropad.Keycode.SHIFT,
                        macropad.Keycode.COMMAND,
                        macropad.Keycode.OPTION,
                        macropad.Keycode.CONTROL,
                        macropad.Keycode.G
                    )
                    macropad.keyboard.release_all()
                if key_event.key_number == 5:
                    macropad.keyboard.send(macropad.Keycode.PAGE_DOWN)
                if key_event.key_number == 6:
                    macropad.keyboard.send(
                        macropad.Keycode.SHIFT,
                        macropad.Keycode.COMMAND,
                        macropad.Keycode.LEFT_BRACKET,
                    )
                    macropad.keyboard.release_all()
                if key_event.key_number == 7:
                    macropad.keyboard.send(
                        macropad.Keycode.SHIFT,
                        macropad.Keycode.COMMAND,
                        macropad.Keycode.RIGHT_BRACKET,
                    )
                    macropad.keyboard.release_all()
                if key_event.key_number == 8:
                    macropad.keyboard.send(
                        macropad.Keycode.CONTROL,
                        macropad.Keycode.OPTION,
                        macropad.Keycode.SHIFT,
                        macropad.Keycode.COMMAND,
                        macropad.Keycode.C,
                    )
                    macropad.keyboard.release_all()
                if key_event.key_number == 9:
                    macropad.keyboard.send(
                        macropad.Keycode.SHIFT,
                        macropad.Keycode.COMMAND,
                        macropad.Keycode.C,
                    )
                    macropad.keyboard.release_all()
                if key_event.key_number == 10:
                    macropad.keyboard.send(
                        macropad.Keycode.OPTION,
                        macropad.Keycode.SHIFT,
                        macropad.Keycode.COMMAND,
                        macropad.Keycode.V,
                    )
                    macropad.keyboard.release_all()

    # --- Microsoft Teams  ---- ---- ---- ---- ---- ---- ---- ---- ---- ----
    if current_position == 2:
        # Display and colors
        row1Label.text = "{}".format(macropad.encoder) + " Microsoft Teams"
        row2Label.text = "--"
        row3Label.text = "--"
        row4Label.text = "--"
        row5Label.text = "VIDEO  HAND   MUTE"
        microsoft_teams_colors()

        if key_event:
            if key_event.pressed:
                if key_event.key_number == 9:
                    # Video on/off
                    macropad.keyboard.send(
                        macropad.Keycode.COMMAND,
                        macropad.Keycode.SHIFT,
                        macropad.Keycode.L,
                    )
                    macropad.keyboard.release_all()
                # Raise/lower hand
                if key_event.key_number == 10:
                    macropad.keyboard.send(
                        macropad.Keycode.COMMAND,
                        macropad.Keycode.SHIFT,
                        macropad.Keycode.K,
                    )
                    macropad.keyboard.release_all()
                # Mute/unmute
                if key_event.key_number == 11:
                    macropad.keyboard.send(
                        macropad.Keycode.COMMAND,
                        macropad.Keycode.SHIFT,
                        macropad.Keycode.OPTION,
                        macropad.Keycode.CONTROL,
                        macropad.Keycode.F,
                    )
                    macropad.keyboard.release_all()
                    macropad.keyboard.send(
                        macropad.Keycode.COMMAND,
                        macropad.Keycode.SHIFT,
                        macropad.Keycode.M,
                    )
                    macropad.keyboard.release_all()

            else:
                microsoft_teams_colors()

    # --- Calculator  ---- ---- ---- ---- ---- ---- ---- ---- ---- ----
    if current_position == 3:
        # Display and colors
        row1Label.text = "{}".format(macropad.encoder) + " Calculator"
        row2Label.text = "7    8      9"
        row3Label.text = "4    5      6"
        row4Label.text = "1    2      3"
        row5Label.text = "0    DELETE RTRN"
        calculator_colors()

        if key_event:
            if key_event.pressed:
                # Every key event
                key = key_event.key_number
                macropad.pixels[key] = colorwheel(270)

                # Keys 0-10
                if key_event.key_number == 0:
                    macropad.keyboard.send(macropad.Keycode.SEVEN)
                if key_event.key_number == 1:
                    macropad.keyboard.send(macropad.Keycode.EIGHT)
                if key_event.key_number == 2:
                    macropad.keyboard.send(macropad.Keycode.NINE)
                if key_event.key_number == 3:
                    macropad.keyboard.send(macropad.Keycode.FOUR)
                if key_event.key_number == 4:
                    macropad.keyboard.send(macropad.Keycode.FIVE)
                if key_event.key_number == 5:
                    macropad.keyboard.send(macropad.Keycode.SIX)
                if key_event.key_number == 6:
                    macropad.keyboard.send(macropad.Keycode.ONE)
                if key_event.key_number == 7:
                    macropad.keyboard.send(macropad.Keycode.TWO)
                if key_event.key_number == 8:
                    macropad.keyboard.send(macropad.Keycode.THREE)
                if key_event.key_number == 9:
                    macropad.keyboard.send(macropad.Keycode.ZERO)
                if key_event.key_number == 10:
                    macropad.keyboard.send(macropad.Keycode.BACKSPACE)
                if key_event.key_number == 11:
                    macropad.keyboard.send(macropad.Keycode.ENTER)

            else:
                calculator_colors()

    # --- Window Management ---- ---- ---- ---- ---- ---- ---- ---- ---- ----
    if current_position == 4:
        # Display and colors
        row1Label.text = "{}".format(macropad.encoder) + " Window Management"
        row2Label.text = "--"
        row3Label.text = "UL     UR"
        row4Label.text = "LL     LR      MAX"
        row5Label.text = "LEFT   RIGHT   CENTER"
        win_man_colors()

        if key_event:
            if key_event.pressed:
                if key_event.key_number == 3:
                    macropad.keyboard.send(
                        macropad.Keycode.CONTROL,
                        macropad.Keycode.OPTION,
                        macropad.Keycode.U,
                    )
                    macropad.keyboard.release_all()
                if key_event.key_number == 4:
                    macropad.keyboard.send(
                        macropad.Keycode.CONTROL,
                        macropad.Keycode.OPTION,
                        macropad.Keycode.I,
                    )
                    macropad.keyboard.release_all()
                if key_event.key_number == 6:
                    macropad.keyboard.send(
                        macropad.Keycode.CONTROL,
                        macropad.Keycode.OPTION,
                        macropad.Keycode.J,
                    )
                    macropad.keyboard.release_all()
                if key_event.key_number == 7:
                    macropad.keyboard.send(
                        macropad.Keycode.CONTROL,
                        macropad.Keycode.OPTION,
                        macropad.Keycode.K,
                    )
                    macropad.keyboard.release_all()
                if key_event.key_number == 8:
                    macropad.keyboard.send(
                        macropad.Keycode.CONTROL,
                        macropad.Keycode.OPTION,
                        macropad.Keycode.UP_ARROW,
                    )
                    macropad.keyboard.release_all()
                if key_event.key_number == 9:
                    macropad.keyboard.send(
                        macropad.Keycode.CONTROL,
                        macropad.Keycode.OPTION,
                        macropad.Keycode.LEFT_ARROW,
                    )
                    macropad.keyboard.release_all()
                if key_event.key_number == 10:
                    macropad.keyboard.send(
                        macropad.Keycode.CONTROL,
                        macropad.Keycode.OPTION,
                        macropad.Keycode.RIGHT_ARROW,
                    )
                    macropad.keyboard.release_all()
                if key_event.key_number == 11:
                    macropad.keyboard.send(
                        macropad.Keycode.CONTROL,
                        macropad.Keycode.OPTION,
                        macropad.Keycode.DOWN_ARROW,
                    )
                    macropad.keyboard.release_all()

    # --- Xcode  ---- ---- ---- ---- ---- ---- ---- ---- ---- ----
    if current_position == 5:
        # Display and colors
        row1Label.text = "{}".format(macropad.encoder) + " Xcode"
        row2Label.text = "LFT    MID    RHT"
        row3Label.text = "--"
        row4Label.text = "--"
        row5Label.text = "PLAY/PAUSE"
        xcode_colors()

        if key_event:

            if key_event.pressed:
                if key_event.key_number == 0:
                    macropad.keyboard.send(
                        macropad.Keycode.COMMAND,
                        macropad.Keycode.ZERO
                    )
                    macropad.keyboard.release_all()
                if key_event.key_number == 1:
                    macropad.keyboard.send(
                        macropad.Keycode.COMMAND,
                        macropad.Keycode.SHIFT,
                        macropad.Keycode.Y
                    )
                    macropad.keyboard.release_all()
                if key_event.key_number == 2:
                    macropad.keyboard.send(
                        macropad.Keycode.COMMAND,
                        macropad.Keycode.OPTION,
                        macropad.Keycode.ZERO
                    )
                    macropad.keyboard.release_all()
                if key_event.key_number == 9:
                    macropad.keyboard.send(
                        macropad.Keycode.COMMAND,
                        macropad.Keycode.OPTION,
                        macropad.Keycode.SHIFT,
                        macropad.Keycode.CONTROL,
                        macropad.Keycode.Y
                    )
                    macropad.keyboard.release_all()

    # --- Sample Colors---- ---- ---- ---- ---- ---- ---- ---- ---- ----
    if current_position == 6:
        # Display and colors
        row1Label.text = "{}".format(macropad.encoder) + " Sample Colors"
        row2Label.text = "RED    GREEN  BLUE"
        row3Label.text = "ORANGE YELLOW PINK"
        row4Label.text = "SAND   PURPLE LTBLUE"
        row5Label.text = "COOL   WHITE  WARM"
        sample_colors()

    # --- Blink  ---- ---- ---- ---- ---- ---- ---- ---- ---- ----
    if current_position >= 7:
        # Display and colors
        row1Label.text = "{}".format(macropad.encoder) + " Blink"
        row2Label.text = "."
        row3Label.text = "."
        row4Label.text = "."
        row5Label.text = "."

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

    # --- Template  ---- ---- ---- ---- ---- ---- ---- ---- ---- ----
    if current_position == 8:
        # Display and colors
        row1Label.text = "{}".format(macropad.encoder) + " Template"
        row2Label.text = "--"
        row3Label.text = "--"
        row4Label.text = "--"
        row5Label.text = "--"
        template_colors()

        if key_event:

            if key_event.pressed:
                if key_event.key_number == 0:
                    macropad.keyboard.send(macropad.Keycode.F1)
                if key_event.key_number == 1:
                    macropad.keyboard.send(macropad.Keycode.F1)
                if key_event.key_number == 2:
                    macropad.keyboard.send(macropad.Keycode.F1)
                if key_event.key_number == 3:
                    macropad.keyboard.send(macropad.Keycode.F1)
                if key_event.key_number == 4:
                    macropad.keyboard.send(macropad.Keycode.F1)
                if key_event.key_number == 5:
                    macropad.keyboard.send(macropad.Keycode.F1)
                if key_event.key_number == 6:
                    macropad.keyboard.send(macropad.Keycode.F1)
                if key_event.key_number == 7:
                    macropad.keyboard.send(macropad.Keycode.F1)
                if key_event.key_number == 8:
                    macropad.keyboard.send(macropad.Keycode.F1)
                if key_event.key_number == 9:
                    macropad.keyboard.send(macropad.Keycode.F1)
                if key_event.key_number == 10:
                    macropad.keyboard.send(macropad.Keycode.F1)
                if key_event.key_number == 11:
                    macropad.keyboard.send(macropad.Keycode.F1)

    # ---Update display with encoder position---
    if current_position >= 9:
        # Display and colors
        row1Label.text = "{}".format(macropad.encoder)

    #---Update macroset if encoder position has changed---
    if current_position != last_position:
        last_position = current_position
        # For blink, reset switch
        turnPixelsOff = True

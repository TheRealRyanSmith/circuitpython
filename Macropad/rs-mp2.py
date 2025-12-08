# RS–MP2 // Second iteration of macropad
import time
import random
import displayio
import terminalio
from adafruit_display_text import label
from adafruit_macropad import MacroPad

macropad = MacroPad()

# ---Display setup--
display = macropad.display
main_group = displayio.Group()
display.root_group = main_group

# create the label
row1Label = label.Label(font=terminalio.FONT, text="Ready", scale=1)
row2Label = label.Label(font=terminalio.FONT, text="", scale=1)
row3Label = label.Label(font=terminalio.FONT, text="", scale=1)
row4Label = label.Label(font=terminalio.FONT, text="", scale=1)
row5Label = label.Label(font=terminalio.FONT, text="", scale=1)

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

# Color Variables
no_fill = 0, 0, 0
cool_white = 130, 150, 255
white = 200, 200, 200
warm_white = 255, 150, 130
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255
light_blue = 12, 162, 179
orange = 255, 40, 0
yellow = 255, 255, 0
pink = 255, 20, 112
purple = 255, 22, 255
light_purple = 170, 80, 170
sand = 40, 20, 0


def sample_colors():
    macropad.pixels[0] = red
    macropad.pixels[1] = warm_white
    macropad.pixels[2] = warm_white
    macropad.pixels[3] = warm_white
    macropad.pixels[4] = warm_white
    macropad.pixels[5] = warm_white
    macropad.pixels[6] = cool_white
    macropad.pixels[7] = cool_white
    macropad.pixels[8] = cool_white
    macropad.pixels[9] = cool_white
    macropad.pixels[10] = cool_white
    macropad.pixels[11] = cool_white


# Get a random color value
def randomColor(min, max):
    red = random.randint(min, max)
    green = random.randint(min, max)
    blue = random.randint(min, max)
    return (red, green, blue)


# Light up a random pixel
def randomPixel():
    random_key = random.randint(0, 11)
    macropad.pixels[random_key] = randomColor(0, 200)

# Turn pixels off
turnPixelsOff = False

def pixels_off():
    for i in range(0, 12):
        macropad.pixels[i] = 0, 0, 0

# Set brightness of neopixels
def set_brightness_to(value):
    macropad.pixels.brightness = value

set_brightness_to(0.05)

# Example usage
original_min = 0
original_max = 25
target_min = 0.0
target_max = 1.0
value = 0


def scale_value(value, original_min, original_max, target_min, target_max):
    # Calculate the scaled value
    value_1 = (value - original_min) / (original_max - original_min)
    value_2 = (target_max - target_min) + target_min
    scaled_value = value_1 * value_2
    return scaled_value


current_key_set = 0
last_encoder_position = 0
current_encoder_position = last_encoder_position
turnPixelsOff = True

while True:
    # set_brightness_to(brightness_value)
    # Listen for key events
    key_event = macropad.keys.events.get()

    if current_key_set == 0:
        row1Label.text = "Select keyset  RS-MP1"
        row2Label.text = " ---   FIGMA"
        row3Label.text = "[ x ]  [ x ]  [ x ]"
        row4Label.text = "[ x ]  [ x ]  [ x ]"
        row5Label.text = "[ x ]  X4     MATRIX"
        sample_colors()
        if key_event:
            print(key_event)
            if key_event.released:
                if 0 <= key_event.key_number <= 11:
                    macropad.keyboard.release_all()
                    current_key_set = key_event.key_number
                    
        current_encoder_position = macropad.encoder
        
        if current_encoder_position > last_encoder_position:
            macropad.keyboard.press(macropad.Keycode.OPTION, macropad.Keycode.SHIFT)
            macropad.keyboard.press(macropad.Keycode.F12)
            macropad.keyboard.release_all()
            print("Fine volume up")
        elif current_encoder_position < last_encoder_position:
            macropad.keyboard.press(macropad.Keycode.OPTION, macropad.Keycode.SHIFT)
            macropad.keyboard.press(macropad.Keycode.F11)
            macropad.keyboard.release_all()
            print("Fine volume down")
        last_encoder_position = current_encoder_position
        time.sleep(0.05)

    # --- [1] Figma ---- ---- ---- ---- ---- ---- ---- ---- ---- ----
    if current_key_set == 1:
        row1Label.text = "[1] Figma     RS-MP1"
        row2Label.text = "[X]    LIB    GOMAIN"
        row3Label.text = "CPLINK LIB    SELECT"

        def figma_colors():
            macropad.pixels[0] = red
            macropad.pixels[1] = green
            macropad.pixels[2] = green
            macropad.pixels[3] = green
            macropad.pixels[4] = green
            macropad.pixels[5] = green
            macropad.pixels[6] = cool_white
            macropad.pixels[7] = cool_white
            macropad.pixels[8] = cool_white
            macropad.pixels[9] = cool_white
            macropad.pixels[10] = cool_white
            macropad.pixels[11] = cool_white

        figma_colors()
        if key_event:
            if key_event.pressed:
                if key_event.key_number == 0:
                    current_key_set = 0
                    macropad.keyboard.release_all()
                # Library panel
                if key_event.key_number == 1:
                    macropad.keyboard.press(
                        macropad.Keycode.LEFT_SHIFT, macropad.Keycode.I
                    )
                    macropad.keyboard.release_all()
                # Go to main component
                if key_event.key_number == 2:
                    macropad.keyboard.press(
                        macropad.Keycode.CONTROL, macropad.Keycode.G
                    )
                    macropad.keyboard.release_all()
                # Copy link to selection
                if key_event.key_number == 3:
                    macropad.keyboard.press(
                        macropad.Keycode.COMMAND, macropad.Keycode.L
                    )
                    macropad.keyboard.release_all()
        macropad.encoder_switch_debounced.update()
        if macropad.encoder_switch_debounced.pressed:
            # Zoom to 100%
            macropad.keyboard.press(macropad.Keycode.COMMAND, macropad.Keycode.ZERO)
            macropad.keyboard.release_all()

    # --- [02] ---- ---- ---- ---- ---- ---- ---- ---- ---- ----
    if current_key_set == 2:
        row1Label.text = "[2] Empty    RS-MP1"
        row2Label.text = "[ x ]  [ x ]  [ x ]"
        row3Label.text = "[ x ]  [ x ]  [ x ]"
        row4Label.text = "[ x ]  [ x ]  [ x ]"
        row5Label.text = "[ x ]  [ x ]  [ x ]"
        if key_event:
            if key_event.pressed:
                if key_event.key_number == 0:
                    current_key_set = 0
                    macropad.keyboard.release_all()
                if key_event.key_number == 1:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 2:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 3:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 4:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 5:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 6:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 7:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 8:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 9:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 10:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 11:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()

    # --- [03] ---- ---- ---- ---- ---- ---- ---- ---- ---- ----
    if current_key_set == 3:
        row1Label.text = "[3] Empty    RS-MP1"
        row2Label.text = "[ x ]  [ x ]  [ x ]"
        row3Label.text = "[ x ]  [ x ]  [ x ]"
        row4Label.text = "[ x ]  [ x ]  [ x ]"
        row5Label.text = "[ x ]  [ x ]  [ x ]"
        if key_event:
            if key_event.pressed:
                if key_event.key_number == 0:
                    current_key_set = 0
                    macropad.keyboard.release_all()
                if key_event.key_number == 1:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 2:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 3:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 4:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 5:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 6:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 7:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 8:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 9:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 10:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 11:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                    
    # --- [04] ---- ---- ---- ---- ---- ---- ---- ---- ---- ----
    if current_key_set == 4:
        row1Label.text = "[4] Empty    RS-MP1"
        row2Label.text = "[ x ]  [ x ]  [ x ]"
        row3Label.text = "[ x ]  [ x ]  [ x ]"
        row4Label.text = "[ x ]  [ x ]  [ x ]"
        row5Label.text = "[ x ]  [ x ]  [ x ]"
        if key_event:
            if key_event.pressed:
                if key_event.key_number == 0:
                    current_key_set = 0
                    macropad.keyboard.release_all()
                if key_event.key_number == 1:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 2:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 3:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 4:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 5:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 6:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 7:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 8:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 9:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 10:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 11:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                    
    # --- [05] ---- ---- ---- ---- ---- ---- ---- ---- ---- ----
    if current_key_set == 5:
        row1Label.text = "[5] Empty    RS-MP1"
        row2Label.text = "[ x ]  [ x ]  [ x ]"
        row3Label.text = "[ x ]  [ x ]  [ x ]"
        row4Label.text = "[ x ]  [ x ]  [ x ]"
        row5Label.text = "[ x ]  [ x ]  [ x ]"
        if key_event:
            if key_event.pressed:
                if key_event.key_number == 0:
                    current_key_set = 0
                    macropad.keyboard.release_all()
                if key_event.key_number == 1:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 2:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 3:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 4:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 5:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 6:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 7:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 8:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 9:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 10:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 11:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                    
    # --- [06] ---- ---- ---- ---- ---- ---- ---- ---- ---- ----
    if current_key_set == 6:
        row1Label.text = "[6] Empty    RS-MP1"
        row2Label.text = "[ x ]  [ x ]  [ x ]"
        row3Label.text = "[ x ]  [ x ]  [ x ]"
        row4Label.text = "[ x ]  [ x ]  [ x ]"
        row5Label.text = "[ x ]  [ x ]  [ x ]"
        if key_event:
            if key_event.pressed:
                if key_event.key_number == 0:
                    current_key_set = 0
                    macropad.keyboard.release_all()
                if key_event.key_number == 1:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 2:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 3:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 4:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 5:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 6:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 7:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 8:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 9:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 10:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 11:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                    
    # --- [07] ---- ---- ---- ---- ---- ---- ---- ---- ---- ----
    if current_key_set == 7:
        row1Label.text = "[7] Empty    RS-MP1"
        row2Label.text = "[ x ]  [ x ]  [ x ]"
        row3Label.text = "[ x ]  [ x ]  [ x ]"
        row4Label.text = "[ x ]  [ x ]  [ x ]"
        row5Label.text = "[ x ]  [ x ]  [ x ]"
        if key_event:
            if key_event.pressed:
                if key_event.key_number == 0:
                    current_key_set = 0
                    macropad.keyboard.release_all()
                if key_event.key_number == 1:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 2:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 3:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 4:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 5:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 6:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 7:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 8:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 9:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 10:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 11:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                    
    # --- [08] ---- ---- ---- ---- ---- ---- ---- ---- ---- ----
    if current_key_set == 8:
        row1Label.text = "[8] Empty    RS-MP1"
        row2Label.text = "[ x ]  [ x ]  [ x ]"
        row3Label.text = "[ x ]  [ x ]  [ x ]"
        row4Label.text = "[ x ]  [ x ]  [ x ]"
        row5Label.text = "[ x ]  [ x ]  [ x ]"
        if key_event:
            if key_event.pressed:
                if key_event.key_number == 0:
                    current_key_set = 0
                    macropad.keyboard.release_all()
                if key_event.key_number == 1:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 2:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 3:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 4:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 5:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 6:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 7:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 8:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 9:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 10:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 11:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                    
    # --- [09] Teams ---- ---- ---- ---- ---- ---- ---- ---- ---- ----
    if current_key_set == 9:
        row1Label.text = "[9] Teams    RS-MP1"
        row2Label.text = "[ x ]  [ x ]  [ x ]"
        row3Label.text = "[ x ]  [ x ]  [ x ]"
        row4Label.text = "[ x ]  [ x ]  [ x ]"
        row5Label.text = "[ x ]  MUTE   [ x ]"
        if key_event:
            if key_event.pressed:
                if key_event.key_number == 0:
                    current_key_set = 0
                    macropad.keyboard.release_all()
                if key_event.key_number == 1:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 2:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 3:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 4:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 5:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 6:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 7:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 8:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 9:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 10:
                    macropad.keyboard.press(
                        macropad.Keycode.LEFT_SHIFT,
                        macropad.Keycode.COMMAND,
                        macropad.Keycode.M,
                    )
                    macropad.keyboard.release_all()
                if key_event.key_number == 11:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()

                if key_event.key_number == 10:
                    macropad.keyboard.press(
                        macropad.Keycode.LEFT_SHIFT,
                        macropad.Keycode.COMMAND,
                        macropad.Keycode.M,
                    )
                    macropad.keyboard.release_all()

    # --- [10] ---- ---- ---- ---- ---- ---- ---- ---- ---- ----
    if current_key_set == 10:
        row1Label.text = "[10] Empty    RS-MP1"
        row2Label.text = "[ x ]  [ x ]  [ x ]"
        row3Label.text = "[ x ]  [ x ]  [ x ]"
        row4Label.text = "[ x ]  [ x ]  [ x ]"
        row5Label.text = "[ x ]  [ x ]  [ x ]"
        if key_event:
            if key_event.pressed:
                if key_event.key_number == 0:
                    current_key_set = 0
                    macropad.keyboard.release_all()
                if key_event.key_number == 1:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 2:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 3:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 4:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 5:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 6:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 7:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 8:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 9:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 10:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 11:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()

    # --- MATRIX ---- ---- ---- ---- ---- ----
    if current_key_set == 11:

        def get_column_set(value):
            if value == 1:
                return [0, 3, 6, 9]
            elif value == 2:
                return [1, 4, 7, 10]
            else:
                return [2, 5, 8, 11]

        def get_random_column():
            random_column = random.randint(1, 3)
            return get_column_set(random_column)

        column = get_random_column()
        print(column)
        time.sleep(0.01)

        def rain(speed, a, b, c, d):
            macropad.pixels[a] = green
            time.sleep(speed)
            pixels_off()
            macropad.pixels[b] = green
            time.sleep(speed)
            pixels_off()
            macropad.pixels[c] = green
            time.sleep(speed)
            pixels_off()
            macropad.pixels[d] = green
            time.sleep(speed)
            pixels_off()

    # Turn pixels off first loop only
    if turnPixelsOff is True:
        pixels_off()
        turnPixelsOff = False

    # --- [XX] EMPTY TEMPLATE ---- ---- ---- ---- ---- ---- ---- ---- ---- ----
    if current_key_set == 99:
        row1Label.text = "[X] Empty    RS-MP1"
        row2Label.text = "[ x ]  [ x ]  [ x ]"
        row3Label.text = "[ x ]  [ x ]  [ x ]"
        row4Label.text = "[ x ]  [ x ]  [ x ]"
        row5Label.text = "[ x ]  [ x ]  [ x ]"
        if key_event:
            if key_event.pressed:
                if key_event.key_number == 0:
                    current_key_set = 0
                    macropad.keyboard.release_all()
                if key_event.key_number == 1:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 2:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 3:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 4:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 5:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 6:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 7:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 8:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 9:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 10:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
                if key_event.key_number == 11:
                    macropad.keyboard.press()
                    macropad.keyboard.release_all()
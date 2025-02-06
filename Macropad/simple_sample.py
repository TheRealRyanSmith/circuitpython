import time
from adafruit_macropad import MacroPad

macropad = MacroPad()  # Initialize MacroPad
last_position = macropad.encoder

# Set NeoPixel color (R, G, B) - Example: Red
macropad.pixels[0] = (255, 0, 0)  # Lights up the first NeoPixel in red
macropad.pixels[1] = (0, 255, 0)
macropad.pixels[2] = (0, 0, 255)
macropad.pixels.show()  # Update the LED state

while True:
    key_event = macropad.keys.events.get()
    position = macropad.encoder

    if key_event:
        print(key_event)
    if key_event and key_event.pressed:
        if key_event.key_number == 0:
            macropad.keyboard.press(macropad.Keycode.F15)
            macropad.keyboard.release_all()

    if position > last_position:
        macropad.keyboard.release_all()
        print("Dial position: ", position)

    if position < last_position:
        macropad.keyboard.release_all()
        print("Dial position: ", position)

    time.sleep(0.3)
    last_position = position

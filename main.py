def on_button_pressed_a():
    basic.show_icon(IconNames.HEART)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    basic.show_number(randint(1, 6))
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

basic.show_string("Hi!")
basic.clear_screen()
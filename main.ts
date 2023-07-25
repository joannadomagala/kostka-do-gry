input.onButtonPressed(Button.A, function () {
    basic.showIcon(IconNames.Heart)
})
input.onButtonPressed(Button.B, function () {
    basic.clearScreen()
})
input.onGesture(Gesture.Shake, function () {
    basic.showNumber(randint(1, 6))
    basic.pause(2000)
    basic.clearScreen()
})
basic.showString("Hi!")
basic.clearScreen()

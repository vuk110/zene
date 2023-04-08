zene = 0

def on_button_pressed_a():
    if True:
        music.play_tone(349, music.beat(BeatFraction.DOUBLE))
        music.play_tone(262, music.beat(BeatFraction.DOUBLE))
    basic.pause(100)
    if True:
        music.play_tone(330, music.beat(BeatFraction.DOUBLE))
        music.play_tone(349, music.beat(BeatFraction.DOUBLE))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global zene
    zene = 1
    basic.pause(3000)
    zene = 2
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    if True:
        music.play_tone(359, music.beat(BeatFraction.WHOLE))
        basic.pause(10)
        music.play_tone(774, music.beat(BeatFraction.WHOLE))
        basic.pause(10)
        music.play_tone(870, music.beat(BeatFraction.WHOLE))
        basic.pause(10)
        music.play_tone(870, music.beat(BeatFraction.WHOLE))
    basic.pause(100)
    if True:
        music.play_tone(784, music.beat(BeatFraction.WHOLE))
        music.play_tone(784, music.beat(BeatFraction.WHOLE))
        music.play_tone(880, music.beat(BeatFraction.WHOLE))
        music.play_tone(880, music.beat(BeatFraction.WHOLE))
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    pass
basic.forever(on_forever)

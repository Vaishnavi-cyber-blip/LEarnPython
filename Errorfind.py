import pygame as py
py.mixer.init()
file = 'drink.mp3'
i = 1
py.mixer.music.load(file)
py.mixer.music.play(-1)
while i != 2:
    print("TYPE: 'DRANK'\nFor closing the reminder")
    close = input().upper()
    if close == "DRANK":
        py.mixer.music.pause()
        i = i+1
    else:
        py.mixer.music.unpause()
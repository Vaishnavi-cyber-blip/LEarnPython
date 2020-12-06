import time
import datetime
import pygame as py
py.mixer.init()


def water_sip():
    f = open("breakbantahai.txt", "a")
    file = 'drink.mp3'
    i = 1
    while i != 2:
        py.mixer.music.load(file)
        py.mixer.music.play(-1)
        print("TYPE: 'DRANK'\nFor closing the reminder")
        c = input().upper()
        if c == "DRANK":
            py.mixer.music.pause()
            i = i+1
            f.write(str(datetime.datetime.now()))
            f.write('\n')
            f.write(" "+c+" ")
            f.close()


def exercise():
    f = open("breakbantahai.txt", "a")
    f1 = 'exercise.mp3'
    i = 1
    py.mixer.music.load(f1)
    py.mixer.music.play(-1)
    while i != 2:
        print("TYPE: 'DONE'\nFor closing the reminder")
        c = input().upper()
        if c == "DONE":
            py.mixer.music.pause()
            i = i+1
            f.write('\n')
            f.write(str(datetime.datetime.now()))
            f.write('\n')
            f.write(" "+c+" ")
            f.close()


def eyes():
    f = open("breakbantahai.txt", "a")
    f2 = 'eye.mp3'
    i = 1
    py.mixer.music.load(f2)
    py.mixer.music.play(-1)
    while i != 2:
        print("TYPE: 'SUPER'\nFor closing the reminder")
        c = input().upper()
        if c == "SUPER":
            py.mixer.music.pause()
            i = i + 1
            f.write('\n')
            f.write(str(datetime.datetime.now()))
            f.write('\n')
            f.write(" "+c+" ")
            f.close()


if __name__ == '__main__':
    while True:
        water_sip()
        time.sleep(40*60)
        eyes()
        water_sip()
        time.sleep(30*60)
        exercise()
        water_sip()
        time.sleep(30*60)

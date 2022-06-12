# coding=utf-8

from gpiozero import Button
import datetime


def toRegie1A():
    print('REGIE1A')

def toRegie1B():
    print('REGIE1B')

def toRegie2A():
    print('REGIE2A')

def toRegie2B():
    print('REGIE2B')


button1 = Button(5)
button1.when_pressed = toRegie1A

button2 = Button(6)
button2.when_pressed = toRegie1B

button3 = Button(13)
button3.when_pressed = toRegie2A

button4 = Button(19)
butten4.when_pressed = toRegie2B

while True:
    print('waiting....')
    sleep(2)

print("Goodbye!")

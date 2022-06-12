# coding=utf-8

from gpiozero import Button
import datetime
import time

def genConnectTo(to):
    def wrapper():
        print('Connect to ' + to)
    return wrapper

def genDisconnectFrom(from):
    def wrapper():
        print('Disconnect from ' + from)
    return wrapper

button1 = Button(5)
button1.when_pressed = genConnectTo("Regie1A")
button1.when_released = genDisconnectFrom("Regie1A")

button2 = Button(6)
button2.when_pressed = genConnectTo("Regie2A")
button1.when_released = genDisconnectFrom("Regie2A")

# button3 = Button(13)
# button3.when_pressed = toRegie2A
#
# button4 = Button(19)
# button4.when_pressed = toRegie2B

while True:
    print('waiting....')
    time.sleep(10)

print("Goodbye!")

# coding=utf-8

from gpiozero import Button
import datetime
import time

def genConnectTo(to):
    def wrapper():
        print('Connect to ' + to)
    return wrapper

def genDisconnectDevice(device):
    def wrapper():
        print('Disconnect from ' + device)
    return wrapper

input_mapping_A = {
    5 : "Regie1A",
    6 : "Regie1B",
    13 : "Regie2A",
    19 : "Regie2B"
}

for pin in input_mapping_A:
    button = Button(pin)
    button.when_pressed = genConnectTo(input_mapping_A[pin])
    button.when_released = genDisconnectDevice(input_mapping_A[pin])

while True:
    print('waiting....')
    time.sleep(10)

print("Goodbye!")

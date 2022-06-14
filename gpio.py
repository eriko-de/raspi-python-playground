from gpiozero import Button
import time

def genConnectTo(to):
    print("setup calback for " + to)
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

buttons = []

for pin in input_mapping_A:
    print(pin)
    buttons.append(Button(pin))
    print(input_mapping_A[pin])
    buttons[len(buttons) - 1].when_pressed = genConnectTo(input_mapping_A[pin])
    buttons[len(buttons) - 1].when_released = genDisconnectDevice(input_mapping_A[pin])

while True:
    print('waiting....')
    time.sleep(10)

print("Goodbye!")

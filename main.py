import yaml

from adderlib import adder

config = yaml.safe_load(open("config.yml"))

# Create a handle to the API by passing the IP address or hostname of the AIM (the KVM server)
api = adder.AdderAPI(config['KVM_IP'])

# Log in using an exising KVM account
api.login(config['KVM_USER'], config['KVM_PW'])

# Get DigiSpot devices
# DigiSpot1 = next(api.getChannels(config['DigiSpot1_id']))
# DigiSpot2 = next(api.getChannels(config['DigiSpot2_id']))

def connectToChannel(rx_id, ch_id):
  try:
    rx = next(api.getReceivers(rx_id))
    ch = next(api.getChannels(ch_id))
    print(f"Connecting {ch.name} to {rx.name}")
    api.connectToChannel(channel=ch, receiver=rx)
  except StopIteration:
    print("No device found with given id")

def disconnectReceiver(rx_id):
  try:
    rx = next(api.getReceivers(rx_id))
    print(f"Disconnecting {rx.name} from {rx.channel_name}")
    api.disconnectFromChannel(rx)
  except StopIteration:
    print("No device found with given id")

try:
  while True:
    action = input('Was willst du tuen? [c]onnect, [d]isconnect, [a]bort')
    print(action)
    if action == 'a':
      break
    elif action == 'c':
      print('Please enter receiver id to connect to')
      rx_id = input('Bitte gebe die id des Receivers ein:')
      ch_id = input('Geb die Channel id ein')
      connectToChannel(rx_id, ch_id)
    elif action == 'd':
      print('disconnecting devices')
      rx_id = input('Bitte gebe die id des Receivers ein:')
      disconnectReceiver(rx_id)
    else:
      print('No valid input, aborting')
      break
finally:
  # Don't forget to log out!
  print('logging out')
  api.logout()

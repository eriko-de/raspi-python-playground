while True:
  action = input('Was willst du tuen? [c]onnect, [d]isconnect, [a]bort')
  print(action)
  if action == 'a':
    break
  elif action == 'c':
    print('connecting devices')
  elif action == 'd':
    print('disconnecting devices')
  else:
    print('No valid input, aborting')
    break
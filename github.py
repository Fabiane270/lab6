def encoder(user_password): 
  user_password = list(user_password)
  for i in user_password:
    i = int(i)
    i += 3
  return ''.join(user_password)


if __name__ == '__main__':
  while True: 
    print('\nMenu\n-------------\n1. Encode\n2. Decode\n3. Quit')
    option = input('\nPlease enter an option: ')
    try:
      option = int(option)
      if 1 <= option <= 3:
        if option == 1:
          global user_password
          user_password = input('Please enter your password to encode: ')
          print(encoder(user_password))
          print('Your password has been encoded and stored!')
        elif option == 2: 
          pass
        elif option == 3:
          exit()
      else: 
        continue
    except TypeError:
      continue

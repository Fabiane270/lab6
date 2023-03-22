def encoder(user_password): # Logic error in orginal function where it would not chnage the list, fixed and updated -Andrew
  user_password = list(user_password)
  for i in range(len(user_password)):
    user_password[i] = str(int(user_password[i]) + 3)
  return ''.join(user_password) # Returns the encoded password

def decode_password(encoded_password): #decoded password function by Andrew Griner
  decoded_password_str = ''
  for char in encoded_password:
    decoded_char = str((int(char) - 3) % 10) #Returns it to orginal password
    decoded_password_str += decoded_char #add to string
  return decoded_password_str #returns the result

if __name__ == '__main__':
  while True:
    print('\nMenu\n-------------\n1. Encode\n2. Decode\n3. Quit')
    option = input('\nPlease enter an option: ')

    try:
      option = int(option)

      if 1 <= option <= 3:
        if option == 1:
          user_password = input('Please enter your password to encode: ')
          encoded_password = encoder(user_password) #runs the function
          #Took out print statment
          print('Your password has been encoded and stored!')
        elif option == 2:
          decoded_password = decode_password(encoded_password)
          print("The encoded password is ", encoded_password, " and the original password is ", decoded_password, " .") #displays the encoded password and orginal
        elif option == 3:
          exit() #option to end the program
      else:
        continue

    except TypeError: #to aviod EOF error
      continue
 #Parter was Andrew, I fixed the encoder, did the decoder, fixed whitespace. tried the program on 3/9 and worked,

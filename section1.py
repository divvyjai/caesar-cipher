import random
# Imports the random module

alphabet = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
# A tuple is used here, as it automatically assigns integer values to each key

alphabetrev = {
    "A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10, "L": 11, "M": 12, "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17, "S": 18, "T": 19, "U": 20, "V": 21, "W": 22, "X": 23, "Y": 24, "Z": 25
}
# A dictionary is used here as the letter needs to be used as a key, not an integer


while True:
  encryptordecrypt = input("\nWould you like to encrypt a message or decrypt a message? ")
  if (encryptordecrypt.lower() != "encrypt" and encryptordecrypt.lower() != "decrypt"):
    print("\nPlease enter either encrypt or decrypt")
    # If the input is not either encrypt or decrypt, the program will ask the user to reenter their choice
  else:
    break
    # If the input is in the correct format, the program will break the loop

while True:
  key = input("\nWhat shift key would you like to use? (enter 'random' for a random shift key) ")
  if key == "random":
    key = random.randint(1, 25)
    # If the user enters 'random', a random integer between 1 and 25 is generated and assigned to the key variable
    break
    # If the input is in the correct format, the program will break the loop
  elif (int(key) > 27) or (int(key) < 0):
    print("\nPlease enter a number from 1-25")
    # If the input is not in the correct format, the program will ask the user to reenter their choice
  elif key != "random":
    print("\nPlease enter either a valid integer or 'random'")
    # If the input is not in the correct format, the program will ask the user to reenter their choice
  else:
    break
    # If the input is in the correct format, the program will break the loop

if (encryptordecrypt.lower() == "encrypt"):
  initialphrase = input("\nEnter the phrase you would like to encrypt: ")

  keyedphrase = ""
  # Creates a variable to use in the for loop

  for i in initialphrase:
    if (i.isalpha()):
      # Checks if the character is a letter
      keyedletterint = (alphabetrev[i.upper()] + int(key)) % 26
      # Adds 3 to the letter's number, then mods it by 26 to make sure it is a number between 1 and 26
      keyedletter = alphabet[keyedletterint]
      # Gets the letter from the alphabet dictionary
      keyedphrase = keyedphrase + keyedletter
      # Adds the letter to the keyed phrase
    else:
      keyedphrase = keyedphrase
      # If the character is not a letter, it will not add anything to the dekeyed phrase
  
  print(" ")
  print(keyedphrase)

elif (encryptordecrypt.lower() == "decrypt"):

  initialphrase = input("Enter the phrase you would like to decrypt: ")

  dekeyedphrase = ""
  # Creates a variable to use in the for loop

  for i in initialphrase:
    if (i.isalpha()):
      # Checks if the character is a letter
      dekeyedletterint = (alphabetrev[i.upper()] - int(key)) % 26
      # Subtracts 3 from the letter's number, then mods it by 26 to make sure it is a number between 1 and 26
      dekeyedletter = alphabet[dekeyedletterint]
      # Gets the letter from the alphabet dictionary
      dekeyedphrase = dekeyedphrase + dekeyedletter
      # Adds the letter to the dekeyed phrase
    else:
      dekeyedphrase = dekeyedphrase
      # If the character is not a letter, it will not add anything to the dekeyed phrase

  print(" ")
  print(dekeyedphrase)
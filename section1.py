import random
# Imports the random module

alphabet = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
# A tuple is used here, as it automatically assigns integer values to each key

alphabetRev = {
    "A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10, "L": 11, "M": 12, "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17, "S": 18, "T": 19, "U": 20, "V": 21, "W": 22, "X": 23, "Y": 24, "Z": 25
}
# A dictionary is used here as the letter needs to be used as a key, not an integer


while True:
  encryptOrDecrypt = input("\nWould you like to encrypt a message or decrypt a message? ")
  if (encryptOrDecrypt.lower() != "encrypt" and encryptOrDecrypt.lower() != "decrypt"):
    print("\nPlease enter either encrypt or decrypt")
    # If the input is not either encrypt or decrypt, the program will ask the user to reenter their choice
  else:
    break
    # If the input is in the correct format, the program will break the loop

while True:
  key = input("\nWhat shift key would you like to use? (enter 'random' for a random shift key): ")
  if key == "random":
    key = random.randint(1, 25)
    # If the user enters 'random', a random integer between 1 and 25 is generated and assigned to the key variable
    break
    # If the input is in the correct format, the program will break the loop
  elif (1<= int(key) <= 25):
    break
  else:
    print("\nPlease enter either a valid integer or 'random'")
    # If the input is not in the correct format, the program will ask the user to reenter their choice

if (encryptOrDecrypt.lower() == "encrypt"):
  while True:
    initialPhrase = input("\nEnter the phrase you would like to encrypt: ")
    # Asks the user what phrase they would like to encrypt
    if(initialPhrase == ""):
      print("\nPlease enter a phrase")
    else:
      break

  keyedPhrase = ""
  # Creates a variable to use in the for loop

  for i in initialPhrase:
    if (i.isalpha()):
      # Checks if the character is a letter
      keyedLetterInt = (alphabetRev[i.upper()] + int(key)) % 26
      # Adds the key to the letter's number, then mods it by 26 to make sure it is a number between 1 and 26
      keyedLetter = alphabet[keyedLetterInt]
      # Gets the letter from the alphabet dictionary
      keyedPhrase = keyedPhrase + keyedLetter
      # Adds the letter to the keyed phrase
    elif(i == " "):
      keyedPhrase = keyedPhrase + " "
      # If the character is a whitespace, it will add a whitespace to the keyed phrase
    else:
      keyedPhrase = keyedPhrase
      # If the character is not a letter, it will not add anything to the keyed phrase

  print("\nThe encrypted phrase is:" + keyedPhrase)

elif (encryptOrDecrypt.lower() == "decrypt"):
  while True:
    initialPhrase = input("\nEnter the phrase you would like to decrypt: ")
    # Asks the user what phrase they would like to decrypt
    if(initialPhrase == ""):
      print("\nPlease enter a phrase")
    else:
      break

  dekeyedPhrase = ""
  # Creates a variable to use in the for loop

  for i in initialPhrase:
    if (i.isalpha()):
      # Checks if the character is a letter
      dekeyedLetterInt = (alphabetRev[i.upper()] - int(key)) % 26
      # Subtracts the key from the letter's number, then mods it by 26 to make sure it is a number between 1 and 26
      dekeyedLetter = alphabet[dekeyedLetterInt]
      # Gets the letter from the alphabet dictionary
      dekeyedPhrase = dekeyedPhrase + dekeyedLetter
      # Adds the letter to the dekeyed phrase
    else:
      dekeyedPhrase = dekeyedPhrase
      # If the character is not a letter, it will not add anything to the dekeyed phrase

  print("\nThe decrypted phrase is: " + dekeyedPhrase)
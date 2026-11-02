import random
# Imports the random module

alphabet = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
# A tuple is used here, as it automatically assigns integer values to each key

alphabetRev = {
    "A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10, "L": 11, "M": 12, "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17, "S": 18, "T": 19, "U": 20, "V": 21, "W": 22, "X": 23, "Y": 24, "Z": 25
}
# A dictionary is used here as the letter needs to be used as a key, not an integer

keyList = {}

encryptOrDecrypt = input("\nWould you like to encrypt or decrypt? ")

print("\nIn order for the program to work correctly, you must enter the tuple shift, and then the key to shift. For example, if you would like to use a shift with a key of 3 from the 2nd character of a phrase, you would first enter 2, and then for the second prompt you would enter 3. \nContinue this process until you have entered all the shifts that you would like to use. If you would like to use a pre-existing tuple shift list, enter 'list'. \nOnce you have entered all the shifts you would like to use, enter 'quit'.")
# Gives the user instructions on how to enter the tuple shifts

shiftEntry = 0

while True:
  shiftInput = input("\nEnter the tuple shift: ")
  if(shiftInput=='quit'):
    break
  elif(shiftInput=='list'):
    keyList = {0: {"key":0,"shift":2}, 1: {"key":3,"shift":5}, 2: {"key":14,"shift":8}, 3: {"key":13,"shift":5}, 4: {"key":23,"shift":9}, 5: {"key":13,"shift":3}, 6: {"key":17,"shift":7}, 7: {"key":2,"shift":6}, 8: {"key":13,"shift":7}, 9: {"key":22,"shift":4}, 10: {"key":17,"shift":6}, 11: {"key":2,"shift":14}, 12: {"key":5,"shift":12}, 13: {"key":14,"shift":3}, 14: {"key":17,"shift":7}, 15: {"key":14,"shift":10}}
    # If the user wants to use a pre-existing list of tuple shifts, they can enter 'list'
    break
  else:
    keyInput = input("Enter the key to shift: ")
    # Asks the user what key they would like to use
    keyList[shiftEntry] = {"key":int(keyInput), "shift":int(shiftInput)}
    # Enters both the key and the shift into the dictionary
    print(keyList)
    # Prints the dictionary so the user knows what tuple shifts they've added already
    shiftEntry += 1
    
i = 0
j = 1
finalPhraseDict = {}
# These variables are all created to use in the for loops

if(encryptOrDecrypt.lower()=="encrypt"):
  phrase = input("\nEnter the phrase you would like to encrypt: ")
  shiftSum = 0
  while(i < len(keyList)):
    keyedPhrase = ""
    # Creates an empty variable each time the loop runs
    a = 0
    key = keyList[i]["key"]
    for n in phrase:
      if (n.isalpha()):
        # Checks if the character is a letter
        keyedLetterInt = (alphabetRev[n.upper()] + key) % 26
        # Adds the shift key to the letter's corresponding number in the dictionary, then mods it by 26 to make sure it is a number between 1 and 26
        keyedLetter = alphabet[keyedLetterInt]
        # Gets the letter from the alphabet dictionary
        keyedPhrase = keyedPhrase + keyedLetter
        # Adds the letter to the keyed phrase
      elif(n==" "):
        keyedPhrase = keyedPhrase + " "
        # If the character is a whitespace, it will add a whitespace to the keyed phrase
      else:
        keyedPhrase = keyedPhrase
        # If the character is neither a letter nor a whitespace, it will not add anything to the keyed phrase

    shiftSum = 0
    
    if(i==0):
      index = int(keyList[i]["shift"])
    else:
      while a < (len(keyList)-1):
        shiftSum = shiftSum + int(keyList[a]["shift"])
        a += 1
      index = int(keyList[i]["shift"]) - shiftSum
    
    index = int(keyList[i]["shift"])
    # Gets the shift location from the tuple list
    finalPhraseDict[i] = keyedPhrase[:index]
    # Used to get the first n letters of the keyed phrase, where n is the number of characters to keep the same before doing a shift. The new phrase is put into the final dictionary
    keyedPhrase = keyedPhrase[index:]
    # Used to get the remaining letters of the keyed phrase, in order to repeat the tuple shift process
    phrase = keyedPhrase
    # Changes the already existing 'phrase' variable to the new shortened and keyed phrase, to repeat the tuple shift process
  
    i += 1
    # Increases i by 1 to repeat the process

elif(encryptOrDecrypt.lower()=="decrypt"):
  phrase = input("\nEnter the phrase you would like to decrypt: ")
  shiftSum = 0
  while(i < len(keyList)):
    keyedPhrase = ""
    # Creates an empty variable each time the loop runs
    a = 0
    key = keyList[i]["key"]
    for n in phrase:
      if (n.isalpha()):
        # Checks if the character is a letter
        keyedLetterInt = (alphabetRev[n.upper()] - key) % 26
        # Adds the shift key to the letter's corresponding number in the dictionary, then mods it by 26 to make sure it is a number between 1 and 26
        keyedLetter = alphabet[keyedLetterInt]
        # Gets the letter from the alphabet dictionary
        keyedPhrase = keyedPhrase + keyedLetter
        # Adds the letter to the keyed phrase
      elif(n==" "):
        keyedPhrase = keyedPhrase + " "
        # If the character is a whitespace, it will add a whitespace to the keyed phrase
      else:
        keyedPhrase = keyedPhrase
        # If the character is neither a letter nor a whitespace, it will not add anything to the keyed phrase

    shiftSum = 0

    if(i==0):
      index = int(keyList[i]["shift"])
    else:
      while a < (len(keyList)-1):
        shiftSum = shiftSum + int(keyList[a]["shift"])
        a += 1
      index = int(keyList[i]["shift"]) - shiftSum

    index = int(keyList[i]["shift"])
    # Gets the shift location from the tuple list
    finalPhraseDict[i] = keyedPhrase[:index]
    # Used to get the first n letters of the keyed phrase, where n is the number of characters to keep the same before doing a shift. The new phrase is put into the final dictionary
    keyedPhrase = keyedPhrase[index:]
    # Used to get the remaining letters of the keyed phrase, in order to repeat the tuple shift process
    phrase = keyedPhrase
    # Changes the already existing 'phrase' variable to the new shortened and keyed phrase, to repeat the tuple shift process

    i += 1
    # Increases i by 1 to repeat the process

finalPhrase = ""

for x in finalPhraseDict:
  finalPhrase = finalPhrase + finalPhraseDict[x]
  # Adds each word of the dictoinary to the finalphrase

finalPhrase = finalPhrase + phrase
# In case the tuple shift list does not cover the entire original phrase, the rest of the phrase is added to the final phrase

print("\n" + finalPhrase)
# Prints the final phrase
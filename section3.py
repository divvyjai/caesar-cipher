import random
# Imports the random module

alphabet = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
# A tuple is used here, as it automatically assigns integer values to each key

alphabetrev = {
    "A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10, "L": 11, "M": 12, "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17, "S": 18, "T": 19, "U": 20, "V": 21, "W": 22, "X": 23, "Y": 24, "Z": 25
}
# A dictionary is used here as the letter needs to be used as a key, not an integer

keylist = ((0,2), (2,5), (7,15), (5,10), (6,24), (5,1), (4,20), (0,18), (3,8), (2,17), (4,23), (6,12), (4,2), (1,19), (3,5))
# This is a tuple containing the combinations of tuple shifts that will be used to encode. This could be randomised, however if you want the encoded text to be decoded by another person, then you must know the tuple shifts and keys that were used.

phrase = input("\nEnter the phrase you would like to encrypt: ")

i = 0
j = 1
finalphrasedict = {}
# These variables are all created to use in the for loops

while(i <= 14):
# 14 is chosen here as that is how many tuple shift combinations there are (including a combination with a key of 0), this number can be changed if more combinations are added
  keyedphrase = ""
  # Creates an empty variable each time the loop runs
  key = keylist[i][1]
  # Grabs the key from the tuple list
  for n in phrase:
    if (n.isalpha()):
      # Checks if the character is a letter
      keyedletterint = (alphabetrev[n.upper()] + key) % 26
      # Adds the shift key to the letter's corresponding number in the dictionary, then mods it by 26 to make sure it is a number between 1 and 26
      keyedletter = alphabet[keyedletterint]
      # Gets the letter from the alphabet dictionary
      keyedphrase = keyedphrase + keyedletter
      # Adds the letter to the keyed phrase
    else:
      keyedphrase = keyedphrase + " "

  index = keylist[i][0]
  # Gets the tuple shift from the tuple list
  finalphrasedict[i] = keyedphrase[:index]
  # Used to get the first n letters of the keyed phrase, where n is the number of characters to keep the same before doing a shift. The new phrase is put into the final dictionary
  keyedphrase = keyedphrase[index:]
  # Used to get the remaining letters of the keyed phrase, in order to repeat the tuple shift process
  phrase = keyedphrase
  # Changes the already existing 'phrase' variable to the new shortened and keyed phrase, to repeat the tuple shift process

  i += 1
  # Increases i by 1 to repeat the process

finalphrase = ""

for x in finalphrasedict:
  finalphrase = finalphrase + finalphrasedict[x]

print(" ")
# Extra line break to avoid clutter in the output
print(finalphrase)
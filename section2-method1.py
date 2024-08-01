alphabet = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
# A tuple is used here, as it automatically assigns integer values to each key

alphabetrev = {
    "A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10, "L": 11, "M": 12, "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17, "S": 18, "T": 19, "U": 20, "V": 21, "W": 22, "X": 23, "Y": 24, "Z": 25
}
# A dictionary is used here as the letter needs to be used as a key, not a number

initialphrase = input("Enter the phrase you would like to decrypt: ")

key = 1
# Sets the shift key to 1, which is the minimum value

while key <= 25:
# This process will repeat until the key is 25, which is the maximum value, as anything past this will loop back to the beginning of the alphabet
  dekeyedphrase = ""
  # Creates a variable to use in the for loop

  for i in initialphrase:
    if (i.isalpha()): 
    # Checks if the character is a letter
      dekeyedletterint = (alphabetrev[i.upper()] - key) % 26
      # Subtracts the key from the letter's corresponding number in the dictionary, then mods it by 26 to make sure it is a number between 1 and 26
      dekeyedletter = alphabet[dekeyedletterint]
      # Gets the letter from the alphabet dictionary
      dekeyedphrase = dekeyedphrase + dekeyedletter
      # Adds the letter to the dekeyed phrase
    elif (i == " "):
      dekeyedphrase = dekeyedphrase + " "
      # If the character is a whitespace, it will add a space to the dekeyed phrase
    else:
      dekeyedphrase = dekeyedphrase
      # If the character is neither a letter nor a whitespace, it will not add anything to the dekeyed phrase (as this decoder ignores numbers and other symbols)
  
  print(" ")
  # Extra line to avoid clutter in the output
  print("Trying key =", str(key) + ":", dekeyedphrase)
  
  key += 1
  # Increases the key by 1, and repeats the process until the key is 25
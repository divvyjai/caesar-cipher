alphabet = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
# A tuple is used here, as it automatically assigns integer values to each key

alphabetrev = {
    "A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10, "L": 11, "M": 12, "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17, "S": 18, "T": 19, "U": 20, "V": 21, "W": 22, "X": 23, "Y": 24, "Z": 25
}
# A dictionary is used here as the letter needs to be used as a key, not an integer

chivalues = {
    "A": 0.082, "B": 0.015, "C": 0.028, "D": 0.043, "E": 0.127, "F": 0.022, "G": 0.02, "H": 0.061, "I": 0.07, "J": 0.0015, "K": 0.0077, "L": 0.04, "M": 0.024, "N": 0.067, "O": 0.075, "P": 0.019, "Q": 0.00095, "R": 0.06, "S": 0.063, "T": 0.091, "U": 0.028, "V": 0.0098, "W": 0.024, "X": 0.0015, "Y": 0.02, "Z": 0.00074
}
# This dictionary contains the relative frequencies of each letter, according to https://en.wikipedia.org/wiki/Letter_frequency

finaldekeydict = {}
# Creates an empty dictionary to store the final dekeyed phrases

finalchidict = {}
# Creates an empty dictionary to store the final Chi values

initialphrase = input("Enter the phrase you would like to decrypt: ")

key = 1
# Sets the key to 1, which is the minimum value

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
    
    lettercountdict = {}
    # Creates an empty dictionary to store the letter counts

    for i in dekeyedphrase.lower():
        if(i == " "):
            pass
            # This will not do anything, as whitespaces will remain as whitespaces in the final dekeyed phrase
        else:
            lettercountdict[str(i)] = (dekeyedphrase.lower()).count(str(i))
            # For each letter in the dekeyed phrase, this will count how many times it appears and stores that number in a dictionary

    phraselength = len(dekeyedphrase)
    # Gets the total length of the phrase to use in later calculations

    phrasechi = 0
    # Creates a variable to store the total Chi value
    
    for i in lettercountdict:
        count = lettercountdict[str(i)]
        # Gets the count of the letter from the dictionary
        expectedcount = (chivalues[str(i).upper()])*phraselength
        # Finds the expected count by multiplying the actual count by its relative frequency
        chi = ((count - expectedcount)*(count - expectedcount))/expectedcount
        # Finds the Chi value for that letter
        phrasechi = phrasechi + chi
        # Adds this Chi value to the total Chi value of the phrase
    
    finaldekeydict[key] = dekeyedphrase
    # Adds the dekeyed phrase to the final dekeyed phrase dictionary
    finalchidict[key] = phrasechi
    # Adds the Chi value to the final Chi value dictionary

    key += 1
    # Increases the key by 1, and repeats the process

minimumchikey = min(finalchidict, key = finalchidict.get)
# Finds the lowest value in the Chi dictinary, and then gets the key for that value

print(" ")
# Extra line break to avoid clutter in the output
print("The dekeyed phrase is " + finaldekeydict[minimumchikey] + ", with a shift key of " + str(minimumchikey))
alphabet = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
# A tuple is used here, as it automatically assigns integer values to each key

alphabetRev = {
    "A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10, "L": 11, "M": 12, "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17, "S": 18, "T": 19, "U": 20, "V": 21, "W": 22, "X": 23, "Y": 24, "Z": 25
}
# A dictionary is used here as the letter needs to be used as a key, not an integer

chiValues = {
    "A": 0.082, "B": 0.015, "C": 0.028, "D": 0.043, "E": 0.127, "F": 0.022, "G": 0.02, "H": 0.061, "I": 0.07, "J": 0.0015, "K": 0.0077, "L": 0.04, "M": 0.024, "N": 0.067, "O": 0.075, "P": 0.019, "Q": 0.00095, "R": 0.06, "S": 0.063, "T": 0.091, "U": 0.028, "V": 0.0098, "W": 0.024, "X": 0.0015, "Y": 0.02, "Z": 0.00074
}
# This dictionary contains the relative frequencies of each letter, according to https://en.wikipedia.org/wiki/Letter_frequency

finalDekeyDict = {}
# Creates an empty dictionary to store the final dekeyed phrases
finalChiDict = {}
# Creates an empty dictionary to store the final Chi values

wordlistFile = open("Files/wordlist.txt", "r") 
# Opening the wordlist as a file in read only mode
data = wordlistFile.read() 
# Reading the file and converting it to a string
wordlist = data.split("\n")
# Splitting the string into a list where the newlines used to be


while True:
    initialPhrase = input("\nEnter the phrase you would like to decrypt: ")
    method = input("\nEnter the method you would like to use (chi/wordlist/both) Note: Wordlist method requires there to be spaces between the words in the phrase: ")
    # Asks the user the phrase they would like to decrypt and what method they would like to use

    def chi_method(initialPhrase):
        key = 1
        # Sets the key to 1, which is the minimum value
        while key <= 25:
        # This process will repeat until the key is 25, which is the maximum value, as anything past this will loop back to the beginning of the alphabet
            dekeyedPhrase = ""
            # Creates a variable to use in the for loop
            for i in initialPhrase:
                if (i.isalpha()): 
                    # Checks if the character is a letter
                    dekeyedLetterInt = (alphabetRev[i.upper()] - key) % 26
                    # Subtracts the key from the letter's corresponding number in the dictionary, then mods it by 26 to make sure it is a number between 1 and 26
                    dekeyedLetter = alphabet[dekeyedLetterInt]
                    # Gets the letter from the alphabet dictionary
                    dekeyedPhrase = dekeyedPhrase + dekeyedLetter
                    # Adds the letter to the dekeyed phrase
                elif (i == " "):
                  dekeyedPhrase = dekeyedPhrase + " "
                  # If the character is a whitespace, it will add a space to the dekeyed phrase
                else:
                  dekeyedPhrase = dekeyedPhrase
                  # If the character is neither a letter nor a whitespace, it will not add anything to the dekeyed phrase

            key += 1
            # Increases the key by 1, and repeats the process

            letterCountDict = {}
            # Creates an empty dictionary to store the letter counts

            for i in dekeyedPhrase.lower():
                if(i == " "):
                    pass
                    # This will not do anything, as whitespaces will remain as whitespaces in the final dekeyed phrase
                else:
                    letterCountDict[str(i)] = (dekeyedPhrase.lower()).count(str(i))
                    # For each letter in the dekeyed phrase, this will count how many times it appears and stores that number in a dictionary

            phraseLength = len(dekeyedPhrase)
            # Gets the total length of the phrase to use in later calculations

            phraseChi = 0
            # Creates a variable to store the total Chi value

            for i in letterCountDict:
                count = letterCountDict[str(i)]
                # Gets the count of the letter from the dictionary
                expectedCount = (chiValues[str(i).upper()])*phraseLength
                # Finds the expected count by multiplying the actual count by its relative frequency
                chi = ((count - expectedCount)*(count - expectedCount))/expectedCount
                # Finds the Chi value for that letter
                phraseChi = phraseChi + chi
                # Adds this Chi value to the total Chi value of the phrase

            finalDekeyDict[key] = dekeyedPhrase
            # Adds the dekeyed phrase to the final dekeyed phrase dictionary
            finalChiDict[key] = phraseChi
            # Adds the Chi value to the final Chi value dictionary

        minimumChiKey = min(finalChiDict, key = finalChiDict.get)
        # Finds the lowest value in the Chi dictionary, and then gets the key for that value

        print("\nUsing the chi method, the dekeyed phrase is " + finalDekeyDict[minimumChiKey] + ", with a shift key of " + str(minimumChiKey-1))

    def wordlist_method(initialPhrase):
        key = 1
        # Sets the key to 1, which is the minimum value
        q = 1
        c = {}
        while key <= 25:
            # This process will repeat until the key is 25, which is the maximum value, as anything past this will loop back to the beginning of the alphabet
            dekeyedPhrase = ""
            # Creates a variable to use in the for loop
            for i in initialPhrase:
                if (i.isalpha()): 
                    # Checks if the character is a letter
                    dekeyedLetterInt = (alphabetRev[i.upper()] - key) % 26
                    # Subtracts the key from the letter's corresponding number in the dictionary, then mods it by 26 to make sure it is a number between 1 and 26
                    dekeyedLetter = alphabet[dekeyedLetterInt]
                    # Gets the letter from the alphabet dictionary
                    dekeyedPhrase = dekeyedPhrase + dekeyedLetter
                    # Adds the letter to the dekeyed phrase
                elif (i == " "):
                  dekeyedPhrase = dekeyedPhrase + " "
                  # If the character is a whitespace, it will add a space to the dekeyed phrase
                else:
                  dekeyedPhrase = dekeyedPhrase
                  # If the character is neither a letter nor a whitespace, it will not add anything to the dekeyed phrase (as this decoder ignores numbers and other symbols)

                finalDekeyDict[key] = dekeyedPhrase
                # Adds the dekeyed phrase to the final dekeyed phrase dictionary

            key += 1

        while q <= len(finalDekeyDict):
            # This will continue for each word in the dictionary
            c[q] = 0
            # Sets the initial count to 0
            phrase = finalDekeyDict[q]
            # Gets the phrase from the dictionary
            phraseList = phrase.split()
            # Splits the phrase into a dictionary
            for i in phraseList:
                if i.lower() in wordlist:
                    # If the word is in the wordlist, nothing will happen
                    pass
                else:
                    c[q] += 1
                    # If the word is not in the wordlist, the count will increase by 1
            q += 1
            # Increase q by 1 to repeat the process
        
        minimumCScore = min(c, key=c.get)
        # Gets the key with the lowest count in the c dictionary
        
        print("\nUsing the wordlist method, the dekeyed phrase is " + finalDekeyDict[minimumCScore] + ", with a shift key of " + str(minimumCScore))

    if(method.lower() == "chi"):
        chi_method(initialPhrase)
        # Prints the phrase decrypted with the Chi method
        break
    elif(method.lower() == "wordlist"):
        wordlist_method(initialPhrase)
        # Prints the phrase decrypted with the wordlist method
        break
    elif(method.lower() == "both"):
        chi_method(initialPhrase)
        wordlist_method(initialPhrase)
        # Prints the phrase decrypted with both methods
        break
    else:
        print("\nPlease enter a valid method")
import random
# The random module is imported

alphabet = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
# A tuple is used here, as it automatically assigns integer values to each key

alphabetRev = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7,
    "I": 8,
    "J": 9,
    "K": 10,
    "L": 11,
    "M": 12,
    "N": 13,
    "O": 14,
    "P": 15,
    "Q": 16,
    "R": 17,
    "S": 18,
    "T": 19,
    "U": 20,
    "V": 21,
    "W": 22,
    "X": 23,
    "Y": 24,
    "Z": 25
}
# A dictionary is used here as the letter needs to be used as a key, not an integer

chiValues = {
    "A": 0.082,
    "B": 0.015,
    "C": 0.028,
    "D": 0.043,
    "E": 0.127,
    "F": 0.022,
    "G": 0.02,
    "H": 0.061,
    "I": 0.07,
    "J": 0.0015,
    "K": 0.0077,
    "L": 0.04,
    "M": 0.024,
    "N": 0.067,
    "O": 0.075,
    "P": 0.019,
    "Q": 0.00095,
    "R": 0.06,
    "S": 0.063,
    "T": 0.091,
    "U": 0.028,
    "V": 0.0098,
    "W": 0.024,
    "X": 0.0015,
    "Y": 0.02,
    "Z": 0.00074
}
# This dictionary contains the relative frequencies of each letter, according to https://en.wikipedia.org/wiki/Letter_frequency

wordlistFile = open("Files/wordlist.txt", "r")
# Opening the wordlist as a file in read only mode
data = wordlistFile.read()
# Reading the file and converting it to a string
wordlist = data.split("\n")
# Splitting the string into a list where the newlines used to be

while True:
    encryptOrDecrypt = input("\nWould you like to encrypt or decrypt a message? ")
    # Asks the user whether they would like to encrypt or decrypt a message
    if (encryptOrDecrypt.lower() == "encrypt"):
        phrase = input("\nEnter the phrase you would like to encrypt: ")
        phrase.strip()
        for t in phrase:
            if(t.isalpha()):
                pass
            elif(t.isdigit()):
                pass
            elif(t==" "):
                pass
            else:
                phrase = phrase.replace(t, "")
        # Asks the user what phrase they would like to encrypt
        break
    elif (encryptOrDecrypt.lower() == "decrypt"):
        phrase = input("\nEnter the phrase you would like to decrypt (enter 'random' for a random selection of words from the wordlist): ")
        phrase.strip()
        for t in phrase:
            if(t.isalpha()):
                pass
            elif(t.isdigit()):
                pass
            elif(t==" "):
                pass
            else:
                phrase = phrase.replace(t, "")
        # Asks the user what phrase they would like to decrypt, or enter 'random' to get a random selection of words from the wordlist
        break
    else:
        print("Please enter either encrypt or decrypt")
        # If the user enters and invalid input, the program will ask them to reenter their choice

t = 1
targetPhrase = ""
# These variables are created to use in the below loop

while (t <= random.randint(5, 20)):
    targetPhrase = targetPhrase + " " + random.choice(wordlist)
    # random.choice is used to select multiple random words from the wordlist
    t += 1
    # Increases t by 1 to loop again


def encryptString(target):
    # This is the function that will shift each word in the random phrase by a random key
    i = 0
    j = 1
    finalPhraseDict = {}
    # These variables are all created to use in the for loops

    tempDict = target.split()
    # A temporary dictionary is used to store the words in the phrase

    while (i <= (len(tempDict) - 1)):
        keyedPhrase = ""
        # Creates an empty variable each time the loop runs
        key = random.randint(1, 25)
        # Generates a random key to use for encrypting each word
        for n in target:
            # For each letter in the word
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
                # Adds a whitespace if the character is a space
            else:
                keyedPhrase = keyedPhrase + n
                # If the character is neither a letter nor a whitespace, it will add that to the phrase (as all symbols have been stripped already)

        finalPhraseDict[i] = (keyedPhrase.split())[i]
        # Adds the keyed phrase to the final dictionary
        target = keyedPhrase
        # Changes the already existing 'target' variable to the new keyed phrase, to repeat the keying process
        i += 1
        # Increases i by 1 to repeat the process

    finalPhrase = ""
    # Creates an empty variable to store the final phrase

    for x in finalPhraseDict:
        finalPhrase = finalPhrase + " " + finalPhraseDict[x]
        # Adds the final phrase to the empty variable

    return (finalPhrase)
    # Returns the final phrase instead of printing it, as this is a function


if (encryptOrDecrypt.lower() == "decrypt" and phrase.lower() == "random"):
    print("\nThe target decrypted phrase is: " + targetPhrase.upper())
    phrase = encryptString(targetPhrase)
    # Sets the phrase to the encrypted phrase if the user chose to decrypt a random phrase
    print("\nThe encrypted phrase is:" + phrase)
    # Uses the function to encrypt the target phrase, then prints the encrypted phrase

if (encryptOrDecrypt.lower() == "decrypt"):
    def chiMethod(phrase):
        initialPhraseDict = phrase.split()
        # Splits the encrypted phrase into a list

        finalchiDict = {}
        firstDekeyDict = {}
        finalDekeyDict = {}
        finalPhrase = ""
        n = len(initialPhraseDict)
        o = 0
        # These variables are created to use in the for loops

        while (o <= (n - 1)):
            key = 0
            while key <= 26:
                dekeyedPhrase = ""
                # Creates an empty variable each time the loop runs
                for letter in initialPhraseDict[0]:
                    if (letter.isalpha()):
                        # Checks if the character is a letter
                        dekeyedLetterInt = (alphabetRev[letter.upper()] - key) % 26
                        # Subtracts the key from the letter's corresponding number in the dictionary, then mods it by 26 to make sure it is a number between 1 and 26
                        dekeyedLetter = alphabet[dekeyedLetterInt]
                        # Gets the letter from the alphabet dictionary
                        dekeyedPhrase = dekeyedPhrase + dekeyedLetter
                        # Adds the letter to the dekeyed phrase
                    elif (letter == " "):
                        dekeyedPhrase = dekeyedPhrase + " "
                        # If the character is a whitespace, it will add a space to the dekeyed phrase
                    else:
                        dekeyedPhrase = dekeyedPhrase + letter
                        # If the character is neither a letter nor a whitespace, it will add that to the phrase (as all symbols have been stripped already)

                firstDekeyDict[key] = dekeyedPhrase
                # Adds the dekeyed phrase to the first dekeyed dictionary

                letterCountDict = {}
                # Creates an empty dictionary to store the letter counts

                for t in dekeyedPhrase.lower():
                    if(t.isalpha()):
                        letterCountDict[str(t)] = (dekeyedPhrase.lower()).count(str(t))
                        # For each letter in the dekeyed phrase, this will count how many times it appears and stores that number in a dictionary
                    else:
                        pass

                phraseLength = len(dekeyedPhrase)
                # Gets the total length of the phrase to use in later calculations

                phraseChi = 0
                # Creates a variable to store the total Chi value

                for i in letterCountDict:
                    count = letterCountDict[str(i)]
                    # Gets the count of the letter from the dictionary
                    expectedCount = (chiValues[str(i).upper()]) * phraseLength
                    # Finds the expected count by multiplying the actual count by its relative frequency
                    chi = ((count - expectedCount) * (count - expectedCount)) / expectedCount
                    # Finds the Chi value for that letter
                    phraseChi = phraseChi + chi
                    # Adds this Chi value to the total Chi value of the phrase

                finalDekeyDict[key] = dekeyedPhrase
                # Adds the dekeyed phrase to the final dekeyed phrase dictionary
                finalchiDict[key] = phraseChi
                # Adds the Chi value to the final Chi value dictionary

                key += 1
                # Increases the key by 1 to repeat the process

            nextPhrase = ""
            # Creates an empty variable to store the next phrase

            for word in initialPhraseDict:
                dekeyedPhrase = ""
                # Creates an empty variable each time the loop runs
                for letter in word:
                    if (letter.isalpha()):
                        # Checks if the character is a letter
                        dekeyedLetterInt = (alphabetRev[letter.upper()] - key) % 26
                        # Subtracts the key from the letter's corresponding number in the dictionary, then mods it by 26 to make sure it is a number between 1 and 26
                        dekeyedLetter = alphabet[dekeyedLetterInt]
                        # Gets the letter from the alphabet dictionary
                        dekeyedPhrase = dekeyedPhrase + dekeyedLetter
                        # Adds the letter to the dekeyed phrase
                    elif (letter == " "):
                        dekeyedPhrase = dekeyedPhrase + " "
                        # If the character is a whitespace, it will add a space to the dekeyed phrase
                    else:
                        dekeyedPhrase = dekeyedPhrase + letter
                        # If the character is neither a letter nor a whitespace, it will add that to the phrase (as all symbols have been stripped already)

                nextPhrase = nextPhrase + " " + dekeyedPhrase
                # This entire loop will take the key that was found from calculating the 'c' score, and will apply that shift to the entire phrase

            totalPhraseSplit = nextPhrase.split()
            # Splits the phrase into a list
            finalDekeyDict[o] = totalPhraseSplit[0]
            # Adds the first word of the phrase to the final dekeyed dictionary
            del totalPhraseSplit[0]
            # Deletes the first word of the phrase
            initialPhraseDict = totalPhraseSplit
            # Resets the initial phrase dictionary to the new total phrase dictionary
            phrase = nextPhrase
            # Resets the phrase to the new phrase

            o += 1
            # Increases i by 1 to repeat the process

            minimumChiKey = min(finalchiDict, key=finalchiDict.get)
            # Finds the lowest value in the Chi dictionary, and then gets the key for that value

            finalPhrase = finalPhrase + " " + finalDekeyDict[minimumChiKey]

        return(finalPhrase)

    def wordlistMethod(phrase):
        initialPhraseDict = phrase.split()
        # Splits the encrypted phrase into a list
    
        firstDekeyDict = {}
        finalDekeyDict = {}
        n = len(initialPhraseDict)
        i = 0
        # These variables are created to use in the for loops
    
        while (i <= (n - 1)):
            key = 0
            while key <= 26:
                dekeyedPhrase = ""
                # Creates an empty variable each time the loop runs
                for letter in initialPhraseDict[0]:
                    if (letter.isalpha()):
                        # Checks if the character is a letter
                        dekeyedLetterInt = (alphabetRev[letter.upper()] - key) % 26
                        # Subtracts the key from the letter's corresponding number in the dictionary, then mods it by 26 to make sure it is a number between 1 and 26
                        dekeyedLetter = alphabet[dekeyedLetterInt]
                        # Gets the letter from the alphabet dictionary
                        dekeyedPhrase = dekeyedPhrase + dekeyedLetter
                        # Adds the letter to the dekeyed phrase
                    elif (letter == " "):
                        dekeyedPhrase = dekeyedPhrase + " "
                        # If the character is a whitespace, it will add a space to the dekeyed phrase
                    else:
                        dekeyedPhrase = dekeyedPhrase + letter
                        # If the character is neither a letter nor a whitespace, it will add that to the phrase (as all symbols have been stripped already)
    
                firstDekeyDict[key] = dekeyedPhrase
                # Adds the dekeyed phrase to the first dekeyed dictionary
                key += 1
                # Increases the key by 1 to repeat the process
    
            q = 0
            c = {}
            # These variables are created to use in the below loops. Specifically, the 'c' dictionary is an empty dictionary that will store the count of the number of words in the phrase that do not appear in the wordlist (i.e. are not real words)
            while (q <= 26):
                c[q] = 0
                # Sets the initial count to 0
                countPhrase = firstDekeyDict[q]
                phraseList = countPhrase.split()
                for x in phraseList:
                    if x.lower() in wordlist:
                        pass
                        # If the word is in the wordlist, nothing will happen
                    else:
                        c[q] += 1
                        # Otherwise, if the word is not in the wordlist, the count will increase by 1
                q += 1
                # Increases q by 1 to repeat the process
    
            minimumCScore = min(c, key=c.get)
            # Gets the key of the phrase with the lowest 'c' score (the lowest number of words that do not exist in the wordlist)
    
            nextPhrase = ""
            # Creates an empty variable to store the next phrase
    
            for word in initialPhraseDict:
                dekeyedPhrase = ""
                # Creates an empty variable each time the loop runs
                for letter in word:
                    if (letter.isalpha()):
                        # Checks if the character is a letter
                        dekeyedLetterInt = (alphabetRev[letter.upper()] - minimumCScore) % 26
                        # Subtracts the key from the letter's corresponding number in the dictionary, then mods it by 26 to make sure it is a number between 1 and 26
                        dekeyedLetter = alphabet[dekeyedLetterInt]
                        # Gets the letter from the alphabet dictionary
                        dekeyedPhrase = dekeyedPhrase + dekeyedLetter
                        # Adds the letter to the dekeyed phrase
                    elif (letter == " "):
                        dekeyedPhrase = dekeyedPhrase + " "
                        # If the character is a whitespace, it will add a space to the dekeyed phrase
                    else:
                        dekeyedPhrase = dekeyedPhrase + letter
                        # If the character is neither a letter nor a whitespace, it will add that to the phrase (as all symbols have been stripped already)
    
                nextPhrase = nextPhrase + " " + dekeyedPhrase
                # This entire loop will take the key that was found from calculating the 'c' score, and will apply that shift to the entire phrase
    
            totalPhraseSplit = nextPhrase.split()
            # Splits the phrase into a list
            finalDekeyDict[i] = totalPhraseSplit[0]
            # Adds the first word of the phrase to the final dekeyed dictionary
            del totalPhraseSplit[0]
            # Deletes the first word of the phrase
            initialPhraseDict = totalPhraseSplit
            # Resets the initial phrase dictionary to the new total phrase dictionary
            phrase = nextPhrase
            # Resets the phrase to the new phrase
    
            i += 1
            # Increases i by 1 to repeat the process
    
        p = 0
        finalPhrase = ""
        # Creates an empty variable to store the final phrase
        while (p <= (len(finalDekeyDict) - 1)):
            finalPhrase = finalPhrase + " " + finalDekeyDict[p]
            # Adds each word of the phrase to the final phrase
            p += 1

        return(finalPhrase)

    def compareMethods(wordlistMethod, chiMethod):
        wordlistDict = wordlistMethod.split()
        chiDict = chiMethod.split()
        i = 0
        finalPhrase = ""
        # These variables are created to use in the loops

        while(i<=(len(wordlistDict)-1)):
            if wordlistDict[i] == chiDict[i]:
                finalPhrase = finalPhrase + " " + wordlistDict[i]
                # If the word decrypted using the wordlist method is the same as the word decrypted using the chi method, it will add the word to the final phrase
            else:
                print("\nThere is a mismatch between the two methods used for decryption")
                
                a=1
                indicator = " "
                # These variables are created to use in the loops
                
                while(a<=(len(wordlistDict[i]))):
                    indicator = indicator + "^" 
                    a += 1
                if(finalPhrase == ""):
                    print("\nFor context, this is the decrypted phrase using the wordlist method:" + wordlistMethod + ",")
                    print("this is the decrypted phrase using the chi method:                  " + chiMethod + ",")
                    print("                                                                    " + finalPhrase + indicator)
                    # Prints the existing phrases to give the user more context
                    print("\nOption 1: " + wordlistDict[i])
                    print("Option 2: " + chiDict[i])
                else:
                    print("\nFor context, this is the decrypted phrase using the wordlist method:" + wordlistMethod + ",")
                    print("this is the decrypted phrase using the chi method:                  " + chiMethod + ",")
                    print("and this is the current phrase that you have built:                 " + finalPhrase + indicator)
                    # Prints the existing phrases to give the user more context
                    print("\nOption 1: " + wordlistDict[i])
                    print("Option 2: " + chiDict[i])
                while True:
                    option = input("\nWhich word do you think is the correct one? (1/2). If neither option fits, enter what you think the word should be: ")
                    if option == "1":
                        finalPhrase = finalPhrase + " " + wordlistDict[i]
                        break
                    elif option == "2":
                        finalPhrase = finalPhrase + " " + chiDict[i]
                        break
                    else:
                        finalPhrase = finalPhrase + " " + option
                        break
            i += 1

        return(finalPhrase)
                    

if(encryptOrDecrypt.lower()=="decrypt"):    
    print("\nThe final decrypted phrase is:" + compareMethods(wordlistMethod(phrase), chiMethod(phrase)))
    # If the user chose to decrypt, this will run the compare methods function to compare the decrypted phrases using the wordlist method and the chi method
elif (encryptOrDecrypt.lower() == "encrypt"):
    print("\nThe encrypted phrase is:" + encryptString(phrase))
    # If the user chose to encrypt, this will run the encrypt string function to encrypt the phrase
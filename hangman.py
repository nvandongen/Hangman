def letter():
    if (letter) in (word):
        print ("ja")
    else:
        print("nee")
    
word = input("Please enter your secret word: ")

dashes = "-" * len(word)

print(dashes)

letter = input("Guess a letter: ")

letter()

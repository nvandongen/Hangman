def letter():
    if (getLetter) in (word):
        print ("Ja") 
    else:
        print("Nee")
        
    
word = input("Please enter your secret word: ")

dashes = "-" * len(word)

print(dashes)

getLetter = input("Guess a letter: ")

letter()

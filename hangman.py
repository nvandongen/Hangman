def answerLetterInWord(letter, word):
    if (letter in word):
        return True
    else:
        return False

def displayWrongLetters(wrongLetters):
    display = ""
    for letter in wrongLetters:
        display = display + letter
    print(display)

turns = 10



word = input("Please enter your secret word: ")

dashes = "-" * len(word)

wrongLetters = []
rightLetters = []

gameOver = False

while not gameOver:
    print(dashes)
    displayWrongLetters(wrongLetters)
    letter = input("Guess a letter: ")
##    TODO: Alleen eerste letter van de input lezen.
    if answerLetterInWord(letter, word):
        print("Yes")
        rightLetters.append(letter)
    else:
        if letter in wrongLetters:
            print("Already guessed!")
        else:
            wrongLetters.append(letter)
            turns = turns - 1
    print("Turns left: ", turns)
    if turns == 0:
        gameOver = True
        print("Game over!")
        







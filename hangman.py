def answerLetterInWord(letter, word, dashes):
    if (letter in word):
##        print (dashes.replace("-" , letter))
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
dashes = list("-" * len(word))


wrongLetters = []
rightLetters = []

gameOver = False

while not gameOver:
    print(dashes)
    displayWrongLetters(wrongLetters)
    userInput1 = list(input("Guess a letter: "))
    letter = userInput1[0]
##    TODO: Alleen eerste letter van de input lezen.
    if answerLetterInWord(letter, word, dashes):
        print("Yes")
        rightLetters.append(letter)
##        print (dashList.replace(dashlist, letter))
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
        







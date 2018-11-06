import random
import sys
from graphics import *

def chooseGameWord():
    lines = open('wordList.txt').read().splitlines()
    myline =random.choice(lines)
    return(myline.upper())

def displayPrompt(graphicsWindow):
    prompt = Text(Point(graphicsWindow.getWidth()/2, 535), "Click on a letter from the keyboard to guess.")
    prompt.setFill("white")
    prompt.draw(graphicsWindow)

def displayBadGuesses(graphicsWindow, badGuesses): #Will show bad guesses on screen
    badGuessesDisplay = Text(Point(graphicsWindow.getWidth()/2, 20), "Wrong guesses: " + "".join(badGuesses))
    badGuessesDisplay.draw(graphicsWindow)

def displayWordProgress(graphicsWindow, lettersAndDashes): #Will show letters & dashes on screen
    lettersAndDashesDisplay = Text(Point(graphicsWindow.getWidth()/2, 40), lettersAndDashes)
    lettersAndDashesDisplay.draw(graphicsWindow)

def inputFromScreen(graphicsWindow, won, lost): #Will read input from on-screen keyboard
    click = graphicsWindow.getMouse()

    if click.getY() <= 693 and click.getY() >= 648:
        if click.getX() >= 53 and click.getX() <= 98:
            return("Q")
        elif click.getX() >= 103 and click.getX() <= 148:
            return("W")
        elif click.getX() >= 153 and click.getX() <= 198:
            return("E")
        elif click.getX() >= 203 and click.getX() <= 248:
            return("R")
        elif click.getX() >= 253 and click.getX() <= 298:
            return("T")
        elif click.getX() >= 303 and click.getX() <= 348:
            return("Y")
        elif click.getX() >= 353 and click.getX() <= 398:
            return("U")
        elif click.getX() >= 403 and click.getX() <= 448:
            return("I")
        elif click.getX() >= 453 and click.getX() <= 498:
            return("O")
        elif click.getX() >= 503 and click.getX() <= 548:
            return("P")
        else:
            return("")
    elif click.getY() <= 643 and click.getY() >= 598:
        if click.getX() >= 78 and click.getX() <= 123:
            return("A")
        elif click.getX() >= 128 and click.getX() <= 173:
            return("S")
        elif click.getX() >= 178 and click.getX() <= 223:
            return("D")
        elif click.getX() >= 228 and click.getX() <= 273:
            return("F")
        elif click.getX() >= 278 and click.getX() <= 323:
            return("G")
        elif click.getX() >= 328 and click.getX() <= 373:
            return("H")
        elif click.getX() >= 378 and click.getX() <= 423:
            return("J")
        elif click.getX() >= 428 and click.getX() <= 473:
            return("K")
        elif click.getX() >= 478 and click.getX() <= 523:
            return("L")
        else:
            return("")
    elif click.getY() <= 593 and click.getY() >= 548:
        if click.getX() >= 18 and click.getX() <= 118:
            graphicsWindow.close()
            playGame(won, lost)
        elif click.getX() >= 128 and click.getX() <= 173:
            return("Z")
        elif click.getX() >= 178 and click.getX() <= 223:
            return("X")
        elif click.getX() >= 228 and click.getX() <= 273:
            return("C")
        elif click.getX() >= 278 and click.getX() <= 323:
            return("V")
        elif click.getX() >= 328 and click.getX() <= 373:
            return("B")
        elif click.getX() >= 378 and click.getX() <= 423:
            return("N")
        elif click.getX() >= 428 and click.getX() <= 473:
            return("M")
        elif click.getX() >= 482 and click.getX() <= 585:
            graphicsWindow.close()
            sys.exit()
        else:
            return("")
    else:
        return("")

def checkNewGame(graphicsWindow, won, lost):
    click = graphicsWindow.getMouse()

    if click.getY() <= 593 and click.getY() >= 548:
        if click.getX() >= 18 and click.getX() <= 118:
            graphicsWindow.close()
            playGame(won, lost)
        elif click.getX() >= 482 and click.getX() <= 585:
            graphicsWindow.close()
            sys.exit()
        else:
            checkNewGame(graphicsWindow, won, lost)
    else:
        checkNewGame(graphicsWindow, won, lost)

def displayScore(graphicsWindow, won, lost):
    wonTitle = Text(Point(40, 43), "Games won:")
    wonTitle.draw(graphicsWindow)
    wonNumber = Text(Point(41, 20), won)
    wonNumber.setSize(36)
    wonNumber.draw(graphicsWindow)

    lostTitle = Text(Point(565, 43), "Games lost:")
    lostTitle.draw(graphicsWindow)
    lostNumber = Text(Point(568, 20), lost)
    lostNumber.setSize(36)
    lostNumber.draw(graphicsWindow)

def endGame(graphicsWindow, result):
    if result == "WIN":
        winSequence = Text(Point(graphicsWindow.getWidth()/2, 75), "You win!")
        winSequence.setTextColor("gold")
        winSequence.setSize(36)
        winSequence.draw(graphicsWindow)
    elif result == "LOSE":
        loseSequence = Text(Point(graphicsWindow.getWidth()/2, 75), "You lose.")
        loseSequence.setTextColor("red")
        loseSequence.setSize(36)
        loseSequence.draw(graphicsWindow)

def displayKeyboard(graphicsWindow):
    letterList1 = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"]
    letterList2 = ["A", "S", "D", "F", "G", "H", "J", "K", "L"]
    letterList3 = ["Z", "X", "C", "V", "B", "N", "M"]

    x1 = 53
    for keys in range(10):
        key = Rectangle(Point(x1, 693), Point(x1+45, 648))
        key.setFill("white")
        key.draw(graphicsWindow)
        x1 = x1 + 50
    x2 = 78
    for keys in range(9):
        key = Rectangle(Point(x2, 643), Point(x2+45, 598))
        key.setFill("white")
        key.draw(graphicsWindow)
        x2 = x2 + 50
    x3 = 128
    for keys in range(7):
        key = Rectangle(Point(x3, 593), Point(x3+45, 548))
        key.setFill("white")
        key.draw(graphicsWindow)
        x3 = x3 + 50

    x4 = 75
    for letter in letterList1:
        keyLetter = Text(Point(x4,670), letter)
        keyLetter.draw(graphicsWindow)
        x4 = x4 + 50

    x5 = 100
    for letter in letterList2:
        keyLetter = Text(Point(x5,620), letter)
        keyLetter.draw(graphicsWindow)
        x5 = x5 + 50

    x6 = 150
    for letter in letterList3:
        keyLetter = Text(Point(x6,570), letter)
        keyLetter.draw(graphicsWindow)
        x6 = x6 + 50

def displayButtons(graphicsWindow):
    newGameButton = Rectangle(Point(15, 593), Point(118, 548))
    newGameButton.setFill("green")
    newGameButton.draw(graphicsWindow)
    newGameText = Text(Point(67, 571), "New Game")
    newGameText.setSize(16)
    newGameText.draw(graphicsWindow)

    quitButton = Rectangle(Point(482, 593), Point(585, 548))
    quitButton.setFill("red")
    quitButton.draw(graphicsWindow)
    quitText = Text(Point(534, 571), "Quit")
    quitText.setSize(16)
    quitText.draw(graphicsWindow)

def displayImage(graphicsWindow, numWrongGuesses): #Will display hangman image
    graphicsWindow.autoflush = False
    if numWrongGuesses >= 0:
        sky = Rectangle(Point(0,0), Point(600,700))
        sky.setFill("blue")
        sky.setOutline("blue")
        sky.draw(graphicsWindow)

        ground = Rectangle(Point(0,0), Point(600, 100))
        ground.setFill("green")
        ground.setOutline("green")
        ground.draw(graphicsWindow)

        gallowBase = Rectangle(Point(150,100), Point(450, 115))
        gallowBase.setFill("brown")
        gallowBase.setOutline("brown")
        gallowBase.draw(graphicsWindow)

        gallowUpright = Rectangle(Point(385, 100), Point(400, 500))
        gallowUpright.setFill("brown")
        gallowUpright.setOutline("brown")
        gallowUpright.draw(graphicsWindow)

        gallowTop = Rectangle(Point(225, 500), Point(400, 515))
        gallowTop.setFill("brown")
        gallowTop.setOutline("brown")
        gallowTop.draw(graphicsWindow)

        gallowLowerHinge = Polygon(Point(325, 115), Point(385, 175), Point(385, 115))
        gallowLowerHinge.setFill("brown")
        gallowLowerHinge.setOutline("brown")
        gallowLowerHinge.draw(graphicsWindow)

        gallowLowerGap = Polygon(Point(345, 115), Point(385, 155), Point(385, 115))
        gallowLowerGap.setFill("blue")
        gallowLowerGap.setOutline("blue")
        gallowLowerGap.draw(graphicsWindow)

        gallowUpperHinge = Polygon(Point(325, 500), Point(385, 440), Point(385, 500))
        gallowUpperHinge.setFill("brown")
        gallowUpperHinge.setOutline("brown")
        gallowUpperHinge.draw(graphicsWindow)

        gallowUpperGap = Polygon(Point(345, 500), Point(385, 460), Point(385, 500))
        gallowUpperGap.setFill("blue")
        gallowUpperGap.setOutline("blue")
        gallowUpperGap.draw(graphicsWindow)

        gallowRope = Rectangle(Point(240, 500), Point(243, 450))
        gallowRope.setFill("yellow")
        gallowRope.setOutline("yellow")
        gallowRope.draw(graphicsWindow)

        displayKeyboard(graphicsWindow)

        displayButtons(graphicsWindow)

        if numWrongGuesses >= 1:
            head = Circle(Point(240, 420), 30)
            head.setOutline("black")
            head.draw(graphicsWindow)

            if numWrongGuesses >= 2:
                body = Line(Point(240, 390), Point(240, 250))
                body.setOutline("black")
                body.draw(graphicsWindow)

                if numWrongGuesses >= 3:
                    leftLeg = Line(Point(240, 250), Point(200, 200))
                    leftLeg.setOutline("black")
                    leftLeg.draw(graphicsWindow)

                    if numWrongGuesses >= 4:
                        rightLeg = Line(Point(240, 250), Point(280, 200))
                        rightLeg.setOutline("black")
                        rightLeg.draw(graphicsWindow)

                        if numWrongGuesses >= 5:
                            leftArm = Line(Point(240, 350), Point(200, 300))
                            leftArm.setOutline("black")
                            leftArm.draw(graphicsWindow)

                            if numWrongGuesses >= 6:
                                rightArm = Line(Point(240, 350), Point(280, 300))
                                rightArm.setOutline("black")
                                rightArm.draw(graphicsWindow)

                                if numWrongGuesses >= 7:
                                    leftEyeOne = Line(Point(225, 435), Point(235, 425))
                                    leftEyeOne.setOutline("black")
                                    leftEyeOne.draw(graphicsWindow)
                                    leftEyeTwo = Line(Point(225, 425), Point(235, 435))
                                    leftEyeTwo.setOutline("black")
                                    leftEyeTwo.draw(graphicsWindow)


                                    if numWrongGuesses >= 8:
                                        rightEyeOne = Line(Point(245, 435), Point(255, 425))
                                        rightEyeOne.setOutline("black")
                                        rightEyeOne.draw(graphicsWindow)
                                        rightEyeTwo = Line(Point(245, 425), Point(255, 435))
                                        rightEyeTwo.setOutline("black")
                                        rightEyeTwo.draw(graphicsWindow)

                                        if numWrongGuesses >= 9:
                                            mouth = Circle(Point(240, 410), 5)
                                            mouth.setOutline("black")
                                            mouth.draw(graphicsWindow)
    graphicsWindow.autoflush = True

def playGame(won, lost):
    #Set-up game
    gameWord = chooseGameWord()
    wordInProgress = "_"*len(gameWord)
    lettersInWord = list(gameWord) #lettersInWord is a list containing the letters in gameWord
    guessedLetters = []
    wrongLetters = []
    wrongGuesses = 0

    #Open graphics window
    win = GraphWin("Let's play Hangman!", 600, 700)
    win.yUp()
    displayImage(win, 0)
    displayPrompt(win)
    displayWordProgress(win, "_ "*len(gameWord))
    displayBadGuesses(win, wrongLetters)
    displayScore(win, won, lost)

    #Play game
    while wrongGuesses <= 8 and "_" in wordInProgress :
        guess = inputFromScreen(win, won, lost)

        #Check originality of guess
        for a in range(len(guessedLetters)):
            if guess == guessedLetters[a]:
                guess = ""

        #Check for accuracy of guess
        if gameWord.count(guess) != 0 and guess != "":
            wordInProgress = list(wordInProgress) #wordInProgress becomes a list containing _'s and the filled in letters
            for letter in range(len(lettersInWord)): #letter SHOULD BE an integer
                if lettersInWord[letter] == guess: #if the current index is the guessed letter
                    wordInProgress[letter] = guess #change the _ at that index to the guessed letter
        elif guess != "":
            wrongGuesses = wrongGuesses + 1
            wrongLetters.extend(guess)

        #Add guessed letter to total list of guesses
        guessedLetters.extend(guess)

        #Update word
        displayWord = []
        for index in range(len(wordInProgress)):
            displayWord.extend([wordInProgress[index], " "])
        displayWord = "".join(displayWord)

        #Update display
        displayImage(win, wrongGuesses)
        displayPrompt(win)
        displayWordProgress(win, displayWord)
        displayBadGuesses(win, wrongLetters)
        displayScore(win, won, lost)

    #Print result of game
    if wrongGuesses > 8:
        displayImage(win, wrongGuesses)
        lostWord = Text(Point(win.getWidth()/2, 40), "Sorry, the word was " + gameWord.upper())
        lostWord.draw(win)
        displayBadGuesses(win, wrongLetters)
        displayScore(win, won, lost)
        endGame(win, "LOSE")
        lost += 1
    else:
        displayImage(win, wrongGuesses)
        displayWordProgress(win, displayWord)
        displayBadGuesses(win, wrongLetters)
        displayScore(win, won, lost)
        endGame(win, "WIN")
        won += 1

    checkNewGame(win, won, lost)

def main():
    gamesWon = 0
    gamesLost = 0
    playGame(gamesWon, gamesLost)

main()

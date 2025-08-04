from classes.genericMessages import Messages

class NuGuMessagesClass(Messages):
    @staticmethod
    def guessMessageResult(guessResult:int)->None:
        if guessResult > 0:
            print("Too high!")
            return
        if guessResult < 0:
            print("Too low!")
            return
        
        print("That's right, you got it!")
        return

    @staticmethod
    def finalScore(playerName:str, score:int)->None:
        firstPart = f"Well, so that's it for you, {playerName}..."
        secondPart = f"Your final score was {score} points!"
        if score > 5:
            secondPart = f"Your AWESOME score was {score} points! Congrats!"
        elif score == 0:
            secondPart = f"You didn't score..."

        print(f"{firstPart}\n{secondPart}")
        return 
    
    @staticmethod
    def askForGuess(triesLeft:int, isFirstTry=False)->None:
        firstPart = "Guess Again."
        if isFirstTry:
            firstPart = "So let's begin! Try guessing which number I chose."

        print(f"{firstPart} Tries left: {triesLeft}")
        return

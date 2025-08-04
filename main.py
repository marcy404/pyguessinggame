# Import Classes
from NumberGuess.player import PlayerClass
from NumberGuess.host import HostClass
from NumberGuess.NuGuMessages import NuGuMessagesClass

# Game Banner
print(NuGuMessagesClass.banner("NumberGuess"))

# Create player
mainPlayer = PlayerClass(name=input("Your nickname\n>> "))
print("\n")

# Create Host
gameHost = HostClass()
print(gameHost.number)
# Main Game Loop
isFirstTry = True
while mainPlayer.current_lifes > 0:
    # Asks for guess
    NuGuMessagesClass.askForGuess(mainPlayer.current_lifes, isFirstTry=isFirstTry)
    isFirstTry = False
    playerAnswer = int(input(">> "))

    # Checks boundaries
    if playerAnswer == -1:
        break
    elif playerAnswer < 1 or playerAnswer > 100:
        print("What are you talking about? We all know numbers lower than 1 or higher than 100 don't exist...")
        print("Try again")
        continue

    # Checks answer
    answerResult = gameHost.checkAnswer(playerAnswer)
    
    # Print answer message + change game state based on result
    NuGuMessagesClass.guessMessageResult(answerResult)
    print(NuGuMessagesClass.separator())
    match answerResult:
        case 1:
            mainPlayer.decreaseLife()
            continue
        case -1:
            mainPlayer.decreaseLife()
            continue
        case 0:
            mainPlayer.changeScore(1)
            mainPlayer.resetLifes()
            gameHost.generateNumber()
            print(gameHost.number)
            continue

# Prints final message
NuGuMessagesClass.finalScore(playerName=mainPlayer.name, score=mainPlayer.score)
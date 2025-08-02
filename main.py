# Import Classes
from player import Player
from host import Host

# Welcome print
print("Welcome to the number guessing game!\n")

# Create player
mainPlayer = Player(name=input("Your nickname\n> "))
print("\n")

# Create Host
gameHost = Host()

# Main Game Loop
print("Try to guess the number I chose...")
while mainPlayer.current_lifes > 0:
    print(f"Remaining lifes: {mainPlayer.current_lifes}")
    playerAnswer = int(input("> "))
    if playerAnswer == -1:
        break
    elif playerAnswer < 1 or playerAnswer > 100:
        print("What are you talking about? We all know numbers lower than 1 or higher than 100 don't exist...")
        print("Try again")
        continue


    match gameHost.checkAnswer(playerAnswer):
        case 1:
            print("Too high! Guess again")
            mainPlayer.decreaseLife()
            continue
        case -1:
            print("Too low... guess again!")
            mainPlayer.decreaseLife()
            continue
        case 0:
            print("PERFECT! Congratulations for guessing right! But I just chose another one...")
            mainPlayer.changeScore(1)
            mainPlayer.resetLifes()
            gameHost.generateNumber()
            continue

print("Well, well, well... let's see your results...")
print(f"Final score: {mainPlayer.score}")
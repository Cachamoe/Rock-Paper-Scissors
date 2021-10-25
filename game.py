import random, os, sys
userScore = 0 
computerScore = 0
userInput = ""
computerInput = ""
choice = ""
numGames = int(input("How many games would you like to play?\n"))
userWin = False
draw = False
clear = lambda: os.system("cls")


userInput = input("Choose rock, paper, or sissors\n")

if userInput == "rock" and computerInput == "sissors":
    print("You selected",userInput,"and the computer selected",computerInput,"You won this round!")
    userScore += 1
elif userInput == "rock" and computerInput == "paper":
    print("You selected",userInput,"and the computer selected",computerInput,"You lost this round!")
    computerScore += 1
if userInput == "paper" and computerInput == "rock":
    print("You selected",userInput,"and the computer selected",computerInput,"You won this round!")


for x in range(0, numGames):
    generatedNum = random.randint(1,3)
    if generatedNum == 1:
        computerInput = "rock"
    elif generatedNum == 2:
        computerInput = "paper"
    elif generatedNum == 3:
        computerInput = "sissors"


choice = str(input("Would you like to play again? y/n\n"))
if choice == "y":
    clear()
    os.system("game.py")
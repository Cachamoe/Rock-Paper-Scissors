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


for x in range(0, numGames):
    generatedNum = random.randint(1,3)
    if generatedNum == 1:
        computerInput = "rock"
    elif generatedNum == 2:
        computerInput = "paper"
    elif generatedNum == 3:
        computerInput = "sissors"


userInput = input("Choose rock, paper, or sissors\n")

if userInput == "rock" and computerInput == "sissors":
    print("You selected",userInput,"and the computer selected",computerInput,"You won this round!")
    userScore += 1
elif userInput == "rock" and computerInput == "paper":
    print("You selected",userInput,"and the computer selected",computerInput,"You lost this round!")
    computerScore += 1
if userInput == "paper" and computerInput == "rock":
    print("You selected",userInput,"and the computer selected",computerInput,"You won this round!")
    userScore += 1
elif userInput == "paper" and computerInput == "sissors":
    print("You selected",userInput,"and the computer selected",computerInput,"You lost this round!")
    computerScore += 1
if userInput == "scissors" and computerInput == "paper":
    print("You selected",userInput,"and the computer selected",computerInput,"You won this round!")
    userScore += 1
elif userInput == "scissors" and computerInput == "rock":
    print("You selected",userInput,"and the computer selected",computerInput,"You lost this round!")
    computerScore += 1


if userScore > computerScore:
    userWin = True
elif userScore == computerScore:
    draw = True


if userWin ==  True:
    print("Congratulations, you won!\nYour score:",userScore,"\nComputer's score:",computerScore)
elif userWin == False:
    print("Oh no, you lost!\nYour score:",userScore,"\nComputer's score:",computerScore)
elif draw == True:
    print("You tied!\nYour score:",userScore,"\nComputer's score:",computerScore)


choice = str(input("Would you like to play again? y/n\n"))
if choice == "y":
    clear()
    os.system("game.py")
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







for x in range(0, numGames):
    generatedNum = random.randint(1,3)
    if generatedNum == 1:
        computerInput = "rock"
    elif generatedNum == 2:
        computerInput = "paper"
    elif generatedNum == 3:
        computerInput = "sissors"
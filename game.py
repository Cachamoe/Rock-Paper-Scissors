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

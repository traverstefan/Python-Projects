from random import randint

#Create a list of play options
t = ["Rock", "Paper", "Scissors"]

#Assign a random play to the computer
computer = t[randint(0, 2)]

#Set player to False
player = False

while player == False:
#Set player to True
    player = input("Rock, Paper Scissors?")
    if player == computer:
        print("Its a tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cuts", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose!", computer, "smashes", player)
    else:
        print("Check your spelling and try again!")
    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0,2)]
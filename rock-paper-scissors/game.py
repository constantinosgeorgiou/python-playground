import sys
from random import randint

# Create a list of play options
options = ["Rock", "Paper", "Scissors"]

# Assign a random play to the computer
computer = options[randint(0, 2)]

player = None

while player != "Quit":

    player = input("\nRock, Paper, Scissors, Quit? ")

    if player == computer:
        print("👔 Tie!")

    elif player == "Rock":

        if computer == "Paper":
            print("❌ You lose!", computer, "covers", player)
        else:
            print("🏆 You win!", player, "smashes", computer)

    elif player == "Paper":

        if computer == "Scissors":
            print("❌ You lose!", computer, "cuts", player)
        else:
            print("🏆 You win!", player, "covers", computer)

    elif player == "Scissors":

        if computer == "Rock":
            print("❌ You lose!", computer, "smashes", player)
        else:
            print("🏆 You win!", player, "cuts", computer)

    else:
        if player == "Quit":
            print("Byeeee")
            sys.exit()
        else:
            print("That's not a valid play. Check your spelling!")

    computer = options[randint(0, 2)]

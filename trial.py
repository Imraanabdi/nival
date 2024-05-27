import random

choices = ["rock", "paper", "scissors"]

computer = random.choices(choices)
player = None

while player not in choices:
    player = input("rock, paper, or scissors? ")
if player == computer:
    print("Tie!")
elif player == "rock":
    if computer == "paper":
        print("You lose!", computer, "covers", player)
    else:
        print("You win!", player, "smashes", computer)
elif player == "paper":
    if computer == "scissors":
        print("You lose!", computer, "cuts", player)
    else:
        print("You win!", player, "covers", computer)
elif player == "scissors":
    if computer == "rock":
        print("You lose...", computer, "smashes", player)
    else:
        print("You win!", player, "cut", computer)
print(computer)
print(player)
print("You lost")

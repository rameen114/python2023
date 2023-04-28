import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type rock/paper/sissors or type Q to quit: ").lower()

    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    computer_pick = options[random_number]

    print("computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissor":
        print("You win")
        user_wins += 1
    
    elif user_input == "paper" and computer_pick == "rock":
        print("You win")
        user_wins += 1
    
    elif user_input == "scissor" and computer_pick == "paper":
        print("You win")
        user_wins += 1
    
    else:
        print("You lost")
        computer_wins += 1

print("You won ", user_wins, "times.")
print("Computer won", computer_wins, "times.")

input("Press enter to exit.")
import random


def get_choice():
    player_choice = input("Choose one - rock/paper/scissors: ")
    print("-----------------------------")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choice = {"player": player_choice, "computer": computer_choice}
    return choice


def check_victory(player, computer):
    print(f"Player chose {player}. Computer chose {computer}.")

    if player == computer:
        return "Draw!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smash scissors, VICTORY!"
        else:
            return "Paper cover rock, DEFEAT..."
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cut paper, VICTORY!"
        else:
            return "Rock smash scissors, DEFEAT..."
    elif player == "paper":
        if computer == "rock":
            return "Paper cover rock, VICTORY!"
        else:
            return "Scissors cut paper, DEFEAT..."


choices = get_choice()
result = check_victory(choices["player"], choices["computer"])
print(result)

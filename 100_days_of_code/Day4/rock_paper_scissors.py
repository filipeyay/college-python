import random

rock = """
        _________
    ---'     ____)
            (_____)
            (_____)
            (____)
    -----.__(___)
"""

paper = """
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
"""

scissors = """
        _______
    ---'    ____)____
               ______)
            __________)
            (____)
    ---.___(___)
"""

ascii_hands = [rock, paper, scissors]

player_choice = int(
    input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors: ")
)

if player_choice >= 0 and player_choice <= 2:
    print(ascii_hands[player_choice])

computer_choice = random.randint(0, 2)
print(f"Computer chose {computer_choice}.")
print(ascii_hands[computer_choice])

if player_choice >= 3 or player_choice < 0:
    print("Invalid number.")
elif player_choice == 0 and computer_choice == 2:
    print("You win.")
elif computer_choice == 0 and player_choice == 2:
    print("You lose.")
elif player_choice == 2 and computer_choice == 1:
    print("You win.")
elif computer_choice == 1 and computer_choice == 2:
    print("You lose.")
elif player_choice == 1 and computer_choice == 0:
    print("You win.")
elif computer_choice == 0 and player_choice == 1:
    print("You lose.")
else:
    print("Draw.")

# GAME RULES
# rock wins agains scissors
# scissors win against paper
# paper wins against rock

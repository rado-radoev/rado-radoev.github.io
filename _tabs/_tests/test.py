rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

user_input = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
rps_ascii = [rock, paper, scissors]
rps = ["rock", "paper", "scissors"]

user_selected = int(user_input)
user_choice= rps[user_selected]

computer_select = random.randint(0, len(rps) - 1)
computer_choice = rps[computer_select]

game_over = 0

print(f"User chose: {rps[user_selected]} {rps_ascii[user_selected]}")
print(f"Computer chose: {rps[computer_select]} {rps_ascii[computer_select]}")

if user_choice == computer_choice:
  print("Tie")
  game_over = 1
else:
  # Rock wins against scissors.
  if game_over == 0 and (user_choice == "rock" and computer_choice != "paper"):
    print("You win")
    game_over = 1

  # Scissors win against paper.
  if game_over == 0 and(user_choice == "scissors" and computer_choice != "rock"):
    print("You win")
    game_over = 1


  # Paper wins against rock.
  if game_over == 0 and (user_choice == "paper" and computer_choice != "scissors"):
    print("You win")
    game_over = 1

if game_over == 0:
  print("You lose")


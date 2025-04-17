# ROCK PAPER SCISSOR GAME

import random

# game choices
choices = ["rock", "paper", "scissors"]

# player choices
player_choice = input("Enter rock paper scissors: ").lower()

# computer choices
computer_choice = random.choice(choices)

# winner decision
if player_choice == computer_choice:
    print(f"dono ke choice {player_choice} tha. its a tie!")
elif player_choice == "rock" and computer_choice == "scissors":
    print(f"Player wins! {player_choice} beats {computer_choice}.")
elif player_choice == "paper" and computer_choice == "rock":
    print(f"players wins! {player_choice} beats {computer_choice}.")
elif player_choice == "scissors" and computer_choice == "paper":
    print(f"players wins! {player_choice} beats {computer_choice}.")
else:
    print(f"computers wins! {computer_choice} beats {player_choice}.")
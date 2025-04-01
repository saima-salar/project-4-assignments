import random

# Topic: Project 4 - Rock, Paper, Scissors Game 🪨📄✂️

# Game choices
choices = ["rock", "paper", "scissors"]

# Player choice
player_choice = input("Enter rock 🗿, paper 📄, or scissors ✂️: ").lower()

# Computer choice
computer_choice = random.choice(choices)

# Icons dictionary
icons = {"rock": "🗿", "paper": "📄", "scissors": "✂️"}

# Winner decision
if player_choice not in choices:
    print("Invalid choice! Please enter rock, paper, or scissors.")
elif player_choice == computer_choice:
    print(f"Both chose {icons[player_choice]}. It's a tie!")
elif (player_choice == "rock" and computer_choice == "scissors") or \
     (player_choice == "paper" and computer_choice == "rock") or \
     (player_choice == "scissors" and computer_choice == "paper"):
    print(f"🎉 Player wins! {icons[player_choice]} beats {icons[computer_choice]}.")
else:
    print(f"💻 Computer wins! {icons[computer_choice]} beats {icons[player_choice]}.")




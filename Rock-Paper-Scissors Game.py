# Task 4
import random

# Mapping numbers to emojis for Stone, Paper, and Scissors
choices = {1: "🪨", 2: "📄", 3: "✂️"}

print("Welcome to the game\nLet's play!")

print("1 for 🪨 (Stone)\n2 for 📄 (Paper)\n3 for ✂️ (Scissors)")

# Get user choice
a = int(input("Enter your choice: "))
b = random.randint(1, 3)

# Display the choices made by the user and the computer
print(f"You chose: {choices.get(a, 'Invalid choice')}")
print(f"Computer chose: {choices[b]}")

# Validate user input
if a not in [1, 2, 3]:
    print("You entered an invalid input")
else:
    # Check if it's a draw
    if a == b:
        print("It's a draw! Try again.")
    # Check if user wins
    elif (a == 1 and b == 3) or (a == 2 and b == 1) or (a == 3 and b == 2):
        print("You won!")
    else:
        print("You lose!")

print("Thanks for playing! 😊")

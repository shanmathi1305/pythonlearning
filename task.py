import random

chocolate = ["milkybar", "dairymilk", "perk", "munch"]
selected_chocolate = random.choice(chocolate)

user_guess = input("Guess the chocolate: ")

if selected_chocolate:
    print("Congrats! You guessed it right!")
else:
    print(f"Wrong! do you want to play again {selected_chocolate}.")




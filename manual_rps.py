import random 

def get_computer_choice():
    choices = ["Rock", "Paper", "Scissors"]
    return random.choice(choices)

def get_user_choice():
    choices = ["Rock", "Paper", "Scissors"]
    while True:
        user_choice = input("Enter your choice (Rock/Paper/Scissors): ")
        user_choice = user_choice.capitalize()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid choice. Please choose from Rock, Paper, or Scissors.")
   
def get_winner(computer_choice, user_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors")or (user_choice == "Paper" and computer_choice == "Rock") or (user_choice == "Scissors" and computer_choice == "Paper"):
        return "User wins!"
    else:
        return "Computer wins!"


def play():
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()

    print("Computer's choice:", computer_choice)
    print("User's choice:", user_choice)

    winner = get_winner(computer_choice, user_choice)
    print(winner)

play()




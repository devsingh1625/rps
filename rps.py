import random
again = True
while again == True:
    user_choice = input(
        "Enter your choice (rock,paper, or scissors): ").lower()
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices).lower()
    if user_choice == computer_choice:
        print("It is a tie")
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You Win!")
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You Win!")
    elif user_choice == "paper" and computer_choice == "rock":
        print("You Win!")
    elif computer_choice == "rock" and user_choice == "scissors":
        print("You lose!")
    elif computer_choice == "scissors" and user_choice == "paper":
        print("You lose!")
    elif computer_choice == "paper" and user_choice == "rock":
        print("You lose!")
    play_again = input("Would you like to play again? (Yes or No) ").lower()
    if play_again == "yes":
        again = True
    elif play_again == "no":
        break

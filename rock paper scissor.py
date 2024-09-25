import random

def game():
    print("The game starts -----")
    user_score = 0
    computer_score = 0
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Quit")
    while True: 
        user_choice = input("\n\nEnter your choice (1/2/3/4): ")

        if user_choice == "4":
            print(f"\nFinal Score - You: {user_score}, Computer: {computer_score}")
            break

        if user_choice not in ["1", "2", "3"]:
            print("Invalid choice. Please enter 1, 2, or 3.")
            continue
        choices = ["rock", "paper", "scissors"]
        
        computer_choice = random.choice(choices)

        print(f"\nYou chose: {choices[int(user_choice) - 1]}")
        print(f"Computer chose: {computer_choice}")
        
        # When the user choose ROCK
        if user_choice == "1":
            if computer_choice == "scissors":
                print("Rock smashes scissors! You win!")
                user_score += 1
            elif computer_choice == "paper":
                print("Paper covers rock! You lose.")
                computer_score += 1
            else:
                print("It's a tie!")
        # When the user choose PAPER
        elif user_choice == "2":
            if computer_choice == "rock":
                print("Paper covers rock! You win!")
                user_score += 1
            elif computer_choice == "scissors":
                print("Scissors cuts paper! You lose.")
                computer_score += 1
            else:
                print("It's a tie!")
        # When the user choose SCISSORS
        elif user_choice == "3":
            if computer_choice == "paper":
                print("Scissors cuts paper! You win!")
                user_score += 1
            elif computer_choice == "rock":
                print("Rock smashes scissors! You lose.")
                computer_score += 1
            else:
                print("It's a tie!")

        print(f"Score - You: {user_score}, Computer: {computer_score}")
game()
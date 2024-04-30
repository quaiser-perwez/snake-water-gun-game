import random

print("Welcome Snake Water Gun Game")

def user_ch():
    comp_choice = random.choice(['snake', 'water', 'gun'])
    user_choice = input("Enter Your Choice ('snake', 'water', 'gun'): ")
    if user_choice in ['snake', 'water', 'gun']:
        return user_choice, comp_choice
    else:
        return "Invalid Choice"

def res(user_choice, comp_choice):
    print(f"Your Choice is {user_choice}")
    print(f"Computer Choice is {comp_choice}")
    if comp_choice == user_choice:
        print("It's a Tie")
    elif comp_choice == 'gun' and user_choice == 'water':
        print("You Win! Computer Lost.")
    elif comp_choice == 'gun' and user_choice == 'snake':
        print("Computer Win! You Lost.")
    elif comp_choice == 'water' and user_choice == 'gun':
        print("Computer Win! You Lost.")
    elif comp_choice == 'water' and user_choice == 'snake':
        print("You Win! Computer Lost.")
    elif comp_choice == 'snake' and user_choice == 'gun':
        print("You Win! Computer Lost.")
    elif comp_choice == 'snake' and user_choice == 'water':
        print("Computer Win! You Lost.")

def game():
    while True:
        user_choice, comp_choice = user_ch()
        res(user_choice, comp_choice)
        play_again = input("Play again? Press 'Yes' to continue, or 'No' to exit: ")
        if play_again.lower() != 'yes':
            break

game()

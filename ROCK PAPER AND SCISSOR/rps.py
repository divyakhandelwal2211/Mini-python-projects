import random

# options in game
choices = ["rock", "paper", "scissor"]


# funtion for taking player's choice
def get_player_choice():
    while True:
        player_input = input(
            "Choose rock,paper,scissor or ('quit' to stop the game): "
        ).lower()
        if player_input == "quit":
            return None
        elif player_input in choices:
            return player_input
        else:
            print("Invalid input!")


# funtion for computer's choice
def get_computer_choice():
    return random.choice(choices)


# function for determining winner
def determine_result(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (
        (player_choice == "rock" and computer_choice == "scissors")
        or (player_choice == "scissors" and computer_choice == "paper")
        or (player_choice == "paper" and computer_choice == "rock")
    ):
        return "You wins!"
    else:
        return "Computer wins!"


# main game funtion
def start_game():
    while True:
        player_choice = get_player_choice()
        if player_choice is None:
            print("Thanks for playing!")
            break
        computer_choice = get_computer_choice()
        # diplay both choices
        print(f"Your choice = {player_choice}")
        print(f"Computer choice = {computer_choice}")

        # display result
        result = determine_result(player_choice, computer_choice)
        print(result)
        print("-" * 30)


# start the game
start_game()

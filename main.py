import random


def get_user_choice(options: list[str]) -> str:
    """Simple loop to get the user input or ask again if invalid response"""
    while True:
        user_choice = input("Choose between 'rock', 'paper' or 'scissors': ")

        if user_choice in options:
            return user_choice
        else:
            print("Invalid input, try again!")


def eval_res(user_index: int, random_index: int) -> None:
    """Evaluates and prints result based on the indexes of the choices"""
    results = ["The game is a tie!", "You win!", "You lose!"]
    res = (user_index - random_index) % 3

    print(results[res])


def main() -> None:
    """Main function with actual loop for game"""
    options = ["rock", "paper", "scissors"]

    while True:
        user_choice = get_user_choice(options)
        random_choice = random.choice(options)

        eval_res(options.index(user_choice), options.index(random_choice))

        print(f"Your choice: {user_choice}\nenemy choice: {random_choice}")

        again = input("Again? y or n: ")

        if again == "n":
            print("bye")
            break
        elif again == "y":
            pass
        else:
            print("invalid answer")


if __name__ == "__main__":
    main()

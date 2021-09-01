import random


def main():
    options = {"rock": 0, "paper": 1, "scissors": 2}

    while True:
        user_choice = input("Choose between `rock`, `paper` or `scissors`: ")
        if user_choice not in options:
            print("Invalid input, try again!")
        else:
            break

    random_choice = random.choice(list(options.keys()))

    result = (options.get(user_choice) - options.get(random_choice)) % 3
    if result == 0:
        print("The game is a tie!")
    elif result == 1:
        print("You win!")
    elif result == 2:
        print("You lose!")

    print(f"Your choice: {user_choice} \n"
          f"enemy choice: {random_choice}")

    while True:
        again = input("Again? y or n: ")
        if again == "y":
            main()
        elif again == "n":
            print("bye")
            break
        else:
            print("invalid answer")


if __name__ == "__main__":
    main()

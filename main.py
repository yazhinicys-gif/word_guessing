
import random
import string
from collections import Counter


def number_guessing_game():
    print("\n--- Number Guessing Game ---")
    print("Guess a number between 1 and 100!")

    secret_number = random.randint(1, 100)
    attempts = 0
    score = 100

    while True:
        try:
            guess = int(input("Enter your guess: "))

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                score = max(10, 100 - (attempts - 1) * 10)
                print("\nCorrect! You won!")
                print("Attempts:", attempts)
                print("Your score:", score)
                break

        except ValueError:
            print("Invalid input! Please enter a number.")


def word_counter():
    print("\n--- File-Based Word Counter ---")
    filename = input("Enter the text filename (example: sample.txt): ")

    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()

        # Remove punctuation and convert to lowercase
        words = [
            word.strip(string.punctuation).lower()
            for word in text.split()
        ]
        words = [word for word in words if word]

        frequency = Counter(words)

        print("\nTotal words:", len(words))
        print("Unique words:", len(frequency))
        print("\nWord Frequency:")

        for word, count in frequency.most_common():
            print(f"{word}: {count}")

    except FileNotFoundError:
        print("File not found! Please check the filename.")
    except OSError as error:
        print("Unable to read the file:", error)


while True:
    print("\n===== MAIN MENU =====")
    print("1. Number Guessing Game")
    print("2. Word Counter")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        number_guessing_game()
    elif choice == "2":
        word_counter()
    elif choice == "3":
        print("Thank you for using the program!")
        break
    else:
        print("Invalid choice! Please select 1, 2, or 3.")

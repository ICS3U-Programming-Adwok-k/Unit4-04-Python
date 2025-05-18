#!/usr/bin/env python3
# Created by: Adowk Adiebo
# Created on: May 7th, 2025
# This program asks the user to enter a number within the
# given range and checks if the guessed number is correct

import random


def main():
    # Generate a random number between 0 and 9
    random_number = random.randint(0, 9)

    while True:
        # Ask the user to input a number
        user_number = input("Enter a number between (0-9): ")

        try:
            # Convert user input to integer
            user_num = int(user_number)

            # Check if number is within valid range
            if user_num < 0 or user_num > 9:
                print("Please enter a number within the given range.")

            # Check if the guessed number is incorrect
            elif user_num != random_number:
                print("Try again")

            # If the guess is correct, exit the loop
            else:
                print("You got it right.")
                break

        except ValueError:
            # Handle the case where input is not a valid integer
            print("Please enter a valid number")

    # Thank the user after the loop ends
    print("Thank you for participating")


if __name__ == "__main__":
    main()

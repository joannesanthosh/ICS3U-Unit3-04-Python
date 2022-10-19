#!/usr/bin/env python3

# Created by: Joanne Santhosh
# Created on: Oct 2022
# This program gets the user to guess a number correctly or incorrectly

import math


def main():
    # this function checks if the number input is positive or negative

    # input
    user_input = int(input("Enter an integer (positive or negative): "))
    print("")

    # process
    if user_input > 0:
        print("The number {0} is positive.".format(user_input))
    elif user_input < 0:
        print("The number {0} is negative.".format(user_input))
    elif user_input == 0:
        print("The number 0 is just 0.")
    else:
        print("No idea!")

        print("\nDone.")


if __name__ == "__main__":
    main()

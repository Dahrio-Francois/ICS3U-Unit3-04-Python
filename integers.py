#!/usr/bin/env python 3
#
# Created by: Dahrio Francois
# Created on: December 2020
# this program identifies if the number is a positive or negative
#     with user input

integer = 0


def main():
    # this function identifies a positive or negative number

    # input
    number = int(input("Enter your number value: "))
    print("")

    # process
    if number == integer:
        print(" 0 ")

    elif number < integer:
        print(" - ")

    elif number > integer:
        print(" + ")


if __name__ == "__main__":
    main()

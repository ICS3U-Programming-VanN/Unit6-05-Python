#!/usr/bin/env python3

# Created by: Van Nguyen
# Created on: December 27, 2022
# This program asks the user to enters marks
# to then calculate and display the averages of the marks
# to the user


# This function calculates the average of a list of marks
def calc_average(list_of_marks):
    # Initializes sum variable
    sum = 0

    # Loops for the number of marks
    for counter in range(len(list_of_marks)):
        # Adds each mark to sum variable
        sum += list_of_marks[counter]

    # Calculates the average
    average = sum / len(list_of_marks)

    # Returns the average
    return average


def main():
    # Displays what the program does
    print("This program calculates the average of all the marks entered.")

    # Initializes list
    user_marks = []

    # Initializes user mark variable
    user_mark = 0

    # Checks for exceptions
    try:
        # Asks user for their mark until they input -1 to stop
        while user_mark != -1:
            # Asks user to input a mark
            user_mark = float(input("Enter a mark (input -1 to stop): "))

            # Checks if user wants to stop entering marks
            if user_mark == -1:
                # Exits loop
                break

            # Checks if user entered a mark outside the range
            elif user_mark < -1 or user_mark > 100:
                print("Invalid Mark! Try again.")
            else:
                # Asks the entered mark to a list
                user_marks.append(user_mark)

    # In the event of an exception
    except Exception:
        print("You must enter a valid mark!")
    else:
        # IF the user did not enter any marks
        if user_marks == []:
            print("You did not enter any marks! Run the program again.")
        else:
            # Calls function to find the average of all the marks
            marks_average = calc_average(user_marks)

            # Displays the list of marks
            print(f"The list of marks is {user_marks}")

            # Displays the average of the marks
            print(f"The average is {marks_average}%")


if __name__ == "__main__":
    main()

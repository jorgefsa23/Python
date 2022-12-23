# dice_1to5.py
# This DICE project is a modified version of the tutorial in realpython.com (https://realpython.com/python-dice-roll/#demo)

"""Return values from DICE (1 to 5 dice each time) and total points made.

    Player must choose option between 1 to 5 dice to pay.
    Program gives the value and the total of points
    At the end, player has the option to play again or exit.
    """
import random

def parse_input(input_string):
    """Return `input_string` as an integer between 1 and 5.

    Check if `input_string` is an integer number between 1 and 5.
    If so, return an integer with the same value. Otherwise, tell
    the user to enter a valid number and quit the program.
    """
    if input_string.strip() in {"1", "2", "3", "4", "5"}:
        return int(input_string)
    else:
        print("Please enter a number from 1 to 5. (Or a different value to exit)")
        raise SystemExit(1)


def roll_dice(num_dice):
    """Return a list of integers with length `num_dice`.

    Each integer in the returned list is a random number between
    1 and 6, inclusive (normal Dice values).
    """
    roll_results = []
    for _ in range(num_dice):
        roll = random.randint(1, 6)
        roll_results.append(roll)
    return roll_results

# ~~~ App's main code block ~~~
print("Welcome to the DICE game!\nFirst, you must choose the number of dices to play")

option = 1
# while option==1, there is a command to play 
while option == 1:
    points, i = 0, 0
    # 1. Get and validate user's input
    num_dice_input = input("How many dice do you want to roll? [1-5]: ")
    num_dice = parse_input(num_dice_input)
    # 2. Roll the dice
    roll_results = roll_dice(num_dice)
    # 3. Print results of each dice
    for dice in roll_results:
        i=i+1
        points = points + dice
        print(f"Dice {i}: {dice}")
    print(f"This made a total of: {points} points")
    # 4. Ask to play again
    option = int(input("\nPlay again...? \n1-yes / 2-no : "))
    if option != 1:
        print("Thanks for playing!!!")
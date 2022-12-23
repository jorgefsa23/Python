"""Return values from a simple DICE play.

    Player must choose to play the dice.
    Program gives the value for a normal dice (6 faces)
    At the end, player has the option to play again or exit.
    """
import random

play_number = 0

def dice(number):
    """Return the value {result} after playing the dice.

    Return a random integer from 1 to 6 (normal Dice values).
    """
    if number ==1:
        result = random.randint(1, 6)
    return result

# ~~~ App's main code block ~~~
print("Welcome to the Dice game!")

option = int(input("Play dice? \n1-yes / 2-no :"))
# while option==1, there is a command to play:
while option == 1:
    play_number = play_number + 1
    diceNumber  = dice(option)
    print(f'The result of the Dice number {play_number} is: {diceNumber}')
    option = int(input("Play AGAIN the dice? \n1-yes / 2-no :"))

if option != 1:
    print("Thanks for playing!!!")




import random

def newGame():
    while True:
        bet = input("What number will the dice roll?\nYou can also bet higher or lower by using < or > (lower than x or higher than x) ")
        wager = input("What amount of money would you like to wager? ")
        wager = int(wager)

        diceRoll = random.randint(1, 6)

        print(f"The dice rolled: {diceRoll}")
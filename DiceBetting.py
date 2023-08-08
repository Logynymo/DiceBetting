import random
import math

newGame = False

def main(newGame):
    while newGame == False():
        bet = input("What number will the dice roll?\nYou can also bet higher or lower by using < or > (lower than x or higher than x) ")
        wager = input("What amount of money would you like to wager? ")
        wager = int(wager)

import random

accountMoney = 100.0

def newGame():
    while True:
        bet = input("What number will the dice roll?\nYou can also bet higher or lower by using < or > (lower than x or higher than x) ")
        wager = input("What amount of money would you like to wager? ")
        wager = int(wager)

        diceRoll = random.randint(1, 6)

        print(f"The dice rolled: {diceRoll}")

        if bet.isdigit():
            bet = int(bet)
            if bet == diceRoll:
                winnings = wager * 5  # Payout for exact match
            else:
                winnings = -wager    # Loss if the bet is wrong

        elif bet.startswith('<'):
            target = int(bet[1:])
            if diceRoll < target:
                winnings = wager * 2  # Payout for correct lower bet
            else:
                winnings = -wager     # Loss if the bet is wrong

        elif bet.startswith('>'):
            target = int(bet[1:])
            if diceRoll > target:
                winnings = wager * 2  # Payout for correct higher bet
            else:
                winnings = -wager     # Loss if the bet is wrong

        else:
            print("Invalid bet or bet format. Please try again.")
            continue

        if winnings > 0:
            print(f"Congratulations! You won ${winnings}")
        else:
            print(f"Sorry, you lost ${abs(winnings)}")

# Call the newGame function to start the game
newGame()




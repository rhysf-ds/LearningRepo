import random

fromrange = int(input("Lowest Number: "))
torange = int(input("Highest Number: "))

def numbersgame(fromrange, torange):
    startmin = fromrange
    startmax = torange
    startlist = list(range(startmin, startmax, 2))
    guess = ""
    response = ""
    highlow = ""
    while response != "yes":
        if min(startlist) == guess:
            response = "yes"
            guess = guess +1
        elif highlow.lower() == "lower":
            startlist = startlist[:int(len(startlist)/2)]
            guess = startlist[int(len(startlist)/2)]
            print(guess)
            response = input("Is this your number?: ")
            if response == "yes":
                break
            else:
                highlow = input("Is your number higher or lower?: ")
        elif highlow.lower() == "higher":
            startlist = startlist[int(len(startlist) / 2):]
            guess = startlist[int(len(startlist) / 2)]
            print(guess)
            response = input("Is this your number?: ")
            if response == "yes":
                break
            else:
                highlow = input("Is your number higher or lower?: ")
        else:
            guess = startlist[int(len(startlist)/2)]
            print(guess)
            response = input("Is this your number?: ")
            if response == "yes":
                break
            else:
                highlow = input("Is your number higher or lower?: ")
    print(guess, "was your number!")

numbersgame(fromrange, torange)
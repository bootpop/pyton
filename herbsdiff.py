import random 

base = [random.randint(0, 10) for i in range(10)]
poison = [i for i, e in enumerate(base, 1) if e == 5]
safe = [i for i, e in enumerate(base, 1) if e not in poison]
guesses = []
poisoncount = len(poison)

def difficulty(diff):
    if diff.lower() == "easy":
        print("You're playing a game, and the main way you heal is with herbs. However, there's a catch.\n\
Every herb has a 1 in 10 chance to contain a lethal poison.\n\
Your goal is to heal as much health as possible without being poisoned.\n")
        text()
        guess(int(input("Choose a number between 1 - 10.\n")))
    elif diff.lower() == "hard":
        print("You're playing a game, and the main way you heal is with herbs. However, there's a catch.\n\
Every herb has a 1 in 10 chance to contain a lethal poison.\n\
Your goal is to heal as much health as possible without being poisoned.\n")
        guess(int(input("Choose a number between 1 - 10.\n")))
    else:
        difficulty(input("That input is invalid! Please select your difficulty.\n\
Easy | Hard\n"))


def text():
    if poisoncount == 1:
        print(f'There is {poisoncount} poisonous herb. Choose carefully.')
    elif 10 > poisoncount > 1:
        print(f'There are {poisoncount} poisonous herbs. Choose carefully.')
    elif poisoncount == 0:
        print(f'Congrats. None of the herbs are poisonous. You win by default.')
        exit()
    elif poisoncount == 10:
        print(f'All of the herbs are poisonous, so you lose by default. Too bad!')
        exit()

def guess(gwess):
    if gwess <= 0 or gwess > 10:
        guess(int(input("That guess is invalid! Please try again!\n")))
    if gwess in guesses:
        guess(int(input("You have already consumed that herb. Please try another value!\n")))
    if gwess in poison:
        print("That herb was poisonous. You died. Too bad!")
        exit()
    else:
        guesses.append(gwess)
        safe.remove(gwess)
        if len(safe) == 0:
            print(f'Congratulations! You avoided the poisonous herb(s) at {poison}. You leave, alive and satisfied.')
        else:
            choice(input("That herb was safe. Would you like to keep trying or are you done? Please type your answer.\n\
Keep Trying | Done\n"))

def choice(yes):
    if yes.lower() == "keep trying":
        guess(int(input("Choose a number between 1 - 10.\n")))
    elif yes.lower() == "done":
        print(f"Ok. You avoided the poisonous herb(s) at {poison}. You leave, alive but unsatisfied...")
        exit()
    else:
        choice(input("Invalid input! Please retype your answer!\nKeep Trying | Exit\n"))


difficulty(input("Select your difficulty. Easy mode tells you the number of herbs that contain poison. Hard mode leaves you to fend for yourself.\n\
Easy | Hard\n"))
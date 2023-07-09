import random
volume = random.randrange(0, 500, 10) #Chooses random number from 0 to 500 in intervals of 10
bub = volume 
turn = 0
def glassowater(guess, p = 0, cpu = 0):
    global bub 
    global turn
    low = guess.lower() #makes the guess lowercase for simplification of code
    if low == "small":
        gwess = 10
    elif low == "medium":
        gwess = 50
    elif low == "large":
        gwess = 100
    else:
        glassowater(input(("Invalid input! Please try again!\n")))
    bub -= gwess #the current volume - guess (e.g. 500 = 50)
    if gwess > volume or bub < 0: #if the original guess is already greater, you lose. or if the volume is less than the guess, you lose
        if p == 1:
            print("The water has spilled and a mess has been made. You have been shot dead as a result.")
            exit()
        elif cpu == 1:
            print("The water has spilled and a mess has been made. The CPU has been shot dead as a result. You are free to go.")
            exit()
    elif gwess == volume or bub == volume: 
        print("Congratulations! You and the CPU managed to fill the glass perfectly without any spill! You are both free to go.")
        exit()
    elif gwess < volume or bub > 0: #there is still room for more water (e.g. 100 < 500 and 450 > 0)
        cpu = 0
        p = 0
        turn += 1
        if turn%2 != 0:
            complayer("start")
        elif turn%2 == 0:
            glassowater(input("Choose a cup to fill the glass with:\n\
Small Medium Large\n"), p = 1)

def complayer(initiate):
    if initiate == "start":
        com = random.randint(0, 2)
        if com == 0:
            print("small")
            glassowater("small", cpu = 1)
        elif com == 1:
            print("medium")            
            glassowater("medium", cpu = 1)
        elif com == 2:
            print("large")
            glassowater("large", cpu = 1)

print("You have been kidnapped and forced to play a death game.\n\
You are presented with an empty glass of water. The volume of the glass is unknown to you.\n\
Your goal is to fill the glass with water using the small, medium or large cups (1, 10, and 50 mL, respectively) each turn.\n\
After your turn, the CPU will take its turn.\n\
Whoever overflows the glass will lose the game.")
glassowater(input("Choose a cup to fill the glass with:\n\
Small Medium Large\n"), p = 1)
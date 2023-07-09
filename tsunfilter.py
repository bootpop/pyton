import random

def Tsun(texty):
    splitty = texty.split()                    #this takes the input and splits the words
    end = []                                   #easier to make a new list than to reuse the existing one
    for e in splitty:            
        randy = random.randint(0, 1)
        randy2 = random.randint(0, 10)         
        if randy == 1:                         #if the random number is 1
            lettersplit = [*e]                 #then split it into individual letters 
            first = lettersplit[0]             #this takes the first letter
            dashie = (f'-{first}')             #and adds a dash in front of it (e.g. -y)
            if first.isupper() == True:        #checks to see if the letter is upppercase. if true, itll make it lowrcase 
                end.append(e[:1] + dashie.lower() + e[1:])
            else:
                end.append(e[:1] + dashie + e[1:])
        elif randy == 0:                       #if the random number is 0, itll skip that word
            end.append(e)
            continue
    print(" ".join(end))
    

Tsun("It's not like I like you or anything, baka!")
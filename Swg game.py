import random
# SNAKE WATER GUN GAME
i = 1
ys = 0
cs = 0
print("READ THE RULES BEFORE STARTING")
print("1.YOU GET ONLY 10 TURNS")
print("IF YOUR CHOICE AND THAT OF OPPONENT ARE SAME THAN NO POINT WILL BE GAINED OR LOSE AND CHANCES WILL NOT GET LESS")
print("LET'S START:")
while i < 11:
    print("CHOOSE: SNAKE, WATER, GUN:")
    CHOICE = input().upper()
    OMG = ["SNAKE", "WATER", "GUN"]
    COMP = random.choice(OMG)
    print(COMP)
    if (CHOICE == "SNAKE" and COMP == "SNAKE") or (CHOICE == "WATER" and COMP == "WATER") or (CHOICE == "GUN" and COMP
                                                                                              == "GUN"):
        print("TIE")
        print("TRY AGAIN")
        continue
    elif CHOICE == "SNAKE" and COMP == "WATER":
        ys = ys + 1
        print("you won this time")
        print("YOUR SCORE IS", ys)
        print("COMPUTER SCORE IS", cs)
        i = i+1
        continue
    elif CHOICE == "WATER" and COMP == "SNAKE":
        cs = cs + 1
        print("you lose this time")
        print("YOUR SCORE IS", ys)
        print("COMPUTER SCORE IS", cs)
        i = i + 1
        continue
    elif CHOICE == "SNAKE" and COMP == "GUN":
        cs = cs + 1
        print("you lose this time")
        print("YOUR SCORE IS", ys)
        print("COMPUTER SCORE IS", cs)
        i = i + 1
        continue
    elif CHOICE == "GUN" and COMP == "SNAKE":
        ys = ys + 1
        print("you lose this time")
        print("YOUR SCORE IS", ys)
        print("COMPUTER SCORE IS", cs)
        i = i + 1
        continue
    elif CHOICE == "GUN" and COMP == "WATER":
        cs = cs + 1
        print("you lose this time")
        print("YOUR SCORE IS", ys)
        print("COMPUTER SCORE IS", cs)
        i = i + 1
        continue
    elif CHOICE == "WATER" and COMP == "GUN":
        ys = ys + 1
        print("you lose this time")
        print("YOUR SCORE IS", ys)
        print("COMPUTER SCORE IS", cs)
        i = i + 1
        continue
    else:
        print("i think you made a wrong entry \n please try again")

print("YOUR GRAND SCORE IS", ys)
print("COMPUTER GRAND SCORE IS", cs)
if ys < cs:
    print("you lose")
else:
    print("you won")
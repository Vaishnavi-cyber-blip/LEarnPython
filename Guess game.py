# MAKING OF GUESS GAME
var1 = 18
i = 1
print(" game starts : READ THE KEY RULE BELOW ")
print("You will get only 9 chances to guess the correct number")
print("The number that is to be gussed lies between 0-100")
while i <= 9:
    guess = int(input("your numeric guess:"))
    if guess == var1:
        print("CONGRATS!YOU WON.")
        print("NUMBER OF TRIALS YOU TOOK", i)
        print("GAME OVER")
        break
    elif 18 < guess <= 30:
        print("QUIET NEAR")
        print("CLUE: HERE LESS IS MORE")
        print("number of guess left", 9 - i)
        i = i + 1
        continue
    elif 30 <= guess <= 100:
        print("CLUE : YOU ARE FAR FROM ORIGINAL")
        print("number of guess left", 9 - i)
        i = i + 1
        continue
    elif 0 <= guess <= 17:
        print("CLUE:QUIET CLOSE")
        print("number of guess left", 9 - i)
        i = i + 1
        continue
    else:
        print("WARNING: ENTER THE VALUE BETWEEN 0-100!")

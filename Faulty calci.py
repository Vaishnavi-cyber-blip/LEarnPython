# FAULTY CALCULATOR
x = int(input("Enter the first number:"))
opr = input("choose any one: '*','/' or ,'+':")
y = int(input("Enter another number:"))
if opr == "*":
    if x == 45 and y == 3:
        print("solution", 555)
    else:
        print("solution:", x * y)
elif opr == "+":

    if x == 56 and y == 9:
        print("solution:", 77)
    else:
        print("solution:", x + y)
elif opr == "-":
    print("solution:", x - y)
elif opr == "/":
    if x == 56 and y == 6:
        print("solution:", 4)
    else:
        print("solution:", x / y)
else:
    print("INVALID EXPRESSION")

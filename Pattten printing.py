print("Choose between: true or false")
st = input()
n = int(input("enter the no. of you want"))
if st == "true":
    for i in range(0, n):
        for j in range(0, i+1):
            print("* ", end="" )

        print("\r")       #carriage return function
elif st == "false":
    for i in range(0, n):
        print("*"*(n-i))   # going to new line by default








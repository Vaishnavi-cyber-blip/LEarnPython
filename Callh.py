import datetime
name = input("ENTER THE NAME:").upper()
DorE = input("MAKE A CHOICE: DIET OR EXERCISE:").upper()
f = open("DIETH.TXT", "rt")
for line in f:
    if name == "HARRY" and DorE == "DIET":
        print("CHOOSE: MORNING ; AFTERNOON ; OR DINNER TIME")
        choice = input().upper()
        if choice == "MORNING":
            print(datetime.time(8))
            content = f.readline(20)
            print(content)

        elif choice == "AFTERNOON":
            print(datetime.time(3))
            content = next(line)
            print(content)
        else:
            content = next(line)
            print(content)

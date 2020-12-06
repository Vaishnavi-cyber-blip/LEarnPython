with open("DIETH.TXT" , "w") as f:
    f.write("Hello World Python Program")

with open("DIETH.TXT", 'w+') as f:
    f.write("Hello")
    f.seek(0)
    data = f.readlines()
    for line in data:
        words = line.split()
        print(words)

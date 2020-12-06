def cour(name):
    print("Searching", name)

    while True:
        see = (yield)
        if name in see:
            print("Cool! Your name is here")
        else:
            print("Oops! Your name is not here")


f = open("EXV.TXT", 'rt')
search = cour('tj')
next(search)
search.send(f.read())

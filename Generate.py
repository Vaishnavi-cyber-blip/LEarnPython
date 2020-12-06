def fibbo(n):
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(n):
        c = a+b
        yield c
        a = b
        b = c


# x = fibbo(5)
# print(x)
for item in fibbo(15):
    print(item)

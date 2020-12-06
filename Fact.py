def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
        yield fact


# g = factorial(5)
# print()
for item in factorial(5):
    print(item)

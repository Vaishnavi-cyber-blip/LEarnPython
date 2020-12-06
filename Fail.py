import timeit

begin = timeit.default_timer()


class Dad:
    basketball = 6


class Son(Dad):
    dance = 1
    basketball = 9

    def is_dance(self):
        return f"i can dance {self.dance} times"


class Grandson(Son):
    dance = 6
    guitar = 1

    def is_dance(self):
        return f"i will date {self.dance} no. of times"


darry = Dad()
larry = Son()
harry = Grandson()
print(harry.basketball)
print(harry.is_dance())
print(larry.is_dance())
stop = timeit.default_timer()
execute = stop - begin
print(execute)

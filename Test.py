'''try:
    list = 5*[0]+5*[10]
    x = list[9]
    print("done")
except IndexError:
    print("nw")
else:
    print("gn")
finally:
    print("cv")'''


'''def a(b):
    b = b+[5]


c = [1, 2, 3, 4]
a(c)
print(len(c))'''


'''names1 = ['Amir', 'Bala', 'Charlie']
names2 = [name.lower() for name in names1]


print(names2[2][0])'''


'''def func(x, ans):
    if x == 0:
        return 0
    else:
        return func(x-1, x+ans)


print(func(2, 0))'''

#s1 = {1,2,3}
#s1.issubset(s1)

'''class
    def __init__(self, x = 1):
        self.x = x
class der(A):
    def __init__(self,y = 2):
        super().__init__()
        self.y = y
def main():
    obj = der()
    print(obj.x,obj.y)
main()'''


'''a,b = 6, 7
a,b = b, a
a,b'''

total = {}
def insert(items):
    if items in total:
        total[items]+=1
    else:
        total[items]=1


insert('Apple')
insert('Ball')
insert('Apple')
print(len(total))




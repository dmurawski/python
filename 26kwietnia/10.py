import itertools

def liczby():
    list = [0,1,2,3,4,5,6,7,8,9]
    for i in itertools.combinations(list,3):
        yield print(i)

x=liczby()
while(x != 0):
    next(x)
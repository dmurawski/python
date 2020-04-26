class Point:
    counter = []

    def __init__(self, x=0, y=0):
        """Konstruktor punktu."""
        self.x = x
        self.y = y

    def update(self, n):
        self.counter.append(n)

p1 = Point(0,0)
p2 = Point(1,1)
p3 = Point(2,2)
p4 = Point(54,45)
p5 = Point(543543534,-1231323) 
print(p1.counter)

p1.update(123)
print(p1.counter)

p2.update(-2323)
print(p1.counter)

p3.update(2323232)
print(p1.counter)

Point.counter = [23,34,3434]
print(p1.counter)

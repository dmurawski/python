class Wspak:
    """Iterator zwracający wartości w odwróconym porządku"""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

cos = Wspak("Polska")
cos2 = Wspak("ALA")
cos3 = Wspak("12345678")
cos4 = Wspak("KAJAK")


print(next(cos))
print(next(cos))
print(next(cos))
print(next(cos))
print(next(cos))
print(next(cos))
print("-----------")
print(next(cos2))
print(next(cos2))
print(next(cos2))
print("-----------")

print(next(cos3))
print(next(cos3))
print(next(cos3))
print(next(cos3))
print(next(cos3))
print(next(cos3))
print(next(cos3))
print(next(cos3))
print("-----------")
print(next(cos4))
print(next(cos4))
print(next(cos4))
print(next(cos4))
print(next(cos4))


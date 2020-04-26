class Samogloski:
    def __init__(self, data =[]):
        self.data = data
        self.index = -1
        
    def __iter__(self):
        return self
    
    def __next__(self):
        samogloski = ['a','ą','ę','e','i','o','u','ó','y']
        self.index = self.index + 1
        if self.data[self.index] in samogloski:
            return self.data[self.index]
        



string  = Samogloski("Hello World")
print(next(string))
print(next(string))
print(next(string))
print(next(string))
print(next(string))
print(next(string))
print(next(string))
print(next(string))
print(next(string))
print(next(string))
print(next(string))



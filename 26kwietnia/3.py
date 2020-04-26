class Ksztalty:
    # definicja konstruktora
    def __init__(self, x, y):
        # deklarujemy atrybuty
        # self wskazuje że chodzi o zmienne właśnie definiowanej klasy
        self.x=x 
        self.y=y
        self.opis = "To będzie klasa dla ogólnych kształtów"

    def pole(self):
        return self.x * self.y

    def obwod(self):
        return 2 * self.x + 2 * self.y

    def dodaj_opis(self, text):
        self.opis = text

    def skalowanie(self, czynnik):
        self.x = self.x * czynnik
        self.x = self.y * czynnik
class Kwadrat(Ksztalty):

    def __init__(self, x):
        self.x = x
        self.y = x

    def __str__(self):
        return 'Kwadrat o boku {}'.format(self.x)
    def __add__(self,cos):
        return 'Suma boków {}'.format(self.x + self.y)
    def __le__(self, inne):
        return self.x <= inne 

    def __ge__(self, inne):
        return self.x >= inne

    def __gt__(self, inne):
        return self.x > inne

    def __lt__(self, inne):
        return self.x < inne 

    


kw = Kwadrat(5)
kw2 = Kwadrat(6)
print(kw)
print(kw.__add__(1))
print(kw.__le__(kw2))
print(kw.__ge__(kw2))
print(kw.__gt__(kw2))
print(kw.__lt__(kw2))

print("\n",kw <= kw2)
print("\n",kw >= kw2)
print("\n",kw > kw2)
print("\n",kw < kw2)


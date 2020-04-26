class Osoba:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        return "{} {}".format(self.imie, self.nazwisko)


class Pracownik:

    def __init__(self, pensja):
        self.pensja = pensja

    def przedstaw_sie(self):
        return "{} {} i zarabiam {}".format(self.__init__, self.__init__, self.pensja)


class Menadzer(Osoba, Pracownik):

    def __init__(self, imie, nazwisko, pensja):
        Osoba.__init__(self, imie, nazwisko)
        Pracownik.__init__(self, pensja)

    def przedstaw_sie(self):
        return "{} {}, jestem menadżerem i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)


adrian = Menadzer("Adrian", "Mikulski", 12000)
print(adrian.przedstaw_sie())
x1 = issubclass(Menadzer, Osoba)
x2 = issubclass(Menadzer, Pracownik)
x3 = issubclass(Osoba, Osoba)
x4 = issubclass(Osoba, Pracownik)
x5 = issubclass(Pracownik, Osoba)
x6 = issubclass(Pracownik, Pracownik)
print("issubclass:")
print(x1)
print(x2)
print(x3)
print(x4)
print(x5)
print(x6)

y1 = isinstance(adrian, Osoba)
y2 = isinstance(adrian, Pracownik)
y3 = isinstance(adrian, Menadzer)
print("isinstance:")
print(y1)
print(y2)
print(y3)



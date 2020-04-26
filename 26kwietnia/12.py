def Miesiac(n):
    list =["Styczeń","Luty","Marzec","Kwiecień","Maj","Czerwiec","Lipiec",
    "Sierpień","Wrzesień","Październik","Listopad","Grudzień"]
    for n in list:
        yield (n)

Miesiace = Miesiac(12)
print(next(Miesiace))
print(next(Miesiace))
print(next(Miesiace))
print(next(Miesiace))
print(next(Miesiace))
print(next(Miesiace))
print(next(Miesiace))
print(next(Miesiace))
print(next(Miesiace))
print(next(Miesiace))
print(next(Miesiace))
print(next(Miesiace))

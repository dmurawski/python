produkty = {
    "Mleko" : "sztuki",
    "Ziemniaki" : "kg",
    "Marchewka" : "sztuki",
    "Cola" : "sztuki",
    "Ogórki" : "kg"
}
wartosci = {k for k,wartosc in produkty.items() if wartosc == "sztuki"}
print(wartosci)
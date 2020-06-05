class NaZakupy:
    waluta = "zl"
    
    def __init__(self, nazwa_prod, ilosc, jed_miary, cena_jed):
        self.nazwa_prod = nazwa_prod
        self.ilosc = ilosc
        self.jed_miary = jed_miary
        self.cena_jed = cena_jed
    
    def wyświetl_produkt(self):
        print("produkt: ",self.nazwa_prod,"\nilosc :",self.ilosc,"\nJednostka :",self.jed_miary,"\nCena :", self.cena_jed,self.waluta)
    def ile_produktu(self):
        print(self.nazwa_prod,"=",self.ilosc,self.jed_miary)
    def ile_kosztuje(self):
        cena = 0
        cena = self.ilosc*self.cena_jed
        print(self.ilosc,self.jed_miary,self.nazwa_prod,"=",cena,self.waluta)

cukier = NaZakupy("cukier", 2, "kg", 2)
maka = NaZakupy("maka", 1, "kg", 1)
mleko = NaZakupy("mleko", 3, "butelki", 3)
ziemniaki = NaZakupy("Ziemniaki",5,"kg",3)

mleko.ile_kosztuje()
mleko.ile_produktu()
maka.ile_produktu()
maka.ile_kosztuje()
cukier.wyświetl_produkt()
ziemniaki.wyświetl_produkt()
class ciagi_arytemtyczne:
    def __init__(self, a1, różnica, długość_ciągu, Suma_ciągu): 
        self.a1 = a1
        self.różnica = różnica
        self.długość_ciągu = długość_ciągu
        self.Suma_ciągu = Suma_ciągu
    def wyświtel_dane(self):
        print("a1(pierwszy)= ",self.a1,"\nr(roznica)=",self.różnica), 
        print("n(dlugosc)=",self.długość_ciągu,"\nS(suma)=",self.Suma_ciągu)
    def pob_elementy(self):
        x = input("Podaj elementy ciagu:")
        print(x)
    def parametry(self, a1, różnica, długość_ciągu):                          
        self.a1 = a1
        self.różnica = różnica
        self.długość_ciągu = długość_ciągu
        licznik = 1
        an = 0
        while licznik <= self.długość_ciągu:
            an = self.a1 + (licznik - 1) * self.różnica
            print(an)
            licznik += 1
    
    def elementy(self, a1, różnica, Suma_ciągu):
        self.a1 = a1
        self.różnica = różnica
        długość_ciągu = Suma_ciągu/różnica
        print("Dlugosc = ",długość_ciągu)

    def policz_sume(self , a1 , różnica , długość_ciągu):
        self.a1 = a1
        self.różnica = różnica
        self.długość_ciągu = długość_ciągu
        Suma_ciągu = 0
        an = 0
        licznik = 1
        while licznik <= self.długość_ciągu:
            an = self.a1 + (licznik - 1) * self.różnica
            licznik += 1
        Suma_ciągu =((self.a1 + an) / 2) * self.długość_ciągu
        print("\n\nAn = ",an)
        print("licznik = ",licznik)
        print("Suma =",Suma_ciągu,)

ciag1 = ciagi_arytemtyczne(1, 2 , 15 ,500)
ciag1.parametry(1,2,10)
ciag1.policz_sume(1,4,10)
ciag1.elementy(1,2,100)
ciag1.wyświtel_dane()
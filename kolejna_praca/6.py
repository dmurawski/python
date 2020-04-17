class slowa:

    def __init__(self, slowo1, slowo2):
        self.slowo1 = slowo1
        self.slowo2 = slowo2

    def metagram(self):
        licznik = 0 
        z = 0
        x = len(self.slowo1)
        while z < x:
            if self.slowo1[z] != self.slowo2[z]:
                licznik = licznik + 1
            z = z +1
        if licznik > 1 :
            print("slowo",self.slowo1,"i",self.slowo2," -nie metagramy")
        else:
            print("slowo",self.slowo1,"i",self.slowo2," -metagramamy")
            
    def palindrom(self):
        revers = reversed(self.slowo1)
        revers2 = reversed(self.slowo2)
        if(list(self.slowo1) == list(revers)):
            print("slowo",self.slowo1," -palindrom")
        else:
           print("slowo",self.slowo1," -nie palindrom")
        if(list(self.slowo2) == list(revers2)):
            print("slowo",self.slowo2," -palindrom")
        else:
           print("slowo",self.slowo2," -nie palindrom")


    def anagram(self):
        x = sorted(self.slowo1)
        y = sorted(self.slowo2)
        if(x == y):
            print("slowo",self.slowo1,"i",self.slowo2,"-anagramy")
        else:
            print("slowo",self.slowo1,"i",self.slowo2,"-nie anagramy")

    def wyświetl(self):
        print("Slowo1:",self.slowo1,"\nSlowo2:",self.slowo2)          


pierwsze_slowo = slowa("ala", "ola")
pierwsze_slowo.palindrom()
pierwsze_slowo.metagram()
pierwsze_slowo.anagram()
pierwsze_slowo.wyświetl()

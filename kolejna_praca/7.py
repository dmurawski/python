class robaczek:

    def __init__(self, x, y, krok):
        self.x = x
        self.y = y
        self.krok = krok
    
    def w_lewo(self, ile_krokow):
        self.x = self.x - ile_krokow*self.krok

    def w_prawo(self, ile_krokow):
        self.x = self.x + ile_krokow*self.krok

    def gdzie_jestem(self):
        print("x =",self.x,"y =", self.y)

    def w_gore(self, ile_krokow):
        self.y = self.y+ ile_krokow*self.krok

    def w_dol(self, ile_krokow):
        self.y = self.y - ile_krokow*self.krok 
        
    def __del__(self):
        print("delete",self) #zadanie 8 ?

glizda = robaczek(0,0,3)
glizda.w_gore(12)
glizda.w_dol(32)
glizda.w_lewo(12)
glizda.w_prawo(22)
glizda.gdzie_jestem()
glizda.__del__()
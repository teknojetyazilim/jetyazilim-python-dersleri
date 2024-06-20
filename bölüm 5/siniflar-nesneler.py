class Araba:
    def _init_(self , marka , model , yil):
        self,marka = marka
        self,model = model
        self,yil = yil

    def bilgi_ver(self):
        print(f"{self.yil}model{self.marka}{self.model}")

        araba1 = Araba("bmw","m5",2020)
        araba2 = Araba("honda","civic",2020)
        
        araba1.bilgi_ver()
        araba2.bilgi_ver()

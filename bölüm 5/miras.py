class Araba:
    def __init__(self, marka, model, yil):
        self.marka = marka
        self.model = model
        self.yil = yil

    def bilgi_ver(self):
        print(f"Bu araba {self.yil} model {self.marka} {self.model}")

class ElektrikliAraba(Araba):
    def __init__(self, marka, model, yil, batarya_kapasitesi):
        super().__init__(marka, model, yil)
        self.batarya_kapasitesi = batarya_kapasitesi

    def batarya_bilgisi(self):
        print(f"Bu araba {self.batarya_kapasitesi} kWh kadar kapasiteye sahiptir")

# Elektrikli araba örneği
e_araba = ElektrikliAraba("Tesla", "Model S", 2023, 100)
e_araba.bilgi_ver()
e_araba.batarya_bilgisi()

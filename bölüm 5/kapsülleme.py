class Araba:
    def __init__(self, marka, model , yil ):
        self._marka = marka
        self._model = model
        self._yil = yil

    def bilgi_ver(self):
        print(f"{self._yil} model {self._marka} {self._model}")

    def marka_degis(self, yeni_marka):
        self._marka = yeni_marka

araba = Araba("honda", "civic")
araba.bilgi_ver()
araba.marka_degis("toyota")
araba.bilgi_ver()

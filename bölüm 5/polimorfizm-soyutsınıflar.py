from abc import ABC,abstractmethod

class Hayvan(ABC):
    @abstractmethod
    def ses_cikar(self):
        pass
class Kedi(Hayvan):
    def ses_cikar(self):
        print("miyav")
class Kopek(Hayvan):
    def ses_cikar(self):
        print("hav hav")

kedi = Kedi()
kopek = Kopek()

kedi.ses_cikar()
kopek.ses_cikar()
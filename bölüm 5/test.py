class Kitap:
    def __init__(self, baslik, yazar, yil ):
        self.baslik = baslik
        self.yazar = yazar
        self.yil = yil 

    def bilgi_ver(self):
            print(f"{self.baslik}, {self,yazar} tarafından yazılmıştır ve {self,yil} yilinda yayınlanmıştır")
class Kutuphane:
    def __init__(self):
        self.kitaplar = []

    def kitap_ekle(self,kitap):
         self.kitaplar.append(kitap)
         print(f"{kitap, baslik} kütüphaneye eklendi")

    def kitap_sil(self, baslik):
        for kitap in self.kitaplar:
            if kitap.baslik == baslik:
                self.kitaplar.remove(kitap)
                print(f"{baslik}silindi")
                return
            print(f"{baslik}bulunamadı")
    def kitaplari_listele(self):
        if not self.kitaplar:
            print("kütüphanede kitap yok")
        for kitap in self.kitaplar:
            kitap.bilgi_ver()
kutuphane = Kutuphane()
while True:
    print("\nKütüphane yönetimi")
    print("1. kitap ekle")
    print("2. kitap sil")
    print("3.kitapları listele")
    print("4. çıkış yap")
    secim = input("seçiminizi yapınız")

    if secim == '1':
        baslik = input("Kitap başlığı")
        yazar = input("yazar")
        yil = input("yıl")
        yeni_kitap = Kitap(baslik, yazar, yil)

        kutuphane.kitap_ekle(yeni_kitap)

    elif secim == '2':
        baslik = input("silinecek kitap başlığı")
        kutuphane.kitap_sil(baslik)
    elif secim == '3':
        kutuphane.kitaplari_listele()
    elif secim == '4':
        print("çıkış yapılıyor")
        break
    else:
        print("geçersiz seçim")
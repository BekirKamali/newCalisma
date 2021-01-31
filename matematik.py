class Matematik:
    def __init__(self,sayi1,sayi2):
        self.sayi1=sayi1
        self.sayi2=sayi2
        print("matematik kayıdı oluştu")
    def topla(self):
        return self.sayi1 + self.sayi2

    def cıkar(self):
        return self.sayi1 - self.sayi2

    def böl(self):
        return self.sayi1 / self.sayi2

    def carp(self):
        return self.sayi1 * self.sayi2

matematik = Matematik(10,5)
sonuc = matematik.topla()
print("toplama sonuç  " + str(sonuc))

sonuc = matematik.cıkar()
print("çıkarma sonuç  " + str(sonuc))

sonuc = matematik.böl()
print("bölüm sonuç  " + str(sonuc))

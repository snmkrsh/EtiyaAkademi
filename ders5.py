# Fonksiyonlar
# Kendini tekrarlayacak olan yapiları tek elden ilerletmemize olağan sağlayan yapilardir.
# defination kelimesinden gelen def keywordü ile tanimlanirler.

def ortalamaHesapla() -> None: # Bu fonksiyonda return yok geriye değer dönmüyor.
    # none dönecektir yazdık bu yazma şekli zorunlu değildir bilgilendirme amaçlıdır.
    final = 60
    vize = 100
    ortalama = (vize*0.4 + final*0.6)
    print(ortalama)

# triggerlamak, çalıştırmak, execute etmek, methodu çağırmak, fonksiyonu çalıştırmak.
ortalamaHesapla()

def ortalamaHesaplaVeDondur() ->float : # bu fonksiyon geriye(return) float dönecektir.
    # bilgilendirmesi için koyduk zorunlu değildir. 
    final = 100
    vize = 100
    ortalama = (vize*0.4 + final*0.6)
    # expression
    return ortalama
    # geriye döndürmek

# bir fonksiyonu değişkene eşitledik. 
# bu şu demek oluyor return edilen değer (geri dönülen değer) ne ise onu al ve ort ye ata.
ort = ortalamaHesaplaVeDondur() 
print(ort)
# burada geriye dönen değil fonksiyonu çıktı olarak aldık.
print(ortalamaHesaplaVeDondur())

# Fonksiyona parametre tanimlayabiliriz.
def ortalamaHesaplayici(vize,final):
    ortalama = (vize*0.4 + final*0.6)
    return ortalama

print(ortalamaHesaplayici(34,55))

# Bu şekilde de bi kullanım ile heafıza alan kullanımını azaltmış olabiliriz.
def ortalamaHesaplayiciDeneme(vize:float,final:float): # float belirterek kodun okunurluğunu arttirabiliriz.
    return (vize*0.4 + final*0.6)

print(ortalamaHesaplayiciDeneme(34,55))


# Aşağıda ki örnek pair ödeviydi.
# Kullaniciyi sürekli konsolda tut -> sonsuz döngü
# hesap makinesi : 4 işlem ve mod alma
# q girildiğinde programdan çıkıs yapilacak -> break (sonsuz döngüyü kirmak)
def calculateSum():
    num1 = getNumberFromUser()
    num2 = getNumberFromUser()
    print(f"İşlem Sonucu : {num1 + num2}")

def calculateMinus():
    num1 = getNumberFromUser()
    num2 = getNumberFromUser()
    print(f"İşlem Sonucu : {num1 - num2}")
    
def calculateDivide():
    num1 = getNumberFromUser()
    num2 = getNumberFromUser()
    print(f"İşlem Sonucu : {num1 / num2}")
    
def calculateMultiply():
    num1 = getNumberFromUser()
    num2 = getNumberFromUser()
    print(f"İşlem Sonucu : {num1 * num2}")
    
def calculateMod():
    num1 = getNumberFromUser()
    num2 = getNumberFromUser()
    print(f"İşlem Sonucu : {num1 % num2}")
    
def getNumberFromUser():
    return float(input("Sayi Giriniz: "))

while True:
    userInput = input("Yapmak istediğiniz işlemi seçiniz: ")
    if userInput == 'q':
        break
    elif userInput == '+':
        calculateSum()
    elif userInput == '-':
        calculateMinus()
    elif userInput == '/':
        calculateDivide()
    elif userInput == '*':
        calculateMultiply()
    elif userInput == '%':
        calculateMod()
    else:
        print("Hatali İslem Seçildi:")

# Class, nesne, obje, sınıf
class Human:
    name = ""
    age = 20
    # İnitialize Yapici Blok 
    def __init__(self,name,age):
        print("Yapici Blok Çalişti")
        self.name = name 
        self.age = age
    # Davranişlar
    def talk(self,message):
        print(message)
        print(f"Merhaba Benim adim {self.name} ve yaşım {self.age}.")
    def walk(self):
        print(f"{self.name}  Walking..")

# Instane üretmek - örne üretmek
human2 = Human("Halit",25)
human2.talk("Merhaba")
human2.walk()


# Modüler Yapi: Okunabilirlik açısından farklı dosyalarda kod bulunması index.py dosyası devam niteliğindedir.


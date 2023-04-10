# FONKSİYONLAR
# Bir işlemi tekrar tekrar yapmak yerine, tek fonksiyonla işlem fazlalığından kurtulmayı hedefler.

def kredleriListele():
    krediler = ["Hizli Kredi","Maasini Akbank'tan Alanlara Özel Kredi","Mutlu Emekli İhtiyaç Kredisi"]
    for kredi in krediler:
        print("option "+kredi+" option")

# Yukarıda bir fonksiyon tanımladık. Fonksiyon def ile tanımlanır.

kredleriListele()  # Fonksiyonu çağırdık.
kredleriListele()
kredleriListele()


def fibonacci():
    x = 1
    y = 1
    fib= [x,y]
    for i in range(20):
        z = x + y
        x = y
        y = z
        fib.append(z)
    print(fib)

fibonacci()
fibonacci()


def mukemmelSayi():
    num = int(input("Bir Sayi Giriniz: "))
    toplam = 0
    for i in range(1,num):
        if num % i == 0:
            toplam += i
    if num == toplam :
        print("Seçilen Sayi Mükemmel Sayidir.")
    else: 
        print("Seçilen Sayi Mükemmel Sayi Değildir.")

mukemmelSayi()
mukemmelSayi()


def hesapMakinesi():
    sayi1 = int(input("bir sayi giriniz:"))
    sayi2 = int(input("bir sayi giriniz:"))
    islem = input("işlem seçiniz:")

    toplam = sayi1 + sayi2
    cikarma = sayi1 - sayi2
    carpma = sayi1 * sayi2
    bolme = sayi1 / sayi2

    if islem == "+":
        print(toplam)
    elif islem == "-":
        print(cikarma)
    elif islem == "*":
        print(carpma)
    elif islem == "/":
        print(bolme)
    else :
        print("hatalı işlem seçimi")

hesapMakinesi()

def ortalama():
    vize = float(input("vize notunu giriniz:"))
    final = float(input("final notunu giriniz:"))
    ortalama = (vize*0.4) + (final*0.6)

    if ortalama >= 0 and ortalama < 50:
        print(f'FF, notunuz:{ortalama}')
    elif ortalama >= 50 and ortalama < 60:
        print(f'DD, notunuz:{ortalama}')
    elif ortalama >= 60 and ortalama < 70:
        print(f'CC, notunuz:{ortalama}')
    elif ortalama >= 70 and ortalama < 80:
        print(f'BB, notunuz:{ortalama}')
    elif ortalama >=80 and ortalama <= 100:
        print(f'AA, notunuz:{ortalama}')

ortalama()






"""
print("İlk Sayfa")
krediler = ["Hizli Kredi","Maasini Akbank'tan Alanlara Özel Kredi","Mutlu Emekli İhtiyaç Kredisi"]
for kredi in krediler:
    print("option"+kredi+"option")


print("İkinci Sayfa")
krediler = ["Hizli Kredi","Maasini Akbank'tan Alanlara Özel Kredi","Mutlu Emekli İhtiyaç Kredisi"]
for kredi in krediler:
    print("option"+kredi+"option")


print("Üçüncü Sayfa")
krediler = ["Hizli Kredi","Maasini Akbank'tan Alanlara Özel Kredi","Mutlu Emekli İhtiyaç Kredisi"]
for kredi in krediler:
    print("option"+kredi+"option")

"""


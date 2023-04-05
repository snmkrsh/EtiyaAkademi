
# DEĞİŞKENLER
"""
baslik  = "  HABERİNİZ OLSUN ! " # string
vade = 12 # integer
faizOrani1 = 1,47 # float
faizOrani2 = 1.44
faizOrani3 = 1.47

print(faizOrani1)
print(faizOrani2)
print(faizOrani3)
print(vade)
print(baslik)

print(type(baslik))
print(type(vade))
print(type(faizOrani1))

mesaj = "Hoşgeldin"
musteriAdi = "Sinem"
musteriSoyadi = "Karaşah"
sonucMesaj = mesaj +" "+ musteriAdi +" "+ musteriSoyadi
print(sonucMesaj)

sayi1 = 10
sayi2 = 20
print(sayi1 + sayi2)
print(sonucMesaj)
"""


# if-else ŞART BLOKLARI
"""
dolarDun = 7.65
dolarBugun = 7.55

if dolarDun < dolarBugun :
    print("Artis Oku")
if  dolarDun> dolarBugun :
    print("Azalis Oku")
if  dolarDun == dolarBugun:
    print("Esittir Oku")

print("/////////")

# else ile kullanım
if dolarDun < dolarBugun :
    print("Artis Oku")
elif dolarDun > dolarBugun : 
    print("Azalis Oku")
else:
    print("ESittir Oku")
"""


# DİZİLER
"""
krediler = ["Hizli Kredi","Maasini Halkbank'tan Alanlara Özel","Mutlu Emekli İhtiyac Kredisi"]
print(krediler)
print(krediler[0])
print(krediler[1])
print(krediler[2])
print(len(krediler)) # listenin kaç elemandan olustuğu bilgisini verir.

krediler[0] = "Çabuk Kredi" # 0.elemana atama yaptık.
print(len(deneme))
print(deneme)
"""




# DÖNGÜLER
"""
krediler = ["Hizli Kredi","Maasini Halkbank'tan Alanlara Özel","Mutlu Emekli İhtiyac Kredisi"]

for kredi in krediler : # krediler içindeki tüm değerleri gezer. O anki gezdiğine(alias değer) verdiğimiz takma isim kredi'dir(x,y vb de olabilirdi.)
    print(kredi) 

print("////////////")

for i in range(10): # range ile döngünün 10 kere tekrarlaması sağlanır. / 0 dan 9 a kadar saydırdık.
    print(i)

# i 0 dan başlar.

print("////////////")

for i in range(len(krediler)):
    print(krediler[i])
 
#i 0 dan başlar krediler uzunluğu kadar saydırdık ve print ile o an aliasta ki değeri yazdırdık.

print("////////////")
for i in range(3,10): # 3'den 10'a kadar saydırdık.
    print(i)

print("////////////")

for i in range(0,10,2): # 0'dan başla 10'a kadar -10 dahil değil- 2'ser arttırarak devam et.
    print(i)
"""


# FONKSİYONLAR

def kredileriListele():
    krediler = ["Hizli Kredi","Maasini Halkbank'tan Alanlara Özel","Mutlu Emekli İhtiyac Kredisi"]
    for kredi in krediler :
        print("<Option>"+kredi+"<Option>") 

kredileriListele() # fonsiyon çağırma
kredileriListele()
kredileriListele()
kredileriListele()

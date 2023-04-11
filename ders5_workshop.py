# Class: Fonksiyon ve değerleri, değişkenleri içerisinde tutan yapılardır.
# this gibi düşün. class içinde tanımlanan her fonksiyon için bir parametre self ile rezerve edilir.
# self ismi vermek zorunda değilim ama bir parametre alınma zorunluluğu vardır. Self en yaygın kullanılan isimdir.
# self rezerve bir parametredir bunun için sentence parametresi birinci parametre olarak okunur.
# instance => örnek

class Human:
    # built - in
    # constructor alanı yani yapici alani. Bir nesne ürettiğimiz anda çalişan alan gibi düşünebiliriz.
    # initialize etmek gibi düşünebiliriz.
    def __init__(self,name):
        self.name = name # fonksiyonda bir name parametresi istiyorum bu objenin genel name'i olsun demek.
        print("Bir human instance'i üretildi..")
    
    def __str__(self) -> str: # self parametreye sahip str built. ilgili fonksiyonun geriye donus tipini 'str' gösterir.
        return f"STR Fonksiyonundan Dönen Deger: {self.name}"

    def talk(self,sentence): 
        print(f"{self.name}: {sentence}") # self. ile yazarak class içinde name aramasını sağlarız. 
        # self. yazmasaydık eğer fonksiyon içinde name arayacaktı hata verecekti.
        # fonksiyon içinde diğer fonksiyonu çağırırkende self.walk()  şeklinde çağırm yapmalıyız yoksa kendi içinde arar name'i ve name kendi içinde yoksa hata verir.
    
    def walk(self):
        name = "Bilge"
        print(f"{name} is walking..")    

"""
human1 = Human("Sinem") # human1 değişkenine Human classından bir adet instance atamış olduk.

human1.talk("Merhaba ") 
# self rezerve bir parametredir bunun için sentence parametresi birinci parametre olarak okundu.
# self yokmuş gibi davranıp sentence a merhaba yı atadı gibi düşün.
human1.walk()

name = "Serpil" # Bu değişim etkilemez classı 
human1.name = "Sevgi" # Bu değişim etkiler.
print("//////////////////////")
human1.talk("Merhaba") # self ile yaptığımız için sevgi :Merhaba elde ettik.
human1.walk() # burada name atamasını self ile yapmamıştık o sebeple yine kendi içinde olan name'i alacak. değişim olmayacak.
 

human2 = Human("Merve")
human2.name = "Merve"
human2.talk("Selam")
human2.walk() # burada name atamasını self ile yapmamıştık o sebeple yine kendi içinde olan name'i alacak. değişim olmayacak.

human3 = Human("Tarik") # içinde ismi belirtmezsek hata aliriz. yukarida parametre var burda yollamamıs oluruz. 
human3.name = "Berker" # böyle değişebiliriz.
human3.talk("Hoşgeldiniz...")
human3.walk()
"""

human4 = Human("Ali")
human4.talk("Merhaba! ")
human4.walk() # bilge is walking çiktisi aliyoruz cünkü name i fonksiyon içinden aliyor.
print(human4)

human5 = Human("Veli")
human5.talk("Selam")
human5.walk()
print(human5)
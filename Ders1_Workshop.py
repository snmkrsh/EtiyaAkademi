isimler = []  #isimler adında bos dizi olusturduk.
for i in range(10):
    isim = input("İsminizi Giriniz: ") #kullanıcıdan veri istedik.
    isimler.append(isim) #aldığımız veriyi diziye ekledik append() komutu bunun için kullanıldı, listenin sonuna yeni ögeyi ekler.
print(isimler)

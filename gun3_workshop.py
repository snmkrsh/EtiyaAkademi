numbers = []
for i in range(10):
    num = int(input("Sayi Giriniz: ")) #kullanıcıdan veri istedik.
    numbers.append(num) #aldığımız veriyi diziye ekledik append() komutu bunun için kullanıldı, listenin sonuna yeni ögeyi ekler.
print(numbers)

smallNum = min(numbers)
biggestNum = max(numbers)

print(f'Girilen En Küçük Değer: {smallNum}') # en küçük değer.
print(f'Girilen En Büyük Değer: {biggestNum}') # en büyük değer.

for evenNum in range(0,biggestNum,2):  # 0 dan başlayıp en büyük sayıya kadar olan çift sayıları yazdırdık.
        print(evenNum)


# alt limit belirleyip listemizdeki üst limite kadar ikişer saydırdıık.        
upNum= int(input("Alt limit giriniz: "))
num2 = int(input("Alt limit belirlemek için 1 giriniz: ")) #saydırma işlemi için alt taban belirledik.
if num2 == 1:
     for i in range(upNum, biggestNum, 2):
          print(i)
else:
     print("Geçersiz bir giriş yapildi.")


     


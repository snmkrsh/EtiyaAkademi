
# Workshop odevine baktik.

# kullanıcıdan 10 adet sayı al en büyük olanı kullanıcıya göster.
# alınan sayılardan en büyük 2. yi göster.
# alınan sayılarda diziyi büyükten küçüğe sırala

# numbers =[]
# for i in range(3):
#     sayi = int(input(f"{i+1}. sayinin girişini yapiniz: "))
#     numbers.append(sayi)

# maxNum = max(numbers)
# minNum = min(numbers)

# print(numbers)
# print(f"Girdiğiniz en büyük sayi: {maxNum}")

# numbers.sort() # arrayimizi küçükten büyüğe sıraladık. sort fonksiyonu ile
# print(numbers[len(numbers)-2]) # en büyük 2. sayıyı yazdırdık.
# numbers.sort(reverse=True) # array büyükten küçüğe sıraladık.
# wantMaxNum = int(input("En  büyük kaçinci sayiyi istersin: "))
# print(numbers[wantMaxNum-1])

# #kullanıcının vereceği üst limit ile 0 dan üst limitte dahil tüm çift sayıları yazdıralım.
# 
# upNum = int(input("Üst limit için bir sayi giriniz: "))
# for i in range(upNum+1):
#    if i % 2 == 0:
#        print(i)
# 

# 0 bizim alt limitimiz olduğu için mod almadan range içine range(0,upNump+1,2) seklinde yapabiliriz.

# alt limiti de kullanıcıdan alalım.

# upNum = int(input("Üst limit için bir sayi giriniz: "))
# downNum = int(input("Alt limit için bir sayi giriniz: "))
# for i in range(downNum, upNum):
#     if i % 2 == 0:
#         print(i)

""" Döngüler / Loops """

# For
# i değerim 0 dan başlasın i<10 == True oldukça sağlasın.
for i in range(10):
    print(i)
# range(x) tek bir print içerirse o kaça kadar ilerleyeceğini söyler.
# range(x,y,z) ise başlangıç,son,ilerleme şeklinde kullanılır.

list =["Sinem","Ali","Veli","Volkan"]

#iterate etmek, iteration belli bir koleksiyonun üzerinde eleman eleman gezebilmek.
for i in range(len(list)): 
    print(f"{i+1}. öğrenci: {list[i]}")

for ogrenci in list:
    print(f"Öğrenci: {ogrenci}")

# break keywordü
for i in range(len(list)):
    if i > 2: 
        break
    print(f"{i+1}. öğrenci: {list[i]}")

# pass keywordü, boş bir loop için kullanılır. boş çalışın diye
for i in range(0,10):
    if i == 4 :
        pass
    else:
        print(i)

# veya loop tamamen boş çalışsın istiyorsak kullanabiliriz.
for i in range(0,10):
    pass

# pass keyword çok tercih edilmez.

# continue keywordü itarasyonda ki o değeri atlatıp diğer değerden devam ettirir.
for i in list:
    if i == "Volkan":
        continue
    print(f"Öğrenciler: {i}")

# while boolenDeger 
# infinite loop sönsüz döngüdür. Ctrl + C ile çıkılır.
                    # while True:
                    #    print("Merhaba")

i = 0
while i < 10 :
    i = i + 1
    if i ==3:
        continue # 3. loopu atlattık.
    print(f"While içindeki değer : {i}")


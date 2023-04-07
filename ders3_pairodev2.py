toplam = 0
num = int(input("Bir sayi giriniz: "))
for i in range(1,num):
    if num % i == 0:
        toplam += i

if toplam == num:
    print("Mükemmel Sayi! ")
else:
    print("Mükemmel Sayi Değildir! ")
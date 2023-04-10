"""
def calculate():
    sayi1 = int(input("Bir sayi giriniz: "))
    sayi2 = int(input("İkinci sayiyi giriniz: "))
    toplam = sayi1 + sayi2
    cikarma = sayi1 - sayi2
    carpma = sayi1 * sayi2
    bolme = sayi1 / sayi2
    mod = sayi1 % sayi2
    
    islem = input("islem seçiniz: ")
    if islem == "+":
        print(toplam)
    elif islem == "-":
        print(cikarma)
    elif islem == "*":
        print(carpma)
    elif islem == "/":
        print(bolme)    
    elif islem == "%":
        print(mod)       
    else:
        print("Hatali Seçim")
            
cikis = input("Çikmak istiyor musunuz? ")

while cikis != 'q':
    calculate()
    cikis = input("Çikmak istiyor musunuz? ")
"""


def mult():
    multiplication= num1 * num2
    print(multiplication)

def ext():
    extration = num1 - num2
    print(extration)

def add():
    addition = num1 + num2
    print(addition)

def div() :
    division= num1 / num2
    print(division)

def mod() :
    mod= num1 % num2
    print(mod)

choose = 0
while choose == 0:
    num1 = int(input("Bir sayi giriniz: "))
    num2 = int(input("İkinci sayiyi giriniz: "))
    qProcess = input("Bir işlem Seçiniz: /cikis için 'q' ya basabilirsiniz! ")
    if qProcess == 'q':
        print("Cikis Yapiliyor.")
        choose == 1
        break
    elif qProcess == '+':
        add()
    elif qProcess == '-':
        ext()
    elif qProcess == '/':
        div()
    elif qProcess == '*':
        mult()
    elif qProcess == "%":
        mod()
    else:
        print("hatali giriş")
        

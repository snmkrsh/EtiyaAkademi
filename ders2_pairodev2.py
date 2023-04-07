
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
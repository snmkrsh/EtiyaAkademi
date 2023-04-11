from classOgrenci import Student 
from classOgretmen import Teacher

studentListe = []
teacherListe = []

def addStudent(student):
    studentListe.append(student)

def addTeacher(teacher):
    teacherListe.append(teacher)

while True:
    choose = input("Kayıt edilecek olan Öğrenci(s) mi Öğretmen mi(t): \ cikis için 'q' basiniz ")

    if choose == 't':
        name = input("Kayit edilecek öğretmen adi :")
        surname = input("kayit edilecek öğretmen soyadi:")
        brans = input("Branşi : ")
        ogretmen = Teacher(name,surname,brans)
        teacherListe.append(ogretmen)
        

    elif choose == 's':      
        name = input("Kayit edilecek öğrenci adi :")
        surname = input("kayit edilecek öğrenci soyadi:")
        no = int(input("Okul Numarasini Giriniz: "))
        ogrenci = Student(name,surname,no)
        studentListe.append(ogrenci)
    
    elif choose == "q":
        print("Çikiş yapiliyor...")
        break

    else:
        print("hatali seçim ")


if len(teacherListe)== 0 and len(studentListe)== 0:
    print("Boş liste ekleme yapilmadi..")
elif len(teacherListe)== 0 and len(studentListe)!= 0:
    print("Sadece öğrenci listesine ekleme yapildi. Öğrenci Listesi: ")
    print(studentListe)
elif len(studentListe) == 0 and len(teacherListe) != 0:
    print("Sadece Oğretmen listesine ekleme yapildi. Öğretmen Listesi: ")
    print(teacherListe)
else:
    print(teacherListe)
    print(studentListe)

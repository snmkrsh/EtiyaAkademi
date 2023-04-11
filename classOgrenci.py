class Student:
    name = ""
    surname = ""
    ogrNo = 0
    def __init__(self,name,surname,no) -> None:
        self.name = name
        self.surname=surname
        self.no = no

    def ogrenciYaz(self):
        print(f"Öğrenci sisteme kayit edildi Tam Adi: {self.name} {self.surname}. Numarasi: {self.ogrNo}")
        
    def __repr__(self):  # Bu Fonksiyon bize kullanıcı adı soyadı numarasının gösterimini düzenlememizi sağlıyor.
        return f"İsim: {self.name} Soyismi :{self.surname} Okul no: {self.no}" 

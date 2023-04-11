class Teacher:
    name = ""
    surname = ""
    brans = ""
    def __init__(self,name,surname,brans) -> None: # init nesneyi olusturduğumuzda çalışan ilk fonksiyondur.
        self.brans=brans
        self.name = name
        self.surname = surname

    def ogretmen(self):
        print(f"Öğretmen sisteme kayit edildi Tam Adi: {self.name} {self.surname}. Branşi: {self.brans}")

    def __repr__(self): 
        return f"İsim: {self.name} Surname :{self.surname} Okul Branşı: {self.brans}" 
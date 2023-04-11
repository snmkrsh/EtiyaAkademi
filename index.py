# Modüler yuapıyı anlamak için ders5.py deki Human'ı burda kullanabilir yap.
# direkt ders5 i import ettik.
# from ders5 import Human deseydik.
# ders5.Human dememize herek olmadan Human çağırabilirdik.

import random
import ders5 
human1 = ders5.Human("Sinem",23)
human1.talk("Selam")

#   from ders5 import Human as Insan # as ile alias => takma ad
#   human1 = Insan("leyla", 24)
#   human1.talk("Merhaba")

# pip install dosyaAdı ile terminalden sisteme modül ekleyebiliyoruz.
# indirmeden sonra kullanılacak dosyaya import ile eklemeliyiz.

# import random diyerek rendom sayi alabiliriz.
print(random.random()) 
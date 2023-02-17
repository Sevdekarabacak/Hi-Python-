
###############################################################################
# String Methods
##############################################################################

# Len fonksiyonu kaç karakterden oluştuğunu bize gösterir.

bolum = "İstatistik"
len(bolum)

###################################################################################

# upper() & ve lower() methodları
universite = "OnDoKuZ MaYıS ÜnİvErSiTeSi"

# upper tüm harfleri büyük harfe dönüştürür.
universite.upper()

# lower tüm harfleri küçük harfe dönüştürür.
universite.lower()

###################################################################################

# replace  karakterleri değiştirmemizi sağlar.

il = "ISTANBUL"
il.replace('U', "T")

###################################################################################

# split karakterleri bölmek için kullanılır.

sarki = "Gökyüzünü tutamam yıldızları çalanlar var."

sarki.split()

###################################################################################

# title sadece ilk harfleri büyük yazdırır.

kisi = "dilara"
kisi.title()

cumle = "veri yapıları konusu"
cumle.title()

###################################################################################

# capitalize sadece baştaki ilk harfi büyük yazdırır

mesaj = "I Love You"
mesaj.capitalize()

###################################################################################

# strip baştaki ve sondaki boşluk karakterlerini siler.

bilgi = "  Türkiyede 81 il vardır.   "

bilgi.strip()

###################################################################################

# swapcase ile karakter dizisi içindeki büyük harfleri küçük, küçük harfleri büyük yazdırma

var = "beauty AND THE beast"
var.swapcase()

###################################################################################

# islower karakter dizisinin TAMEMEN küçük harflerden oluşup oluşmadığını sorgular

ornek = "NEVSEHIR"

ornek.islower()

ornek2 = "nevsehır"

ornek2.islower()

###################################################################################

# isupper karakter dizisinin TAMAMEN BÜYÜK  harflerden oluşup oluşmadığını sorgular.

ornek = "NEVSEHIR"

ornek.isupper()

ornek2 = "nevsehır"

ornek2.isupper()

###################################################################################

# istitle karakter dizisi içindeki kelimelerin ilk harfleri büyük mü sorgusu yapar.

number = "Sayılar"

number.istitle()

###################################################################################

# isspace karakter dizisinin tamamen boşluk karakterlerinden mi oluştuğunu sorgular.

bosluk = "               "

bosluk.isspace()

bosluk_degil = "                sf"

bosluk_degil.isspace()

###################################################################################

# isnumeric karakter dizisinin tamamı sayısal değerler mi alıyor sorgusu yapar.

print("12345aaaaaaa".isnumeric())

print("0000000000".isnumeric())

###################################################################################

# startswith verinin belli bir değer ile başlayıp başlamadığına bakar.

kelime = "sezen aksuuuuuu"  # kelimenin ilk harfi s ile mi başlıyor?
kelime.startswith("s")

kelime.startswith("s", 0)  # s harfi kelimenin 0. indisinde mi?

kelime = "dezen dksuuuuuu"  # d harfi kelimenin 0. indisinden başlayıp 7.indisine kadar devam ediyor mu?
kelime.startswith("d", 0, 7)

###################################################################################

# count verinin içerisinde belirli bir karakterden kaç adet olduğunu belirler.

vocable = "Sakarya"
vocable.count("a")

###################################################################################

# join verinin içerisindeki her bir karakterden sonra eklemek istediğimiz karakteri birleştirir.

a = "Fatih"
print("-".join(a))

################################################################################################################################

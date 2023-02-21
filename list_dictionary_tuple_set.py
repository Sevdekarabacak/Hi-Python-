################################################################################
# Liste (List)
################################################################################

# -Değiştirilebilir
# -Sıralıdır (İndex işlemler yapılabilir)
# -Kapsayıcıdır

notes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
type(notes)

names = ["Ali", "Ayşe", "Fatma"]
type(names)

# Listelerden eleman seçimi
eleman_1 = names[0]
eleman_2 = names[1]
eleman_3 = names[2]

# Dilimleme yöntemi ile eleman seçimi
elaman = notes[0:4]

# Liste içinde liste

not_names = ['Ali', "Ayşe", "Fatma", [1, 2, 3]]
type(not_names)

type(not_names[3])
type(not_names[3][1])

# Listelerde eleman değiştirme
notes[0] = 99
print(notes)

#######################################################################
# Listelerin methodlarları
########################################################################

# Kullanılabilecek methodları gösterir.
dir(notes)

# len: eleman bilgisini bize verir.

eleman_sayisi = len(notes)

# append: eleman eklememizi sağlar.

notes.append(100)
print(notes)

# pop: indexe göre eleman siler.

notes.pop(0)
print(notes)

# insert: indexe göre eleman ekler.

# 3.indexe 800 değeri eklenir.
notes.insert(3, 800)
print(notes)

############################################################################################
# Sözlük (Dictionary)
############################################################################################

# Değiştirilebilir
# Kapsayıcıdır

sozluk = {"REG": "Regresyon",
          "LOG": "Lojistik Regresyon"}

eleman = sozluk["LOG"]

yas = {"SEVDE": 21, "FATİH": 24}

sevde_yas = yas["SEVDE"]

gun = {"İLKER": [0, 10, 90, 2], "AHMET": [3, 6, 7, 8]}

ilker_gun = gun["İLKER"]

gun["İLKER"][2]

# key sorgulama

"ayşe" in gun

"İLKER" in gun

# key'e göre value'ye erişmek

sozluk["REG"]
sozluk.get("REG")

# Value değiştirmek

sozluk["REG"] = ["SFU", 10]
print(sozluk)

# Tüm key'lere erişmek
sozluk.keys()

# Tüm value değerlerine erişmek
sozluk.values()

# Tüm key-value çiftlerine ulaşmak
sozluk.items()

# key-value değerleirni güncellemek
sozluk.update({"REG": 11})
print(sozluk)

# Yeni bir key-value çifti atamak

sozluk.update({"SED": "F"})
print(sozluk)

################################################################################
# Demet (Tuple)
################################################################################

# Değiştirilemez
# Sıralıdır
# Kapsayıcıdır

t = ("nur", "seyda", 1, 4)
type(t)

# eleman seçme

birinci = t[0]
dorduncu = t[3]

######################################################################################
# Set (Küme işlemleri)
######################################################################################

# Değiştirilebilir
# Sırasız + Eşsiz
# Kapsayıcıdır

set1 = set([1, 2, 3])
set2 = set([4, 2, 6])

type(set1)

# set1 de olup set2 de olmayanlar (iki kümenin farkı)

set1.difference(set2)
set1 - set2
# set2 de olup set1 de olmayanlar

set2.difference(set1)
set2 - set1
# İki kümenin de birbirinde olmayanlar

set1.symmetric_difference(set2)
set2.symmetric_difference(set1)

# İki kümenin kesişimi

set1.intersection(set2)
set2.intersection(set1)

# İki kümenin birleşimi

set1.union(set2)
set2.union(set1)

# İki kümenin kesişi mi boş mu değil mi sorgulama

set1.isdisjoint(set2)
set2.isdisjoint(set1)

# Bir küme diğer kümenin alt kümesi mi sorgulama

set1.issubset(set2)
set2.issubset(set1)

# Bir küme diğer kümeyi kapsıyor mu sorgulama

set1.issuperset(set2)
set2.issuperset(set1)

name = "VBO_Bootcamp"
typee = "new.term"

f"Name:{name} type : {typee}"

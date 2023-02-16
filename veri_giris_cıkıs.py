############################################################################
# Python Veri Giriş ve Çıkış Komutları
############################################################################

# Ekrana klavyeden girilen belirli bir mesajı yazdırmak için "input" kullanılır.
age = int(input('What is you age?'))
name = str(input("What is you name?"))
height = float(input("what is you height?"))

# Ekrana yazdırmak için "print" kullanılır.

print('sevde')
print("sevde")
print("""sevde""")

# "sep" parametresi yazdırılan verilerin hangi karakterle ayrılacağını belirtir.

print("sevde", "karabacak", sep="-")
print("Sevde", "Karabacak", "İstanbul", "21", sep="-")

# \n Alt satıra geçer ve \t boşluk bırakarak devam eder.
print("Sevde Karabacak\nİstanbul\t21")
print("Sevde", "\tKarabacak", "\tİstanbul", "\t21", sep="   ")
print("Sevde", "\tKarabacak", "\nİstanbul", "\t21", sep="   ")

# "end" parametresi verilerin sonuna gelecek karakteri belirler.

print("Sevde", "Karabacak", "İstanbul", "21", sep=",", end=".")

# format kullanımı

a = "sevde"
b = "karabacak"
c = "21"

print("name: {},\nsurname: {},\nage: {}".format(a, b, c))
print("name: {0},surname: {1},age: {2}".format(a, b, c))


########################################################################################################


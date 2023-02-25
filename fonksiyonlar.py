########################################################################################
# FONKSİYONLAR
########################################################################################

# print fonksiyonunun argümanlarına bakalım

print("a")

help(print)


# tek argümanlı fonksiyon tanımlayalım

def calculate(i):
    print(i * 2)


calculate(8)


# iki argümanlı fonksiyon tanımlayalım

def summer(var_1, var_2):
    print(var_1 + var_2)

    summer(3, 4)


##################################################
# Docstring (Fonksiyona bilgi notu ekleme)
##################################################

def sum_one(deg1, deg2):
    """
    Sum of two numbers
    Args:
        deg1: int,float
        deg2: int,float

    Returns:
        deg1: int,float
        deg2: int,float
    """

    print(deg1 + deg2)


help(sum_one)


##################################################
# Fonksiyonların Statement/Body Bölümü
##################################################

def say_hi():
    print("Merhaba")
    print("Hello")
    print("Hi")

    say_hi()


def say_hii(string):
    print(string)
    print("Hello")
    print("Hi")

    say_hii("sevde")


def multiplication(bir, iki):
    end = bir * iki
    print(end)

    multiplication(10, 9)


# Girilen iki sayıyı çarpıp değerlerini bir liste içinde saklayan fonksiyon

list_one = []


def list_cal(h, j):
    u = h * j
    list_one.append(u)
    print(list_one)


list_cal(1, 4)


##################################################
# Ön tanımlı argümanlar/parametreler
##################################################

def divide(t1, t2):
    print(t1 / t2)

    divide(46, 3)


def adivide(a1, a2=1):
    print(a1 / a2)

    adivide(46)


def say_data(name="Kuzey"):
    print(name)
    print("Hi!")


say_data()


##############################################################
# Return: Fonksiyon çıktılarını girdi olarak kullanma
##############################################################

def cal(b1, b2, b3):
    return (b1 + b2) / b3


cal(3, 7, 2) * 10


def cal_change(aa, bb, cc):
    aa = aa * 2
    bb = bb * 2
    cc = cc * 2
    var = (aa + bb) / cc

    return aa, bb, cc, var


cal_change(3, 7, 2)

aa, bb, cc, var = cal_change(3, 7, 2)


#########################################################################
# Fonksiyon içinden fonksiyon çağırmak
#########################################################################

def calculus(s, d, f):
    return int((s + d) / f)


calculus(90, 12, 12)


def standardization(var1, var2):
    return var1 * 10 / 100 * var2 * var2


standardization(45, 1)


def all_calculus(s, d, f, var2):
    var1 = calculus(s, d, f)
    t = standardization(var1, var2)
    print(t * 10)


all_calculus(1, 3, 5, 12)

############################################################
# Local ve Global Değişkenler
############################################################

# Fonksiyonun içinde tanımlanan değişkenlere LOKAL DEĞİŞKENLER, 
# fonksiyonun dışında tanımlanan değişkenlere GLOBAL DEĞİŞKENLER adı verilir.

list_store = [1, 2]


def add_element(number1, number2):
    finish = number1 * number2
    list_store.append(finish)
    print(list_store)


add_element(1, 9)


#################################################################################################

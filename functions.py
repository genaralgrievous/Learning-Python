def hello_name (name):
    print("hello")
    print(name)

hello_name("can")
'''
hello
can
'''

# Fonksiyonlardaki parantezlerin icine parametleri yazarak  ornekteki gibi
#kullanabiliriz.Ancak eger fonksiyona parametre girmezsek hata verir
#Istersek parametreye sabit bir deger atayip hata vermemesini saglayabiliriz.

def hello_surname(surname = "aydogan"):
    print("hello")
    print(surname)

hello_surname()
'''
hello
aydogan
'''

# Bu sekilde fonksiyonlardan input alabiliriz.


def summation (num1,num2):
    result = num1+num2
    print(result)
    return result

x = summation(456,8979)
'''
9435
'''
#return fonksiyondan buldugumuz degerleri yeni degiskenlere atamamizi saglar . Eger return kullanmazsak python x degerini hatirlamaz.
#ayrica return kod blogunun sonuna yazilir cunku bilgisayar return'dan sonra kodlari okumayi birakir .


###
def string_kontrolu(s):
    if s[0] == "a":
        print("aaaaaaa")
    else:
        print(":(")

string_kontrolu("atil")
'''
aaaaaaa
'''
string_kontrolu("can")
'''
:(
'''


### args , kwargs

def toplam (*args):
    return sum(args)

toplam(12,34,45,56,67,78,89,90)

print(toplam(12,34,45,56,67,78,89,90)
)
'''
471
'''

def kwargs_ex (**kwargs):
    print(kwargs)

kwargs_ex(apple=100,banana= 354,pear=545,watermelon=798)
'''
{'apple': 100, 'banana': 354, 'pear': 545, 'watermelon': 798}
'''
# arg'lar bize fonksiyon icine istedigimiz kadar parametre yazmamizi saglar.
# kwargs'lar ise fonksiyon icine yazdigimiz parametleri bize bir sozluk olarak dondurur.Ancak bir sozlugun methodlarini
#kullanamazsin (.keys, .values gibi)














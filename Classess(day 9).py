###CLASS
class Person():
#Property (ozellikler)
    #name
    #age
    #gender
    job = ""
# Siniflar buyuk harfle yazilir.
# Sinifin ozelliklerini yukaridaki gibi yazmamiza gerek yok init altina yazdigimizda python anliyor.Eger ozelligin zorunlu
#verilmesini istemiyorsak yukaridaki gibi bos birakabiliriz.
    def __init__(self,age,name,gender):
        self.age = age
        self.name = name
        self.gender = gender
#Sinif cagrildiginda ne olmasini istiyorsak init ile yapariz (sinifi cagirdiginda parametlerin girilmesini zorunlu kilmak gibi).

    def print_name(self):
        print(self.name)

#self sinifin kendisine , sinifin icindeki degistirmek istedigimiz ozelliklere parametlere referans veriyor.

can = Person("can",67,"male")

can.job = "developer"
can.job


###Sinif ornekleri

# Kopegin yasini degistirmek gibi bir ozellik eklemek istiyorsak bunun 2 yonten kullanilabilir.

class Dog():
    year = 10

#1.'si init'in altina ayri bir ozellik olarak eklenebilir.
#init kullancidan sadece bi sey isteme araci degil her obje olusturuldugunda cagrilacak method.
#Bu yuzden init'i bu sekilde kullanilabilecegi unutulmamali.

    def __init__(self, age=5):
        self.age= age
        self.dog_human_age = age * self.year

    # veya ayri bir method eklenebilir.

    def human_age(self):
        return self.age * self.year  # istersen Dog.year de yazılabilir.

myDog = Dog()
print(myDog.dog_human_age)
print(myDog.human_age())

























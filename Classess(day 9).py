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
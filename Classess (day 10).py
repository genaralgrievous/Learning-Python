###INHERITANCE
from tkinter.font import names


class Musician ():
    def __init__(self,name):
        self.name=name

    def test1(self):
        print("test1")

    def test2(self):
        print("test2")

can = Musician("can aydogan")
print(can.name)
print(can.test1())


class Super_musician(Musician):
    def __init__(self,name):
        Musician.__init__(self,name)
        print("super musician")


    def test1(self):
        print("test1, test1,test1")

mehmet = Super_musician("mehmet aydogan")
mehmet.test1()

#Baska bir siniftan aktarmak istedigimiz methodlar icin :
'''
class Super_musician(Musician):
    def __init__(self,name):
        Musician.__init__(self,name)
'''
# bu sekilde bir yapi kullanilir.Ayrica yeni sinifin icinden eski sinifa ait methodlari degistirebiliriz.
#Bu methodlari degistirdiginde eski siniftaki methodu cagirirsan eski hali gelir , yeni halini cagirirsan yeni hali gelir.

'''
can.test1()
test1

mehmet.test1()
test1, test1,test1
'''
###POLYMORPHISM
#polymorphism ayni isimli ama farkli islevlere sahip olabilen methodalara , ayni anda calistirilabilmesine denir.

class Banana ():
    def __init__(self,name):
        self.name=name

    def info(self):
        return f"150 calorie {self.name}"


class Apple ():
    def __init__(self, name):
        self.name = name

    def info(self):
        return f"200 calorie {self.name}"

apple = Apple("apple")
banana = Banana("banana")

print(banana.info())
print(apple.info())

'''
150 calorie banana
200 calorie apple
'''

fruitList =[apple,banana]

for fruit in fruitList:
    print(fruit.info())

'''200 calorie apple
150 calorie banana'''

#bu sekilde farkli siniflardaki ayni isimdeki methodlari cagirabiliriz.


###ENCAPSULATION (HAPSETMEK)
#encapsulation prensibi bize yazdigimiz kodlarin degistirilememesini vurgular.

class Phone():
    def __init__(self,name,price):
        self.name=name
        self.__price=price

    def info (self):
        print(f"{self.name}'s price is {self.__price}")

    def changeInfo (self,price):
        self.__price =price

iphone= Phone("iphone",500)
print(iphone.info())
iphone.changeInfo(899)
'''
iphone's price is 500
'''

#self.__price=price bu formati kullanarak (iki alt cizgi ile) parametreleri sadece sinifin icinden degistirebilir hale
#getirebiliriz.Eger degistirmek istersek changeprize methodu kullanilarak degistirilebilir.













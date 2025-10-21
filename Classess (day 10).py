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

###ABSTRACTION(SOYUTLAMA)
#Abstraction bir kalip olarak kullanilan siniflardir.

from abc import  ABC , abstractmethod

class Car (ABC):

    @abstractmethod
    def maxSpeed(self):
        pass


class Tesla (Car):

    def maxSpeed(self):
        print(200)



class Mercedes (Car):

    def maxSpeed(self):
        print(300)

myTesla = Tesla()
myMercedes = Mercedes()

print(myMercedes.maxSpeed())
print(myTesla.maxSpeed())

'''
300
200
'''
#Abstract sinif kullanmak icin 'from abc import  ABC , abstractmethod' satirini importlamamiz lazim ikinci olarak
#Abstract edecegimiz sinifin icine ABC'yi methodunu inherit ederiz. class Car (ABC):
# Method yazarken de su yapiya dikkat etmeliyiz.
'''
@abstractmethod
    def maxSpeed(self):
'''

#Son olarak diger siniflari olustururken (Tesla , Mercedes ) kalip olarak olusturdugumuz sinifin icindeki methodlari
# bulundurmak zorunda (maxSpeed) yoksa hata verir.



###Special Methods

class Fruit():

    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

    def __str__(self):
        return f"{self.name}: {self.calories} calories"

    def __len__(self):
        return self.calories


#Istersek bir sinifin icerisine __as__ ile ozel bir method yazabiliriz ancak bunun icin bu ozel methodlarin ismini bilmek
#gerekiyor.
#Bir nevi init gibi sinif cagrildiginda bazi ozel fonksiyonlar cagiriyoruz.

myFruit = Fruit("banana", 150)
myFruit.calories
'''150'''

myFruit.name
'banana'

print(myFruit)

'''banana: 150
calories'''

myList = [10, 20, 30]
len(myList)
3
len(myFruit)
150


class Train():

    def __init__(self, name):
        self.name = name

    def __getitem__(self, key):
        if key == "a":
            return self.name
        else:
            return "Not found"


myTrain = Train("myTrain")
myTrain["a"]
'myTrain'
myTrain["b"]
'Not found'



















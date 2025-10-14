def divide_number (number):
    return number/2

print(divide_number(78))

my_list = [3,5,7,10,20,30]
new_list = []

'''
for num in my_list:
    divide_number(num)
    new_list.append(divide_number(num))
'''

print(new_list)

###MAP
list(map(divide_number,my_list))
print(list(map(divide_number,my_list)))

#map sayesinde yukaridaki for loop'a gerek kalmadan istedigimiz fonksiyonu istedigimiz listenin her elemanina uygulaya
#biliriz.map(fonksiyon,koleksiyon)

###FILTER

def string_control (string):
    return "can" in string

print(string_control("can aydogan"))
'''
True
'''

name_list = ['can','aydogan','mehmet','can sungur']
print(list(filter(string_control,name_list)))
'''
['can', 'can sungur']
'''

#filter fonksiyonu sayesinde bir liste icerisinden istedigimiz elamanlari fonksiyondan gecirip tutabiliriz.


###LAMBDA
divide_lambda = lambda num : num/7
print(divide_lambda(78))
'''
11.142857142857142
'''
# Bu sekilde kisa yoldan anonim fonksiyonlar olusturulabilir.

print(list(map(lambda sayi:sayi/17,my_list)))
'''
[0.17647058823529413, 0.29411764705882354, 0.4117647058823529, 0.5882352941176471, 1.1764705882352942, 1.7647058823529411]
'''

###LEGB -> L->Local, E-> Enclosing, G->Global, B->Built - In
# Global
myString = "Atıl"


def myFunction():
    # Enclosing
    myString = "Atıl 2"
    print(myString)

    def myFunction2():
        # Local
        myString = "Atıl 3"
        print(myString)

    myFunction2()
'''  
myString
'Atıl'

myFunction()
Atıl 2
Atıl 3

myString
'Atıl'
'''

y = 10
def newFunction(y):
    print(y)
    y = 5
    print(y)
    return y
newFunction(10)
'''
10
5
5
y
10
y = 10
'''
#
def changeY():
    global y
    y = 5
    print(y)
changeY()
'''
5
y
5
'''
#Istersek fonksiyonun icinden global y'nin degerini degistirebiliriz.


def test1():
    myX= 10
    print(myX * 2)
'''
def test2():
    print(myX * 3)
test1()
20
'''
#Yukaridaki fonksiyonlarin scope'lari farkli oldugu icin test2 fonksiyonu calismayacak.


















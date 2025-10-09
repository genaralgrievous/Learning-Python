from numpy.random import randint, shuffle

for num in list(range(10)):
    print(num)
'''
0
1
2
3
4
5
6
7
8
9
'''
#Range fonksiyonu belirlenen araliktaki sayilari yazdirir
#Istersek range (5,37,4) seklinde indexing'de yapilabilir
# (5'ten 37'ye dorter dorter say).

new_list = [10,20,30,40,50]
for x in range(len(new_list)):
    print(x)
# Bir listedeki elemanlarin indexlerini yazdirmak istersek kullanabiliriz.

### Enumerate

for element in enumerate(new_list):
    print(element)

#enumarate listedeki elemanlari indexleri ile beraber bir tuple olusturur.
'''
(0, 10)
(1, 20)
(2, 30)
(3, 40)
(4, 50)
'''
for (ix,value) in enumerate(new_list):
    print(ix)

'''
0
1
2
3
4
'''
# Istersek sadece index yada degerleri'de alabiliriz.

###randint

randint(0,100)
# randint bir araliktaki rastgele bir sayi secer.

###shuffle
shuffle(new_list)
print(new_list)

#shuffle listeyi karistirir.


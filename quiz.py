

my_dictionary = {"k1":10,"k2k":"a","k32":30,"k4":"c"}

if "c" in my_dictionary.values():
    print("u")



r_list = [3,2,5,8,4,6,9,12]
cevre_list= []
for r in r_list:
    cevre_list.append(2*r*3.14)
print(cevre_list)


age_name_list = [("Ahmet",30),("Ayse",24),("Mehmet",40),("Fatma",29)]

yas_list = []
for (x,y) in age_name_list:
    yas_list.append(y)

print(yas_list)


from random import randint
metal_list = ["Metallica","Iron Maiden","Dream Theater","Megadeth","AC/DC"]
###

#Bir listeden random eleman secmek istedigimizde asagidaki satiri kullanabiliriz.
print(metal_list[randint(0,len(metal_list)-1)])

###



number_list = [5,7,18,21,20,10,405,24]
print([num % 2 == 0 for num in number_list])

"""[False, False, True, False, True, True, False, True]"""
#Listedeki sayilari cift mi degil mi kontrol ediyor
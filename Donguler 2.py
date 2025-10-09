my_list2 = [10,20,30,40,50,60,70]

for num in my_list2 :
    if num % 6 == 0:
        print(num)
# For ve diger donguler senin verdigin degeri liste icinde bulunan her bir degere atar ve buna gore islem yapmani veya
#listeyi ayiklamana yardimci olur

tuple_list = [(1,2),(3,4),(5,6)]
for (x,y) in tuple_list:
    print(x)
# Tuple unpacking yaparak iceriden istedigimiz degeri alabiliriz hatta x,y,z seklinde 3 lu tuple larda bile olur.

### Break Continue , Pass

for number in my_list2:
    print(number)
    if number == 40:
        print("yes")
        break
'''10
20
30
40
yes'''
#Break donguleri bitirmek icin faydali , kodlarin daha verimli olmasini saglar . 40 'tan sonrasini yazdirmayarak kod daha
#verimli hale geldi

for number in my_list2:
    if number == 40:
        continue
    print(number)

'''10
20
30
50
60
70'''
#Continue ile dongude istemedigimiz yeri atlayarak devam etmemizi sagladi.


for num in my_list2:
    pass

### while
x = 0
while x<10:
    print("x is smaller than 10")
    x = x+1 # veya x += 1 seklinde'de yazilabilir

#Formatted string
name = "can"
print(f"my name is {name}")

print("welcome",name)
# Gosterilen sekilde print in icine istedigimiz degiskenleri yazabiliriz.

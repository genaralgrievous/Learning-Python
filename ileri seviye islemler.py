
###zip
food_list = ["apple","banana","pear"]
calorie_list = [150,300,340]
day_list =["monday","tuesday","wednesday"]

diet_list = list(zip(food_list,calorie_list,day_list))

#[('apple', 150, 'monday'), ('banana', 300, 'tuesday'), ('pear', 340, 'wednesday')]
#zip listeleri birlestirip yukaridaki sekilde saklamani saglar
print(diet_list)



number_list = [30,40,50,60,70]
empty_list = []
for num in number_list:
    empty_list.append(num) # ayrica num\2 veya baska bir islem uygulayarak yeni listeye gelecek elemanlari degistirebiliriz
print(empty_list)
#[30, 40, 50, 60, 70]
#Bir listedeki elemanlari hepsini aktarmak istiyorsak yukaridaki gibi bir dongu kullanilabilir.




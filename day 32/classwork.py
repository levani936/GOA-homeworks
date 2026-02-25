#list-ს აქვს ინდექსი, დალაგებულია და mutable-ა.
#set-ს არ აქვს ინექსი, დაულაგებელია, მაგრამ mutable-ა
#tuple-ს აქვს ინდექსი, დალაგებულია მაგრამ immutable-ა.


#.add() ამატებს ელემენტს სიმრავლეში.
#.update() რამდენიმე ელემენტს ამატებს სიმრავლეში.
#.remove() შლის ელემენტს სიმრავლიდან დასახელებით. თუ სიმრავლეში მითითებული ელემენტი არ არის აგდებს error-ს.
#.discard() შლის ელემენტს სიმრავლიდან მაგრამ error-ს არ აგდებს.
#.union() აერთიანებს ორ სიმრავლეს ერთში.


group1 = {"idk1", "idk2", "idk3", "idk4"}
group2 = {"sth1", "sth2", "sth3", "sth4"}

group1.add("idk5")
print(group1)
group2.update("sth5", "sth6", "sth7")
print(group2)

group1.remove("idk2")
print(group1)

group2.discard("sth1")
print(group2)

group3 = group1.union(group2)
print(group3)


numbers = (1, 2, 1, 4, 8, 4, 1, 5)
print(numbers[3], numbers[7])
print(numbers[2 : 7])

count = len(set(numbers))
print(count)

numbers = tuple(numbers)
print(numbers[4])

num2 = (4, 6 ,4 ,7 ,8, 9, 11)
union = (numbers + num2)

listtuple = list(numbers)
numbers.append(12)
numbers = tuple(numbers)
print(numbers)




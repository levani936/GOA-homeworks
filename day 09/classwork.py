#ლოგიკური ოპერატორები ამოწმებენ დაწერილ კოდს სრულყოილია თუ არა.
#and ოპერატორი ამოწმებს ყველაფერია კოდში ზუსტად თუ არა.თუ არარის მაშინვე false-ია.
#or ოპერატორი გვაძლევს ვარიანტს,ანუ ან პირველი კოდი უნდა იყოს გაეთებული ან მეორე.

name = "ixvi"
print(name == "ixvi")

number = 51
print(number == 50)

fav_toy = "toygun"
print(fav_toy == "toygun")

# True and False and True or False and True and False True and False and True and False and True and False = False
print(True and False and True or False and True and False and True and False and True and False and True and False )

print(50 > 45)
print(90 > 78)
print(78 <= 79)
print(90 >= 90)
print(69 == 69)

ingredient1 = "meat"
ingredient2 = "tomato"
print(ingredient1 >= "meat" and ingredient2 >= "lettuce")
print(ingredient1 >= "bread" or ingredient2 >= "tomato")
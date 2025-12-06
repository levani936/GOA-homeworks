#slicing არის მაგალითად list-ის ორ ნაწილად გაყოფა.
#indexing არის მონაცემთა დანომრვა,რომელსაც თვითონ კოდი აკეთებს.

#ფუნქცია python-ში არის კოდი,რომლის მეშვეობით ვმოქმედებთ კოდში,და ასევე კოდის შემოკლებული ფორმა.
#მაგ:  print(type("hello")),input((int)"hello")...

C = ["$","€","£", "¥", "W", "P", "J", "N" ]
print(C[-5:-2])
print(C[-4:-1])
print(C[::-1])
print(C[::2])

name_and_surname = "Levan Bedoshvili"
lastfour = print(name_and_surname[1:5])
firstthree = print(name_and_surname[6:9])

names = ["Sandro", "Davit", "Lazare", "Giorgi", "Luka", "Andria"]
names[4] = "Levani"
print(names[4])
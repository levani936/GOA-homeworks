#for loop გამოიყენება რაიმე სიტყვის ან ციფრის იმდენჯერ გამეორებისთვის, რამდენსაც მივუთითებთ.
for i in range(5):
    print("Hello")

#while loop გამოიყენება რაიმის დაწერაში,სანამ იგი სწორი აღარ იქნება.
while i < 10:
    print(i)

#indendation არის შედგენა ან ჩამოწევა კოდის ხაზის.
# პითონში Indentation აუცილებელია იმისთვის, რომ კომპიუტერმა გაიგოს რომელი კოდი ეკუთვნის ციკლს, ფუნქციას ან სხვა ბლოკს.

# % არის მათემატიკური ოპერატორი
# ის აბრუნებს ნაშთს გაყოფისას.

for i in range(0, 50, 2):
    print(i)

for i in range(10):
    print("Levani")

for i in range(1, 67):
    print(i)


i = 0
while i < 10:
    print("Levani")
    i += 1  


my_fav_num = 7

user_number = int(input("67"))

while user_number < my_fav_num:
    print("hello world!")
    user_number = int(input("67"))

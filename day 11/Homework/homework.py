
# for ციკლი გვეხმარება ერთიდაიგივე რაღაცის რამდენჯერმე გაკეთებაში.
# მაგ: თუ გვინდა რომ რამე 5-ჯერ დავბეჭდოთ, ხელით არ ვწერთ 5-ჯერ, ვიყენებთ for-ს.

for i in range(5): 
    print("გამარჯობა!")  

for x in range(3): 
    print("ეს ციკლია!", x)  


for i in range(1, 101): 
    print(i)

for i in range(1, 100, 5):  
    print(i)


for i in range(5, 88):  
    if i % 2 == 0: 
        print(i)


name = input("შეიყვანე შენი სახელი: ")
for i in range(15):  
    print(name)

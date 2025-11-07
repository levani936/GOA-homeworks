
age = int(input("Please enter your age:"))

if age == 18:
    print("You can go for voting!")
else:
    print("You cant go for voting!")

number = int(input("შეიყვანეთ რიცხვი:"))

if number % 2 == 0:
    print("ეს რიცხვი ლუწია.")
else:
    print("ეს რიცხვი კენტია.")

cars = ["BMW", "Mercedes", "Toyota", "Honda", "Ford"]

first = cars[0]
last = cars[-1]

print("პირველი მანქანა:", first)
print("ბოლო მანქანა:", last)

print("პირველი ასოები:", first[0], and last[-1])

numbers = [1,2,3,4,5,6,7,8,9,10]

print("მხოლოდ ლუწი რიცხვები:")
for num in numbers:
    if num % 2 == 0:
        print(num)

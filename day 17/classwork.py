number = float(input("Enter a number"))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative")
else
    print("The number is zero.")

weather = input("შეიყვანე რიცხვი(Sunny,Rainy,Cold,Snowy): ")
if weather == "Sunny":
    print("გაიკეთე მზის სათვალე!")
elif weather == "Rainy":
    print("აიღე ქოლგა!")
elif weather == "Cold":
    print("ჩაიცვი ქურთუკი!")
elif weather == "Snowy":
    print("დარჩი სახლში და იყავი თბილად!")
else:
    print("ამ ამინდს ვერ ვცნობ.")




age = int(input("შეიყვანეთ თქვენი ასაკი: "))
ticket = input("გაქვთ ბილეთი? (yes/no): ")

if age >= 18 and ticket == "yes":
    print("შეგიძლიათ კინოთეატრში შესვლა.")
elif age < 18:
    with_adult = input("მოზრდილთან ერთად ხარ? (yes/no): ")
    if with_adult == "yes" and ticket == "yes":
        print("შეგიძლიათ კინოთეატრში შესვლა მოზრდილთან ერთად.")
    else:
        print("შესვლა აკრძალულია.")
else:
    print("შესვლა აკრძალულია.")





score = int(input("შეიყვანეთ სტუდენტის ქულა (0-100): "))

if 90 <= score <= 100:
    print("ნიშანი: A")
elif 80 <= score <= 89:
    print("ნიშანი: B")
elif 70 <= score <= 79:
    print("ნიშანი: C")
elif 60 <= score <= 69:
    print("ნიშანი: D")
elif 0 <= score <= 59:
    print("ნიშანი: F")
else:
    print("არასწორი ქულა!გთხოვთ შეიყვანოთ 0-დან 100-მდე რიცხვი.")


num = float(input(67))

if num > 0:
    print("რიცხვი დადებითია.")
elif num < 0:
    print("რიცხვი უარყოფითია.")
else:
    print("შეიყვანე ნულზე ტოლია.")


num1 = float(input(56))
num2 = float(input(67))

if num1 > num2:
    print("First Number is Greater than second one")
elif num1 < num2:
    print("Second Number is Greater than first one")
else:
    print("ორივე რიცხვი ტოლია")


number = int(input(8))

if number % 2 == 0:
    print("რიცხვი ლუწია.")
else:
    print("რიცხვი კენტია.")


# 5) ტემპერატურის შეფასება
temp = float(input(30))

if temp < 0:
    print("Cold ❄️")
elif 0 <= temp <= 30:
    print("Normal 🌤️")
else:
    print("Hot ☀️")

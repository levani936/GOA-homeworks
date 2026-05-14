# 1)

students = {
    "Giorgi": {"score": 95, "attendance": 90},
    "Nika": {"score": 88, "attendance": 85},
    "Luka": {"score": 99, "attendance": 92}
}

best_student = ""
highest_score = 0

for name in students:
    if students[name]["score"] > highest_score:
        highest_score = students[name]["score"]
        best_student = name

print("ყველაზე მაღალი ქულა აქვს:", best_student)

total = 0

for name in students:
    total += students[name]["score"]

average_score = total / len(students)

print("საშუალო ქულა:", average_score)


# 2)

products = {
    "laptop": {"price": 3000, "stock": 4},
    "phone": {"price": 1500, "stock": 10},
    "tablet": {"price": 1200, "stock": 0}
}

print("მარაგშია:")

for product in products:
    if products[product]["stock"] > 0:
        print(product)

total_value = 0

for product in products:
    total_value += products[product]["price"] * products[product]["stock"]

print("ყველა პროდუქტის ჯამური ღირებულება:", total_value)


# 3)

footballers = {
    "Messi": {"goals": 30, "assists": 12},
    "Ronaldo": {"goals": 28, "assists": 5},
    "Mbappe": {"goals": 25, "assists": 10}
}

footballers["Haaland"] = {"goals": 32, "assists": 6}

footballers["Messi"]["goals"] += 5

top_scorer = ""
most_goals = 0

for player in footballers:
    if footballers[player]["goals"] > most_goals:
        most_goals = footballers[player]["goals"]
        top_scorer = player

print("ყველაზე მეტი გოლი აქვს:", top_scorer)


# 4)

employees = {
    "Giorgi": {"salary": 2500, "position": "Manager"},
    "Nika": {"salary": 1800, "position": "Developer"},
    "Luka": {"salary": 1500, "position": "Designer"}
}

for employee in employees:
    employees[employee]["salary"] += employees[employee]["salary"] * 0.10

highest_paid = ""
highest_salary = 0

for employee in employees:
    if employees[employee]["salary"] > highest_salary:
        highest_salary = employees[employee]["salary"]
        highest_paid = employee

print("ყველაზე მაღალი ხელფასი აქვს:", highest_paid)

total_salary = 0

for employee in employees:
    total_salary += employees[employee]["salary"]

print("ყველა ხელფასის ჯამი:", total_salary)
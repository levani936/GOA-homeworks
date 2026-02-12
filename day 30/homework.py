data = ("Ana", 15, "Tbilisi")
name, age, city = data
sentence = "".join([name, "is", str(age), "years old and lives in", city])

#ეს კოდი ქმნის ფუნქციას, რომელიც აერთებს სიის ელემენტებს symbol არგუმენტით. ის აერთებს ელემენტებს $-თი და აჭრის ბოლო ზედმეტ სიმბოლოს.
def join_clone(symbol, arr):
    result = ""
    
    for i in arr:
        result += f"{i}{symbol}"
    
    return result[:-1]

print(join_clone("$", ["nika", "vano", "giorgi"]))
print("$".join(["nika", "vano", "giorgi"]))

#ეს ფუნქცია აკეთებს იმას, რასაც split აკეთებს:ის ანცალკევებს სიის ელემენტებს ,-ით.
def split_clone(str, symbol):
    result = []
    test = ""
    
    for i in str:
        if i != symbol:
            test += i
        else:
            result.append(test)
            test = ""

    result.append(test)
    return result

print(split_clone("gamarjoba rogor xar", " "))
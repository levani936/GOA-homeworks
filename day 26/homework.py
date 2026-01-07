#ფუნქცია არის კოდის ბლოკი,რომელსაც აქვს საკუთარი სახელი და დანიშნულება.
#Python-ში costum ფუნქციას ვქმნით def(define)-ით და პარამეტრებით.

def count_even_numbers(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1
    return count
nums_list = [2, 3, 4 ,5 , 6, 7 ,8, 9, 10]
result = count_even_numbers(nums_list)
print(result)

def greet(Name, Surname):
    print("Hello", (Name), (Surname))
greet("Levan", "Bedoshvili")

def even_or_not(number):
    if number % 2 == 0:
        return True
    else:
        return False    

#return აბრუნებს ფუნქციიდან მნიშვნელობას ან ასრულებს ფუნქციის შესრულებას,ხოლო print უბრალოდ ტერმინალში უშვებს კოდს.


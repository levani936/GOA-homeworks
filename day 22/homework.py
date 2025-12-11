surname = ["b","e","d","o","s","h","v","i","l","i"]
counter = 0

for letter in surname:
    print(letter)
    counter += 1
print("იტერაციების რაოდენობა :", counter)

name = input("შეიყვანეთ თქვენი სახელი:")
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name[::-1].upper())
print(name.swapcase())
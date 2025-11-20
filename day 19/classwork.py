fruits = ["apple", "banana", "orange", "grapes"]
print(fruits[0])
print(fruits[-1])
fruits = fruits + ["mango"]
fruits[2] = "kiwi"

numbers = [1 ,2 , 13 , 21 , 67, 69 , 59]
print(numbers[:3])
print(numbers[-2:])
print(numbers[2:5])
print(numbers[::2])

surname = "Bedoshvili"
reversed = surname[::-1]
print(reversed)

#slicing-ს ვიყენებთ რათა list-ებში და string-ებში გარვვეული ნაწილები ამოვიღოთ ან სხვა list შევქმნათ.
#mutable ნიშნავს როცა list-ში შეგვიძლია რაიმე ელემენტი შევცვალოთ.

numbers = [3, 5, 89, 1, 10, 67, 80]
odd_sums = 0
for n in numbers:
    if n % 2 != 0
    odd_sums += n
print(odd_sums)


string = input("Enter a word:")
print(string.upper())
print(string.lower())

string2 = "hello"
print(string2.__len__)

nums = [1, 2, 5, 67, 12, 10, 8]
nums.append(42)
nums.pop(6)
print(nums)

fruits = ["apple", "banana", "apple", "orange"]
count = 0

for item in fruits:
    if item == "apple":
        count += 1

input = input()
print(input.swapcase())

nums.remove(67)
print(nums)

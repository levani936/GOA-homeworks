letters = ['a','b','c','d','e','f','g','h']

print(letters[:4])

print(letters[2:6])

print(letters[::2])

print(letters[::-1])

nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

nums[-2:] = [777, 888]
print(nums)

numbers = list(range(1, 21))
even_sum_list = []

even_sum = sum([n for n in numbers if n % 2 == 0])
even_sum_list = [even_sum]

print(even_sum_list)

nums = [1,2,3,4,5,6,7,8]

middle_four = nums[2:6]
last_three = nums[-3:]

print(middle_four)
print(last_three)

letters = list("abcdefghij")
result = letters[1::2]
print((result))

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for n in nums:
    if n % 2 == 0:
        print(n, "Your Number is even")
    else:
        print(n, "Your Number is Odd")

list_2 = [1, 2, 3, 2, 1]

if list_2 == list_2[::-1]:
    print("list is a palindrome")
else:
    print("list is not a palindrome")

mix = [10, "hello", 3.14, 2.71, "test", 5, 9.8]

floats = [x for x in mix if type(x) == float]
print(floats)

numbers = [1,2,3,4,5,6,7,8,9,10]

numbers.sort(reverse=True)
print(numbers)







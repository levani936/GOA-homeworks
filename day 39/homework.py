# 1 - https://www.codewars.com/kata/576b93db1129fcf2200001e6/train/python

def sum_array(arr):
    if arr is None or len(arr) < 3:
        return 0
    return sum(arr) - min(arr) - max(arr)


# 2 - https://www.codewars.com/kata/5861d28f124b35723e00005e/train/python

def zero_fuel(distance_to_pump, mpg, fuel_left):
    return fuel_left * mpg >= distance_to_pump


# 3 - https://www.codewars.com/kata/56b1f01c247c01db92000076/train/python
def double_char(s):
    return ''.join(c * 2 for c in s)


# 4 - https://www.codewars.com/kata/55eca815d0d20962e1000106/train/python
def generate_range(start, stop, step):
    result = []
    current = start
    
    while current <= stop:
        result.append(current)
        current += step
        
    return result


# 5 - https://www.codewars.com/kata/55a5befdf16499bffb00007b/train/python
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b  # or a // b for integer division

def mod(a, b):
    return a % b

def exponent(a, b):
    return a ** b

def subt(a, b):
    return a - b


# 6 - https://www.codewars.com/kata/55a5bfaa756cfede78000026/train/python

def problem(a):
    if type(a) == str:
        return "Error"
    return a * 50 + 6
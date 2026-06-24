#7 kyu
# https://www.codewars.com/kata/546e2562b03326a88e000020/train/python

def square_digits(num):
    result = ""
    
    for digit in str(num):
        result += str(int(digit) ** 2)
        
    return int(result)


#7 kyu
# https://www.codewars.com/kata/554b4ac871d6813a03000035/train/python

def high_and_low(numbers):
    nums = list(map(int, numbers.split()))
    return f"{max(nums)} {min(nums)}"


#7 kyu
# https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/python

def filter_list(l):
    return [x for x in l if type(x) == int]


#7 kyu
# https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/python

def accum(s):
    return "-".join(char.upper() + char.lower() * i for i, char in enumerate(s))



#8 kyu
# https://www.codewars.com/kata/5265326f5fda8eb1160004c8/train/python

def number_to_string(num):
    return str(num)


#8 kyu
# https://www.codewars.com/kata/5715eaedb436cf5606000381/train/python

def positive_sum(arr):
    return sum(x for x in arr if x > 0)


#8 kyu
# https://www.codewars.com/kata/55685cd7ad70877c23000102

def make_negative( number ):
    if number > 0:
        return -number
    return number
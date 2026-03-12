# https://www.codewars.com/kata/57a5b0dfcf1fa526bb000118/train/python

def distinct(seq):
    result = []
    for i in seq:
        if i not in result:
            result.append(i)
    return result


# https://www.codewars.com/kata/559d2284b5bb6799e9000047/train/python

def add_length(str):
    result = []
    str = str.split(" ")
    for i in str:
        result.append(f"{i} {len(i)}")
    return result


# https://www.codewars.com/kata/52ceafd1f235ce81aa00073a/train/python

def plural(n):
    if n == 1:
        return False
    else:
        return True


# https://www.codewars.com/kata/559ac78160f0be07c200005a/train/python

def name_shuffler(str):
    str = str.split(" ")
    return " ".join(str[::-1])


# https://www.codewars.com/kata/56f699cd9400f5b7d8000b55/train/python

def fix_the_meerkat(arr):
    return arr[::-1]


# https://www.codewars.com/kata/50654ddff44f800200000007/train/python

def solution(a, b):
    if len(a) > len(b):
        return b + a + b
    return a + b + a


# https://www.codewars.com/kata/50ee6b0bdeab583673000025/train/python

a = "code"
b = "wa.rs"
name = a + b


# https://www.codewars.com/kata/58ca658cc0d6401f2700045f/train/python

def find_multiples(n, limit):
    result = []
    x = n
    while n <= limit:
        result.append(n)
        n += x
    return result


# https://www.codewars.com/kata/53da6d8d112bd1a0dc00008b/train/python

def reverse_list(l):
    return l[::-1]


# https://www.codewars.com/kata/59342039eb450e39970000a6/train/python

def odd_count(n):
    return n // 2
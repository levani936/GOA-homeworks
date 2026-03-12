# https://www.codewars.com/kata/563e320cee5dddcf77000158/train/python

def get_average(marks):
    return int(sum(marks) / len(marks))


# https://www.codewars.com/kata/53dc54212259ed3d4f00071c/train/python

def sum_array(numbers):
    total = [0]
    for n in numbers:
        total[0] += n
    return total[0]


# https://www.codewars.com/kata/50ee6b0bdeab583673000025/train/python

a = "code"
b = "wa.rs"
name = a + b


# https://www.codewars.com/kata/5a00e05cc374cb34d100000d/train/python

def reverse_seq(n):
    result = []
    for i in range(n, 0, -1):
        result.append(i)
    return result


# https://www.codewars.com/kata/596fba44963025c878000039/train/python

def contamination(text, char):
    if text == "" or char == "":
        return ""
    return char * len(text)
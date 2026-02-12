
def join_clone(symbol, arr):
    result = ""
    
    for i in arr:
        result += f"{i}{symbol}"
    
    return result[:-1]


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


sometuple = ("someone1", "someone2", "someone3", "someone4", "someone5", "someone6", "someone7")
listedtuple = list(sometuple)
idk1 = listedtuple[0:3]
idk2 = listedtuple[4:6]

nums = (1, 2, 3, 4, 5, 67, 7, 8)
strnums = list(nums)
strnums.insert(5, 12)

#asterisk აძლევს ცვლადს დანარჩენი ლისთის ყველა მნიშვნელობას.


fav_foods = ["Shawarma", "Burger", "Caesar", "Pizza", "Xinkali"]
print(fav_foods)
fav_foods.append("Mtsvadi")
fav_foods.remove("Pizza")
print(fav_foods)


nums = (1, 2, 3, 4, 5)
print(nums[1])
print(nums[-1])
nums = set(nums)
nums.discard(10)
nums = tuple(nums)


set = {1, 2, 3, 4, 4, 5}
set.add(6)
set.remove(1)
set.discard(10)
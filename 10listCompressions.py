# 	list compressions
# 	basic format: new_list = [transform sequence [filter]]

under_20 = [x for x in range(20)]
print(under_20)

squares = [x ** 2 for x in range(20)]
print(squares)

oddMul2 = [x * 2 for x in range(20) if x & 1]
print(oddMul2)

s = "m8 i love 2 go wth u b8 l8r"
nums = [x for x in s if x.isnumeric()]
print(nums)

nums2 = [5, 3, 10, 18, 6, 7]
my_list = [x if not x & 1 else 10 * x for x in nums2]
print(my_list)
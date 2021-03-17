# 	lambda -> a simple 1-line function
x = 5
mul = lambda a: 2 * a
print(mul(x))

y = 20
add = lambda x, y: x + y
print(add(y, 2))


mx = lambda a, b: a if a > b else b
print(mx(10, 20))

# 	map -> apply same function to each element of a sequence and return the modified list
n = [1, 2, 3, 4]


def cube(n):
    return n ** 3


print(list(map(cube, n)))
print(list(map(lambda x: x ** 2, n)))

# 	filter -> filters items out of sequence and returns the filtered list

n = [1, 2, 3, 4]

print(list(filter(lambda x: x >= 2, n)))

# 	reduce -> applies same operation to items of a sequence and uses the result of the operation as first param of the next operation and returns an item

import functools

n = [4, 3, 2, 1]
print(functools.reduce(lambda x, y: x * y, n))

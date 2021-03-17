# 	while loop is used when the number of iterations is not known
count = 0
while count < 9:
    print(count)
    count += 1

print("\n")

import random

n = 20
to_be_guessed = int(n * random.random()) + 1
guess = 0

while guess != to_be_guessed:
    guess = int(n * random.random()) + 1
    print(guess)

# 	for loop is used when the number of iterations is known
fruits = ["mango", "grapes", "apple"]

for fruit in fruits:
    print(fruit)

# 	pythagorean triplet
from math import sqrt

n = int(input("Maximal Number? "))

for a in range(1, n + 1):
    for b in range(a, n):
        c_sq = a ** 2 + b ** 2
        c = int(sqrt(c_sq))
        if c ** 2 - c_sq == 0:
            print(a, b, c, sep=" ,")

# 	factorial
num = int(input("Number:"))
factorial = 1

if num < 0:
    print(0)
elif num == 0:
    print(1)
else:
    for i in range(1, num + 1):
        factorial *= i

print(factorial)

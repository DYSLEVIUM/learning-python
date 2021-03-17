# 	array and list are different as in that list can store different data type elements whereas array can store only one data type elements

# three ways of importing array
# import array as arr
# from array import *
import array

a = array.array(
    "d", [1, 2, 3, 4, 5, 6]
)  # 	first array is module name, second array is constructor and it takes a typecode as in the type of data and the list of elements

print(a)
print("length is " + str(len(a)))

a.append(3.4)  # 	used to insert one element at the end
print(a)

a.insert(2, 21)  # 	used to insert one element at the index
print(a)

a.extend([132, 15, 5, 1])  # 	used to insert more than one element at the end
print(a)

a.pop(2)  # 	removes the element at index, default is -1
print(a.pop())  # 	pop function removes the element at index, and returns it
print(a)

a.remove(5)  # removes the element specified without returning it
print(a.remove(3))  # 	removes the element without returning it
print(a)

# 	array concatenation
b = array.array("d", [6, 5, 4, 3, 2, 1])
c = a + b
print(c)

# 	slicing in an array
print(c[3:5])

# 	printing reverse of an array
print(c[::-1])

# 	looping through the array
# 	using loop
for i in c:
    print(i, end=" ")

for i in c[0:-5]:
    print(i, end=" ")

print("\n")
print(list(range(len(c))), sep=", ", end="\n")

for i in range(len(c)):
    print(i, end=" ")
print("\n")

# using while
temp = 0
while temp < c[2]:
    print(c[temp])
    temp += 1

tem = 0
while tem < len(c):
    print(c[tem], end=" ")
    tem += 1

print("\n")

# 	multidimensional array
col = 2
row = 2
arr = [[[0] * col] * row]  # 	with each element value as 0
print(arr)

arr2 = []
arr2.append([1, 2, 4])
arr2.append([1, 2, [1, 1]])
print(arr2)

# taking input in multidimensional array
r = int(input())
arr = []
for i in range(r):
    arr.append([int(j) for j in input().split()])

#   This is a comment
print("Hello world")

i = 10  #   number data type
st = "sadsad"  #   string data type, strings are immutable
# z = input()  #   taking input
# z = int(input())  #   taking integer input

# print(z + 10)
# print(z[0:9]) #   string range print

fruits = ["apple", 10, "banana"]  #   list => fancy way to say array!? => No

fruits.reverse()

print(fruits[2:5])
# fruits.sort() #   to sort list must contain same data types
fruits.append(10)
fruits.insert(10, "qwqew")

print(fruits)

animals = {
    "reptiles": "snake",
    "mammals": "whale",
    "amphibians": "frogs",
    7: "10",
}  #   dictionary are is a collection that is mutable, unordered, indexed

print(animals)
print(animals.get("reptiles"))
print(animals.get(7))

animals = ("lion", "tiger", "monkey", 10, "tiger")  #   tuple is immutable
print(animals)
print(animals.count("tiger"))

myset = {10, 20, 30, 212, 10, "ste"}

print(myset)

print(range(10))

print(list(range(10)))

print(list(range(-10, 10)))


a = {1, 2, 3}
b = [123, "asd", 13]
c = [a, b]

print(c)

x = 10
y = "asdas"

# print(x+y)  # error
print(str(x) + y)

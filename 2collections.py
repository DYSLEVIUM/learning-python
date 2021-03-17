#   there are only four collection data types in python -> lists, tuples, sets, dictionary
#   also there are a collections module apart that covers for the short-comings
import collections

#   namedtuple() -> returns a tuple with a named value for each element in the tuple
#   Python supports a type of container like dictionaries called “namedtuple()” present in module, “collections“. Like dictionaries they contain keys that are hashed to a particular value. But on contrary, it supports both access from key value and iteration, the functionality that dictionaries lack.

Student = collections.namedtuple("Student", ["name", "age", "DOB"])
# Student = collections.namedtuple("Student", "name, age, DOB") #   alternate way to write

s = Student("Pushpa", 21, "idk")
s2 = Student._make(["yo", 10, "asd"])

print(s2)

print(s.name)
print(s[1])
print(getattr(s, "DOB"))
print(s._fields)
print(s._replace(name="Manjeet"))

print("The OrderedDict instance using namedtuple is  : ")
print(s._asdict())

#   Deque (Doubly Ended Queue) in Python is implemented using the module “collections“. Deque is preferred over list in the cases where we need quicker append and pop operations from both the ends of container, as deque provides an O(1) time complexity for append and pop operations as compared to list which provides O(n) time complexity.

de = collections.deque(["name", "age", "DOB"])
print(de)

de.append(40)
print(de)

de.appendleft(10)
print(de)

de.pop()
print(de)

de.popleft()
print(de)

de2 = collections.deque([1, 2, 3, 3, 4, 2, 4])

#   index(ele, beg, end) :- This function returns the first index of the value mentioned in arguments, starting searching from beg till end index.
print(de2.index(4, 2, 5))

#   insert(i, a) :- This function inserts the value mentioned in arguments(a) at index(i) specified in arguments.
de2.insert(4, 3)
print(de2)

print(de2.count(3))

de2.remove(3)
print(de2)

de2.extend([4, 5, 6])
print(de2)

de2.extendleft([7, 8, 9])
print(de2)

de2.rotate()
print(de2)

de2.reverse()
print(de2)

# 	Counter is a sub-class which is used to count hashable objects. It implicitly creates a hash table of an iterable when invoked.

# 	elements() is one of the functions of Counter class, when invoked on the Counter object will return an itertool of all the known elements in the Counter object.

x = collections.Counter("geeksforgeeks")

for i in x.elements():
    print(i, end=" ")

# Example - 2
b = collections.Counter({"geeks": 4, "for": 1, "gfg": 2, "python": 3})

for i in b.elements():
    print(i, end=" ")
print()

# Example - 3
c = collections.Counter([1, 2, 21, 12, 2, 44, 5, 13, 15, 5, 19, 21, 5])

for i in c.elements():
    print(i, end=" ")
print()

# Example - 4
d = collections.Counter(a=2, b=3, c=6, d=1, e=5)

for i in d.elements():
    print(i, end=" ")

# creating a raw data-set using keyword arguments
x = collections.Counter(a=2, x=3, b=3, z=1, y=5, c=0, d=-3)

# printing out the elements
for i in x.elements():
    print("% s : % s" % (i, x[i]), end="\n")

a = collections.Counter([1, 1, 1, 2, 3, 4, 2, 6])
print(a)
print(list(a.elements()))
print(list(a.most_common()))
print(list(a))

sub = {2: 1, 6: 2}
a.subtract(sub)
print(a)

# 	An OrderedDict is a dictionary subclass that remembers the order that keys were first inserted. The only difference between dict() and OrderedDict() is that:

# OrderedDict preserves the order in which the keys are inserted. A regular dict doesn’t track the insertion order, and iterating it gives the values in an arbitrary order. By contrast, the order the items are inserted is remembered by OrderedDict.

od = collections.OrderedDict()
od["a"] = 1
od["b"] = 2
od["c"] = 3
od["d"] = 4

print(od)
print(od.keys())

for key, value in od.items():
    print(key, value, sep=" : ", end="\n")

# 	Defaultdict is a container like dictionaries present in the module collections. Defaultdict is a sub-class of the dict class that returns a dictionary-like object. The functionality of both dictionaries and defualtdict are almost same except for the fact that defualtdict never raises a KeyError. It provides a default value for the key that does not exists.


# def def_value():
#     return "Not Present"

# d = collections.defaultdict(def_value)

d = collections.defaultdict(lambda: "Not Present")

d["a"] = 1
d["b"] = 2

print(d)
print(d["a"])
print(d["b"])
print(d["c"])  # 	we get error in ordinary dict if we access key which DNE

d2 = collections.defaultdict(int)  # 	passing int as default factory
# d2[1] = "sadas"
# d2[2] = "sdasdqweq"
d2["asdsad"] = 1
d2["sada"] = 2

print(d2)
print(d2["asdsad"])
print(d2["sada"])
print(d2["asdasdawq"])
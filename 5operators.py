# types of operators in python
# 	1.	arithmetic	->	+, -, *, /, %, **, //
# 	2.	assignment
# 	3.	comparison
# 	4.	logical ->	and, or, not
# 	5.	membership => they are used to check if a sequence is present in an object -> in => returns true if a sequence with the specified value is present in the object, not in => vice-versa of in
# 	6.	idnetity => identity operators are used to compare objects -> is => returns true if both the variables are same object, is not => returns true if both the variables are not the same object
# 	7.	bitwise => ~ -> not

print(2 ** 10)
print(3 // 2)  # 	floor division

print(1 > 0 and 2 > 0)
print(1 < 0 or 2 > 0)
print(not (1 < 0 or 2 > 0))

list1 = [10, 20, 30]
list2 = [10, 20, 30]

x = list1
print(x is list1)

print(list2 is list1)

s1 = "asd"
s2 = "aaasdff"

print(s1 in s2)

print(list1 in list2)  # 	list2 does not contain the entire list1 as a element

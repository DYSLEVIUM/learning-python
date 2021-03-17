# dictionary is a hashmap
my_dict = {"dave": 1, "ava": 2, "joe": 4}
print(my_dict)
print(type(my_dict))

print("\n")

new_dict = dict()
print(new_dict)
print(type(new_dict))

# 	nested dictionary
emp_details = {
    "employee": {
        "dave": {"id": 1, "salary": 1000, "designation": "junior engineer"},
        "ava": {"id": 2, "salary": 2000, "designation": "senior engineer"},
    }
}

print(emp_details)

print("\n")

# 	accessing items
print(my_dict["dave"])
print(my_dict.keys())
print(my_dict.values())
print(my_dict.get("ava"))

for x in my_dict:
    print(x)

for x in my_dict.values():
    print(x)

for x, y in my_dict.items():
    print(x, y, sep=" : ", end="\n")

print("\n")

# 	updating items
my_dict["dave"] = 5
my_dict["chris"] = 3
print(my_dict)

print("\n")

# 	deleting items
print(my_dict.pop("ava"))  # 	removes the key and returns the value
print(my_dict)
print(my_dict.popitem())  # 	removes the last inserted element and returns it
print(my_dict)

del my_dict["dave"]
print(my_dict)

print("\n")

# 	converting dictionary to a dataframe
# 	dataframe is a 2-D data structure that consists of columns of potentially various types
import pandas as pd

df = pd.DataFrame(emp_details["employee"])
print(df)

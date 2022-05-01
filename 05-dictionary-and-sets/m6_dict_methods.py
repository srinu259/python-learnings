d = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4:  "four",
    5:  "five",
    6:  "six",
    7:  "seven",
    8:  "eight",
    9:  "nine"
}

pantry = ["eggs", "bread", "cheese", "onions", "chillies"]

# dict.fromKeys takes an iterable as input and convert it into dictionary
new_dict = dict.fromkeys(pantry)
print(f"new_dict with no default value {new_dict}")

# pass a default value for keys
new_dict = dict.fromkeys(pantry, 0)
print(f"new_dict with default value set to 0 : {new_dict}")

# keys method iterates over dictionary keys
# python 2.2 this used to produce list object, which is very inefficient if there are large dictionaries
# python 3.x creates a view object, so you cannot update the keys
keys = d.keys()
# print(f"keys is {keys}")
# print(type(keys))
# print(list(keys))
# for i in keys:
#     print(i)

# dictionary update method
d2 = {
    3: "a new beginning",
    10: "one more!",
    7: "lucky 'u'"
}
d.update(d2)
for key, value in d.items():
    print(key, value)

# dict `update` method with list, this is only a special case
# enumerate returns sequence and value, the sequence here matches with the keys
print()
d.update(enumerate(pantry))
for key, value in d.items():
    print(key, value)

# dict `value` method
print()
val = d.values()
val_list = list(d.values())
print(val)
print(val_list)

print("eggs" in val)
print("eggs" in val_list)

# name = "Eric Sigel"
# print(name.lower(), "is funny")
# print("{}.lower() is funny".format(name))
# print(f"{name.lower()} is funny")


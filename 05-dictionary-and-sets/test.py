from m4_contents import pantry, recipes

# using lists `in` operator
available_parts = [
    "Computer",
    "Monitor",
    "Keyboard",
    "Mouse",
    "Floppy",
    "HDMI Cable"
]

item = "Mouse"
item_value = "4"
print(item in available_parts)        # True
print(item_value in available_parts)  # False

print()
# using dictionaries `in` operator
available_parts = {
    "1": "Computer",
    "2": "Monitor",
    "3": "Keyboard",
    "4": "Mouse",
    "5": "Floppy",
    "6": "HDMI Cable"
}

item = "Mouse"
item_value = "4"
print(item in available_parts)        # False
print(item_value in available_parts)  # True

###########

# We need an empty dictionary, to store and display the letter frequencies.
word_count = {}

# Text string
text = "Later in the course, you'll see how to use the collections Counter class."
print(text.casefold())

for char in text.casefold():
    if char.isalpha():
        count = text.casefold().count(char)
        word_count[char] = count

# Printing the dictionary
for letter, count in sorted(word_count.items()):
    print(letter, count)

t_car_models = {
    "kia": "seltos",
    "maruti": "altos",
    "nexa": "scross",
    "tata": "nexon",
    "mahindra": "thar"
}

for model in t_car_models:
    print(model, t_car_models[model])

print()
print("Cars - List")
t_cars_l = ["kia", "maruti", "nexa", "tata", "mahindra"]
for car in t_cars_l:
    print(car)

print()
print("Cars - Tuples")
t_cars_t = ("kia", "maruti", "nexa", "tata", "mahindra")
for car in t_cars_t:
    print(car)





# for cars in t_car_models:
#     print(cars, t_car_models[cars])
#     print(cars, t_car_models.get(cars))
#
# t_car_models["tata"] = "harrier"
# print(t_car_models)
#
# for cars, model in t_car_models.items():
#     print(cars, model)
#
# # print(t_car_models["daimler"])
# print(t_car_models.get("daimler"))
# t_car_models["daimler"] = "c class"
#
# del t_car_models["daimler"]
# print(t_car_models)
# print(t_car_models.pop("daimler", "Already Removed"))
# print(t_car_models)
# # del t_car_models["daimler"]

t_zip = zip(('a', 'b', 'c'), (1, 2, 3), ('A', 'B', 'C'))
print(tuple(t_zip))

t_computer_parts = {
    "1": "Computer",
    "2": "Monitor",
    "3": "Keyboard",
    "4": "Mouse",
    "5": "Floppy",
    "6": "HDMI Cable"
}

selected_parts = []
print("Please select the computer parts")
for partId, partName in t_computer_parts.items():
    print(f'{partId}. {partName}')

# while True:
#     print()
#     i = input(">: ")
#     if i in t_computer_parts:
#         if t_computer_parts[i] in selected_parts:
#             selected_parts.remove(t_computer_parts[i])
#             print(f"Removed {t_computer_parts[i]}")
#             print(f"Updated order list: {selected_parts}")
#         else:
#             selected_parts.append(t_computer_parts[i])
#             print(f"Added {t_computer_parts[i]}")
#             print(f"Updated order list: {selected_parts}")
#     else:
#         print(f"Your order list {selected_parts}")
#         break

def order_for_pantry(item: str, value: int):
    if item in pantry:
        to_buy = value - pantry.get(item)
    else:
        to_buy = value
    print(f"Buy {item} - {value}")

print()
print("Please select from menu list")
for key, value in enumerate(recipes):
    print("{0}. {1}".format(key+1, value))

print()
# i = input(">: ")
i = 0
selected_meal = list(recipes.keys())[int(i)-1]
print(selected_meal)
required_items = recipes[selected_meal]

for item in required_items:
    item_value = required_items[item]
    pantry_value = pantry.get(item, 0)
    if item_value <= pantry_value:
        print(f"{item} is available")
    else:
        print(f"Please buy {item} {item_value}")
        order_for_pantry(item, item_value)

# for pantry_item, pantry_value in pantry.items():


t_dict_example = {
    "Orange": "Orange colored fruit",
    "Grape": "Green colored fruit",
    "Banana": "Yellow colored fruit",
    "Water Melon": "Green colored fruit"
}

keys = [""]*10
values = keys.copy()
print(keys, values)

def get_hash(s: str) -> int:
    '''
    Return a simple hash value
    :param s: input string to get the simple hash
    :return: return the hash value
    '''
    return ord(s[0]) % 10


def get_value(key: str) -> str:
    hashcode = get_hash(key)
    if values[hashcode]:
        return values[hashcode]
    else:
        return "None"


for item in t_dict_example:
    print(item)
    keys[get_hash(item)] = item
    values[get_hash(item)] = t_dict_example[item]

print(keys)
print(values)
print(values[1])


def deep_copy(old: dict) -> dict:
    new = {}
    for key, value in old.items():
        val = value.copy()
        new[key] = val
        print(key, id(val[1]))
    return new


t_old = {
    "a": [1, [2, 3]],
    "b": [3, [4, 5]]
}
t_new = deep_copy(t_old)
t_old["a"][1].append(4)
print("a", id(t_old["a"][1]))
print(t_old)
print(t_new)

t_1 = {
    "a": "a-key",
    "b": "b-key"
}
t_2 = t_1.copy()
print(id(t_1), id(t_2))

# SETS
animals_domesticated = {"cow", "sheep", "goat", "dog", "cat"}
print(animals_domesticated)
for animal in animals_domesticated:
    print(animal)

# this print statement will not work
# print(animals_domesticated[2])

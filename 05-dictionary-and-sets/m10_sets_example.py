# sets are unordered data types
# if you execute the below code multiple times, you will get different order of set everytime
farm_animals = {"cow", "sheep", "hen", "dog", "horse"}
print(farm_animals)

for animals in farm_animals:
    print(animals)

new_farm_animals = {"dog", "sheep", "cow", "horse", "hen"}
if farm_animals == new_farm_animals:
    print("Sets are identical")
else:
    print("Sets are NOT identical")

# List maintains the order, so 2 lists with same values and different order cannot be equal
print()
print(" --- Test Lists --- ")
farm_animals_list = ["cow", "sheep", "hen", "dog", "horse"]
print(farm_animals_list)
new_farm_animals_list = ["dog", "sheep", "cow", "horse", "hen"]
if farm_animals_list == new_farm_animals_list:
    print("List are identical")
else:
    print("List are NOT identical")

# From Python 3.9 dictionaries maintains the order, so 2 dictionaries with same keys and different order are still equal
print()
print(" --- Test Dictionary --- ")
farm_animals_dict = {"cow": "cow", "sheep": "sheep", "hen": "hen", "dog": "dog", "horse": "horse"}
print(farm_animals_dict)
new_farm_animals_dict = {"dog": "dog", "sheep": "sheep", "cow": "cow", "horse": "horse", "hen": "hen"}
if farm_animals_dict == new_farm_animals_dict:
    print("Dictionaries are identical")
else:
    print("Dictionaries are NOT identical")

# create an empty set
# numbers = {} -> This creates a dictionary and not set!!!
numbers = {}
print(numbers, type(numbers))
# numbers = {*""} -> Not an ideal way, but does the job
numbers = {*""}
print(numbers, type(numbers))
# numbers = {*""} -> Not an ideal way, but does the job
numbers = {*{}}
print(numbers, type(numbers))
# numbers = set() -> this is how you do it!
numbers = set()
print(numbers, type(numbers))

# set only accepts the unique value, even if you try adding duplicate values, the value will be added only once
while len(numbers) < 4:
    next_value = int(input("Enter a number: "))
    numbers.add(next_value)
print(f"Numbers set is: {numbers}")

# converting a list with dupicate values into a set with unique values
car_colors = ["red", "black", "red", "silver", "brown", "silver"]
car_unique_colors = set(car_colors)
# this does not preserve the order
print(car_unique_colors)
print(list(car_unique_colors))
car_unique_colors = list(dict.fromkeys(car_colors))
# this preserves the order
print(car_unique_colors)


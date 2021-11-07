import copy

# dictionary shallow copy examples
animals = {
    "lion": "roar",
    "elephant": "mammoth",
    "teddy": "soft"
}
print("--- normal-copy ---")
# things = animals points the 2 dictionary to same object
things = animals
print("id(things)", id(things))
print("id(animals", id(animals))
animals["teddy"] = "bear"
print(animals["teddy"])
print(things["teddy"])

# copy() function does a shallow copying by creating a new dictionary
print()
print("--- shallow-copy ---")
print("        --- with immutable objects --- ")
things = animals.copy()
animals["teddy"] = "soft"
print(animals["teddy"])
print(things["teddy"])

# another confusing example, here we set values to list
new_animals = {
    "lion": ["roar", "ferocious", "king"],
    "elephant": ["mammoth", "strong", "vegetarian"],
    "teddy": ["soft", "toy", "stuffed"]
}

# using copy() creates a new dictionary, we expect 2 dictionary objects and 6 lists
# but the lists are not shallow copied
print("        --- with mutable objects --- ")
new_things = new_animals.copy()
new_animals["teddy"].append("doll")
print(new_animals["teddy"])
print(new_things["teddy"])

# simplifying the example to understand shallow copy of mutable objects
# dictionary object does not store the list, but it stores the reference for the list
lion_list = ["roar", "ferocious", "king"]
elephant_list = ["mammoth", "strong", "vegetarian"]
teddy_list = ["soft", "toy", "stuffed"]

print("        --- with mutable objects - simplified example --- ")
another_animal = {
    "lion": lion_list,
    "elephant": elephant_list,
    "teddy": teddy_list
}

# eventhough we make a shallow copy of the dictionary,
# the new dictionary object still points to the list reference
another_thing = another_animal.copy()
# another_animal["teddy"].append("doll")

# here we append a new item to the teddy_list
# because the dictionary has reference to the list, so the list objects are updated in both dictionaries
teddy_list.append("doll")
print(another_animal["teddy"])
print(another_thing["teddy"])
print()

# dictionary deep copy examples
print(" --- deep-copy --- ")
deep_animals = {
    "lion": ["roar", "ferocious", "king"],
    "elephant": ["mammoth", "strong", "vegetarian"],
    "teddy": ["soft", "toy", "stuffed"]
}

# similar to OO, deep copy creates copy of each and existing object
# so deep copy makes a new list instead of referring the dictionary to an existing list
deep_things = copy.deepcopy(deep_animals)
deep_animals["teddy"].append("doll")
print(deep_things["teddy"])
print(deep_animals["teddy"])
# dictionaries store data in key:value format
# with get method if the key does not exist a None is returned
# with the [] the program crashes if the key does not exist
# [] is to be used when you know the key, this is the faster way to access the dictionary
# get is to be used when you dont know the key name and you dont want to crash your program

cars = {
    'kia': 'seltos',
    'nexa': 'scross',
    'ford': 'ecosport',
    'hyundai': 'creta',
    'mahindra': 'xuv300',
    'tata': 'nexon'
}

# the below code works, but there is duplicate key
# so the second nexa element value will be replaced with baleno
# cars = {
#     'kia': 'seltos',
#     'nexa': 'scross',
#     'ford': 'ecosport',
#     'hyundai': 'creta',
#     'mahindra': 'xuv300',
#     'tata': 'nexon',
#     'nexa': 'baleno'
# }

print(cars['kia'])
print(cars.get('kia'))
print(cars.get('KIA'))
# print(cars['KIA'])
print()

# iterate over dictionaries
print("-- iterate over dictionary --")
for key in cars:
    print(key, cars[key], sep=", ")

print()
for key, value in cars.items():
    print(key, value, sep=", ")

# add new keys to dictionaries
print()
print("-- add new key to dictionary --")
cars['mg'] = 'hector'
for key, value in cars.items():
    print(key, value, sep=", ")
    
# override an existing value from dictionary
print()
print("-- override existing key in a dictionary --")
cars['mg'] = 'astor'
for key, value in cars.items():
    print(key, value, sep=", ")

# deleting items from dictionary
print()
print("-- deleting items from dictionary --")
del cars['mg']
for key, value in cars.items():
    print(key, value, sep=", ")

# this will crash program as mg key does not exist
# del cars['mg']
# cars.pop('mg')

# provide a default value with pop, if the key may not exist, so that program does not crash
result = cars.pop('mg', 'Key Not Available')
print(result)


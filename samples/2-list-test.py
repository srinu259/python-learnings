"""
clean up the numbers list so that only numbers between 100-200 exists
"""

numbers = [5, 3, 102, 157, 143, 202, 257, 199, 123, 164, 135, 210]
low = 100
high = 200

# devastating to do this with lists. list indexing gets updated after changes
# for idx, num in enumerate(numbers):
#     if num < low:
#         del numbers[idx]

# iterate from the last and delete, so that even if indexing is updated it will not make any difference
for idx in range(len(numbers)-1, -1, -1):
    if not low < numbers[idx] < high:
        del numbers[idx]

numbers = [5, 3, 102, 157, 143, 202, 257, 199, 123, 164, 135, 210]
numbers.sort()
print(numbers)

# we first sort the numbers and then remove the outliers
for idx in range(0, len(numbers)-1):
    if numbers[idx] > low:
        del numbers[:idx]
        break

for idx in range(0, len(numbers)-1):
    if numbers[idx] > high:
        del numbers[idx:]
        break

print(numbers)

# nested list spam challenge
menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

for menu_list in menu:
    for idx in range(len(menu_list)-1,-1,-1):
        if menu_list[idx] == 'spam':
            del menu_list[idx]

print(menu)

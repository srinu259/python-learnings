test = sorted('246733358901')
print(test)

test = sorted('238956efd#@^*$')
print(test)

# spam challenge
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

# for items in menu:
#     while items.__contains__("spam"):
#         items.remove("spam")
#     print(items)

for items in menu:
    for i in range(len(items)-1, -1, -1):
        if items[i] == "spam":
            del items[i]
    print(items)

# for items in menu:
#     for i in range(0, len(items)):
#         if items[i] == "spam":
#             items.remove("spam")
#             # del items[i]
#     print(items)

numbers = "9,234,563,123,567,036,857"
separator = ","
value = " ".join(" " if char in separator else char for char in numbers).split()
print(value)
print(float("-inf"))


def find_max(nums):
    max_num = float("-inf") # smaller than all other numbers
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num


print(find_max([1, 12, 3]))

# spam challenge
menu1 = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

for item_list in menu1:
    for item in item_list:
        if item == "spam":
            item_list.remove("spam")
            break

print(menu)

temp = '9 234,563,123,567,036,857'
print(temp.split())

temp = '9,234,563,123,567,036,857'
print(temp.split(','))

temp_list = []
for temp_item in temp[:]:
    if temp_item == ',':
        temp_list.append(' ')
    else:
        temp_list.append(temp_item)
print(temp_list)

# #use list-comprehension to do the same code
# for temp_item in temp[:]
# if temp_item == ',' then ' ' else temp_item
# nested list a list contained within a list
even_number = [2, 4, 6, 8,]
odd_number = [1, 3, 5, 7, 9,]

all_numbers = even_number + odd_number
print(all_numbers)

nested_list_numbers = [even_number, odd_number]
for number_list in nested_list_numbers:
    print(number_list)
    for value in number_list:
        print(value)

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

# what i wrote
# new_list = []
# for menu_list in menu:
#     print(menu_list)
#     temp_list = []
#     for value in menu_list:
#         if not value.__contains__("spam"):
#             temp_list.append(value)
#             print(value)
#     new_list.append(temp_list)
# print(new_list)

# from the tutor
for menu_list in menu:
    for index in range(len(menu_list)-1, -1, -1):
        if menu_list[index] == "spam":
            del menu_list[index]
    print(menu_list)

for menu_list in menu:
    for item in menu_list:
        if not item == "spam":
            print (item)
    print()
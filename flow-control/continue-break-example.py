#CONTINUE example
shopping_list = ["cream", "powder", "deo", "spam", "bread", "eggs"]

for item in shopping_list:
    if(item == "spam"):
        continue
    print("Buy {}".format(item))

#BREAK example
print()
item_to_find = "spam"
found_at = None

# for index in range(len(shopping_list)):
#     if item_to_find == shopping_list[index]:
#         found_at = index
#         break

if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)

print("{} is found at position {}".format(item_to_find, found_at))


from contents import pantry, recipes, recipes_tuple, recipes_dict

# print(pantry)
# print(recipes)
items_list = {}
new_order = {}


def order_for_pantry(data: dict, item_to_order: str, quantity_to_order: int=0) -> None:
    # if item_to_order in data:
    #     data[item_to_order] += quantity_to_order
    # else:
    #     data[item_to_order] = quantity_to_order
    data[item_to_order] = data.setdefault(item_to_order, 0) + quantity_to_order


for index, key in enumerate(recipes):
    items_list[str(index+1)] = key

while True:
    print("Choose items from the menu below:")
    for key, value in items_list.items():
        print(f"{key}. {value}")

    print()
    item = input("> ")

    if item == "0":
        break
    elif item in items_list:
        item_selected = items_list.get(item)
        print(f"Item selected is '{item_selected}'")
        print("Recipe includes .... ", end="")
        ingredients = recipes.get(item_selected)
        print(ingredients)

        for ingredient, quantity_required in ingredients.items():
            quantity_in_pantry = pantry.get(ingredient, 0)
            if quantity_required <= quantity_in_pantry:
                print(f"\t{ingredient} is available")
            else:
                quantity_to_buy = quantity_required - quantity_in_pantry
                print(f"\tPlease buy {quantity_to_buy} of {ingredient}")
                order_for_pantry(new_order, ingredient, quantity_to_buy)
        print()
print(new_order)
        # print("Quantity required: Using Tuple")
        # for food, quantity in recipes_tuple[item_selected]:
        #         print(f"\t{food} - {quantity}")
        # print()
        # print("Quantity required: Using Dictionary")
        # for food, quantity in recipes_dict.get(item_selected).items():
        #     print(f"\t{food} - {quantity}")
        #     # for food, quantity in food_items.items():  # this fails because iterator will iterate through dictionary and returns single value
        #     #     print(f"\t{food} - {quantity}")
        # print()


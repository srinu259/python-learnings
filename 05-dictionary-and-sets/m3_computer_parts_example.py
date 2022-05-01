available_parts = {
    "1": "Computer",
    "2": "Monitor",
    "3": "Keyboard",
    "4": "Mouse",
    "5": "Floppy",
    "6": "HDMI Cable"
}

ordered_parts = []
ordered_dict = {}
item = "1"
# while item in available_parts.keys():
while item in available_parts:
    print("Please select from the below computer parts to order: ")
    for key, value in available_parts.items():
        # print("{}. {}".format(key, value))
        print(f"{key}. {value}")

    print()
    item = input("> ")
    # if ordered_parts.__contains__(available_parts.get(item)):
    # if available_parts.get(item) in ordered_parts:
    #     print("Removing '{}' from basket".format(available_parts.get(item)))
    #     ordered_parts.remove(available_parts.get(item))
    #     print("Ordered items: {}".format(ordered_parts))
    # elif available_parts.get(item):
    #     print("Adding '{}' to basket".format(available_parts.get(item)))
    #     ordered_parts.append(available_parts.get(item))
    #     print("Ordered items: {}".format(ordered_parts))

    if item in ordered_dict:
        print("Removing '{}' from basket".format(available_parts.get(item)))
        ordered_dict.pop(item)
        print(f"Ordered items: {ordered_dict}")
    elif available_parts.get(item):
        print("Adding '{}' to basket".format(available_parts.get(item)))
        ordered_dict[item] = available_parts.get(item)
        print(f"Ordered items: {ordered_dict}")

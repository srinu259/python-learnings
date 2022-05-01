travel_mode = {"1": "car", "2": "plane"}

items = {
    "can opener",
    "fuel",
    "jumper",
    "knife",
    "matches",
    "razor blades",
    "razor",
    "scissors",
    "shampoo",
    "shaving cream",
    "shirts (3)",
    "shorts",
    "sleeping bag(s)",
    "soap",
    "socks (3 pairs)",
    "stove",
    "tent",
    "mug",
    "toothbrush",
    "toothpaste",
    "towel",
    "underwear (3 pairs)",
    "water carrier",
}

restricted_items = {
    "catapult",
    "fuel",
    "gun",
    "knife",
    "razor blades",
    "scissors",
    "shampoo",
}

print("Select the mode of travel")
for key, value in travel_mode.items():
    print(f"{key}. {value}")
print()
mode = input(">: ")
if mode == "1":
    print("You can carry the following items:")
    for item in items:
        print(item, end=", ")
if mode == "2":
    print("Following restricted items cannot be carried:")
    for r_items in restricted_items:
        print(r_items, end=", ")
    print(end="\n")
    print()
    print("You are carrying the following restricted items that has to be removed:")
    for r_items in restricted_items:
        if r_items in items:
            # items.remove(r_items)
            print(r_items, end=", ")
    print(end="\n")
    print()
    print("Your new item list:")
    # print(items)
    print(items - restricted_items)
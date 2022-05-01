from m4_contents import pantry

chicken = pantry.setdefault("chicken", 0)
print(f"chicken: {chicken}")

# a setdefault method on dictionary adds the item back to dictionary if it does not find it. Its like a PUT call
beans = pantry.setdefault("beans", 0)
print(f"beans: {beans}")

# a get method on dictionary does not add the item back in dictionary. Its just a GET call
carrot = pantry.get("carrot", 0)
print(f"carrot: {carrot}")

print()
for key, value in sorted(pantry.items()):
    print(key, value)
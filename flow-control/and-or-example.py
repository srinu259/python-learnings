age = int(input("Enter your age: "))

print()
print("Using AND condition")
if age >= 18 and age <= 65:
    print("Enjoy your day at work!")
else:
    print("Enjoy your free time!")

print()
print("Using CHAINED condition")
if 18 <= age <= 65:
    print("Enjoy your day at work!")
else:
    print("Enjoy your free time!")

print()
print("Using OR condition")
if age < 18 or age > 65:
    print("Enjoy your free time!")
else:
    print("Enjoy your day at work!")


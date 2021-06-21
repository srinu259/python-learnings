month = 'September1'
temp = 30
raining = False

# BOOLEAN with AND condition
if (month == 'September' and temp > 27 and not raining):
    print("You can swim")
else:
    print("Not a time to swim")

# BOOLEAN with OR condition
if ((month == 'September' and temp > 27) or not raining):
    print("You can swim")
else:
    print("Not a time to swim")

# BOOLEAN with TRUTH values
if 0:
    print("Code will never reach here. True here!")
else:
    print("False here!")

# name = input("Enter your name: ")
# if name:
#     print("Hello {}".format(name))
# else:
#     print("You are kidding not to have a name")

# BOOLEAN with IN
dinosaur = 'trisorase'
letter = input("Enter a character: ")

if letter in dinosaur:
    print("Yes the letter {} is in {}".format(letter, dinosaur))
else:
    print("I don't need that letter")

# BOOLEAN with NOT-IN
activity = input("What would you like to do today? ")
if 'cinema'.casefold() not in activity:
    print("But, I want to learn Python")



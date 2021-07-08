# Following datatypes are mutable in python
# 1. list
# 2. dict
# 3. set
# 4. bytearray

computer_parts = ["Monitor",
                  "Keyboard",
                  "Mouse",
                  "CPU",
                  "RAM"]
print("computer_parts id {}".format(id(computer_parts)))
another_computer_parts = computer_parts
print("another_computer_parts id {}".format(id(another_computer_parts)))
print("another_computer_parts list {}".format(another_computer_parts))
computer_parts += ["Storage"]

print()
print("Updated computer_parts list {}".format(computer_parts))
print("Updated computer_parts ID {}".format(id(computer_parts)))
print("Another computer_parts list {}".format(another_computer_parts))
# ID remains same as above as list is a mutable object
# Similar to JavaScript objects mutable objects in python will have the same ID even after object is updated


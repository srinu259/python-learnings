parrot = "Norwegian Blue"

print(parrot)
'''
# Indexing
print("--Indexing--")
print(parrot[3])
print(parrot[4])
print()
print(parrot[3])
print(parrot[6])
print(parrot[8])

# Negative Indexing
print("--Negative Indexing--")
print()
print(parrot[-11])
print(parrot[-10])
print()
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])

#Slicing
print()
print("--Slicing--")
print(parrot[2:5])
print(parrot[:4])
print(parrot[4:])
print(parrot[:4] + parrot[4:])
print(parrot[:])
'''

# Negative Slicing
print()
print("--Negative-Slicing--")
print(parrot)
print(parrot[-4:2]) # -4 means from the ending, 2 means from the beginning, so this is empty
print(parrot[-4:12]) # -4 means from the ending, 12 means from the beginning
print(parrot[-14:-10])

# Slicing with steps
print()
print("--Slicing-with-steps--")
print(parrot)
print(parrot[1::2]) # Get every alternate character

# Slicing with negative steps
print()
print("--Slicing-with-negative-steps--")
letters = "abcdefghijklmnopqrstuvwxyz"
print(letters[25:0:-1]+letters[0])
print(letters[25::-1])
print(letters[::-1])  # Reverse a string

# qpo  edcba
print()
print("qpo edcba last-6-letters")
print(letters[-10:-13:-1])
print(letters[-10:13:-1])
print(letters[4::])
print(letters[4::-1])
print(letters[:19:-1])
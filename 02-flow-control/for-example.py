# Print all characters with FOR loop
parrot = 'Norwegian Blue'
for chars in parrot:
    print(chars)

print()
number = "9,234;3534;232;245;24f"
sequence = ""
for char in number:
    if not char.isnumeric():
        sequence = sequence + char
print(sequence)

# FOR loop with RANGE
# Ending value in the RANGE is not looped
print()
for i in range(0,10):
    #print("i is now {}".format(i))
    print(i)

# FOR loop with RANGE and STEP
print()
for i in range(0,10,2):
    #print("i is now {}".format(i))
    print(i)

# FOR loop with RANGE and NEGATIVE STEP
print()
for i in range(10,0,-2):
    #print("i is now {}".format(i))
    print(i)

print()
for i in range(0,100,7):
        print(i)

print()
print("NESTED FOR loops")
for i in range(1, 11):
    for j in range(1, 11):
        print("{} times {} is equal to {}".format(j, i, j*i))
    print("-"*10)

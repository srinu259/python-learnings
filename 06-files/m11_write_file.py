flowers = [
    "Rose",
    "Sunflower",
    "Lilly"
]

# METHOD-1: Writing to a file by printing to it
file_name = "m12_invictus_copy.txt"
with open(file_name, 'w') as poem:
    for flower in flowers:
        print(flower, file=poem)

flowers_copy = []
with open(file_name) as poem:
    for flower in poem:
        flowers_copy.append(flower.rstrip())

print(flowers_copy)

# METHOD-2: Writing to a file by using write method
file_name = "m12_invictus_copy_2.txt"
with open(file_name, 'w') as poem:
    for flower in flowers:
        poem.write(flower)

print(flowers)
print(type(flowers.__str__()))

# Difference between PRINT and WRITE
# PRINT adds the new line character by default at the end of the string
# PRINT can also be customized by adding sep as required
# WRITE just writes what you want thats all
# Thats why with WRITE observe that the new line characters are missing at the end
# Note that you can only write strings to a file, integers cannot be written to file
# If integers have to be written they have to be converted to string

# Write int using print to a file
file_name = "m12_invictus_copy_3.txt"
with open(file_name, "w") as test:
    for i in range(10):
        print(i, file=test)

# Write int using write to a file
file_name = "m12_invictus_copy_4.txt"
with open(file_name, "w") as test:
    for i in range(10):
        # This will fail as i is int
        # test.write(i)
        test.write(str(i))

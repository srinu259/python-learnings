# list is always recommended to have homogeneous values
# eventhough you can have different datatypes added and python/list wont complain
flowers = [
    "Lilly",
    "Rose",
    "Hibiscus",
    "Jasmine",
    "Lavender"
]

for flower in flowers:
    print(flower)

# using join
separator = " | "
output = separator.join(flowers)
print(output)
print(", ".join(flowers))

# join only works on strings
# numbers = [1, 2, 3, 4, 5]
# print(", ".join(numbers))

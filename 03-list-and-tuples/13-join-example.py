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
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)
# print(", ".join(numbers))

# any iterable can be joined
# provided its content and the joiner are the strings!!
# even though numbers list is iterable, they cannot be joined as they are integers
# now question is why the heck can't they join integers as well ?
# with that question will come like why can't they join anything and everything ?
# this is where you have to be little sensitive. There is no point in joining numbers

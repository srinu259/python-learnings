# using lists `in` operator
available_parts = [
    "Computer",
    "Monitor",
    "Keyboard",
    "Mouse",
    "Floppy",
    "HDMI Cable"
]

item = "Mouse"
item_value = "4"
print(item in available_parts)        # True
print(item_value in available_parts)  # False

print()
# using dictionaries `in` operator
available_parts = {
    "1": "Computer",
    "2": "Monitor",
    "3": "Keyboard",
    "4": "Mouse",
    "5": "Floppy",
    "6": "HDMI Cable"
}

item = "Mouse"
item_value = "4"
print(item in available_parts)        # False
print(item_value in available_parts)  # True

###########

# We need an empty dictionary, to store and display the letter frequencies.
word_count = {}

# Text string
text = "Later in the course, you'll see how to use the collections Counter class."
print(text.casefold())

for char in text.casefold():
    if char.isalpha():
        count = text.casefold().count(char)
        word_count[char] = count

# Printing the dictionary
for letter, count in sorted(word_count.items()):
    print(letter, count)
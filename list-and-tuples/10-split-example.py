# split returns a list
# split by default breaks a string based on spaces, new line characters and tabs
# you can always provide a char on which it has to be split

panagram = "The quick brown fox jumps over the lazy dog"
print(panagram.split())

panagram = "The quick brown fox " \
           "jumps over\tthe lazy dog"
print(panagram.split())

numbers = "9,234,563,123,567,036,857"
print(numbers.split(","))

# separators = ","
# temp_list=[]
# for char in numbers:
#     if char not in separators:
#         print(char)
#         temp_list.append(char)
#     else:
#         print(" ")
#         temp_list.append(" ")
# print(temp_list)
# ['9', ' ', '2', '3', '4', ' ', '5', '6', '3', ' ', '1', '2', '3', ' ', '5', '6', '7', ' ', '0', '3', '6', ' ', '8', '5', '7']

# value = " ".join(char if char not in separators else " " for char in numbers).split()
# print(value)

generated_list = ['9', ' ',
                  '2', '3', '4', ' ',
                  '5', '6', '3', ' ',
                  '1', '2', '3', ' ',
                  '5', '6', '7', ' ',
                  '0', '3', '6', ' ',
                  '8', '5', '7']
value = "".join(generated_list).split()
print(value)

# mini-challenge in the course: convert the strings into int
# what i wrote
new_list = []
for new_values in value:
    new_list.append(int(new_values))
print(new_list)

# tutor another way
for index in range(len(value)):
    value[index] = int(value[index])
print(value)
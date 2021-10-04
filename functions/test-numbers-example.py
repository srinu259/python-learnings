num_sequence = (1, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8)
list1 = []
list2 = []
skip = "N"

for num in range(len(num_sequence)-1):
    print(num)
    if skip == "N":
        if num_sequence[num] == num_sequence[num+1]:
            skip = "Y"
        else:
            list1.append(num_sequence[num])
            list2.append(num_sequence[num+1])
    else:
        skip = "N"

print("{} length is {}".format(list1, len(list1)))
print("{} length is {}".format(list1, len(list2)))
data = [3,5,102,127,139,144,157,162,175,189,198,305,307]
min_valid = 100
max_valid = 200

# for index, num in enumerate(data):
#     if num < min_valid or num > max_valid:
#         continue;
#     else:
#         print(num)

# A wrong way to delete the outliers. Python resets the index every iteration
for index, num in enumerate(data):
    if num < min_valid or num > max_valid:
        del data[index]
print(data)


data = [102,3,5,127,139,144,157,162,305,307,175,189,198]
min_valid = 100
max_valid = 200

data.sort()
stop = 0
for index, num in enumerate(data):
    if min_valid < num:
        stop = index
        break
del data[:stop]
print(data)
# Below approach might consume lot of resources if the data set is huge
# stop = 0
# for index, num in enumerate(data):
#     if num > max_valid:
#         stop = index
#         break
# del data[stop:]
# print(data)

# Alternate way is to iterate the data from the end
stop = 0
for index in range(len(data)-1,-1,-1):
    print(index,' - ', data[index])
    if max_valid >= data[index]:
        stop = index + 1
        break
del data[stop:]
print(data)

# a better way to remove outliers from both sorted and unsorted data
data = [ 102, 107, 3, 147, 132, 167, 5, 189, 306, 155, 135, 5, 330, 190, 195]
min_valid = 100
max_valid = 200

print(data)
for index in range(len(data) - 1, -1, -1):
    print(index, ' - ', data[index])
    if data[index] <= min_valid or data[index] >= max_valid:
        del data[index]
        print(data)
print(data)

# Another way is to use reversed() function to reverse the data
# keep an eye on index when enumerate() function is used, index has to be reversed from the code
data = [ 102, 107, 3, 147, 132, 167, 5, 189, 306, 155, 135, 5, 330, 190, 195]
min_valid = 100
max_valid = 200

print(data)
get_index = len(data) - 1
for index, num in enumerate(reversed(data)):
    if num <= min_valid or num >= max_valid:
        print(get_index - index, num)
        del data[get_index - index]
print(data)
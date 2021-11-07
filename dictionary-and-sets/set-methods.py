# clear, remove, discard methods are for removing items

# clear removes all the values from the set
number_set = set(range(20))
print(number_set)
number_set.clear()
print(number_set)

# discard removes an element, if the element doesnot exist it will not throw an error
number_set = set(range(20))
number_set.discard(10)
number_set.discard(99)
print(number_set)

# remove removes an element, if the element doesnot exist it will throw an error
number_set = set(range(20))
number_set.remove(10)
# throws error
# number_set.remove(99)
print(number_set)

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

even.extend(odd)
# Why is output None for the below print statements
# print(even.sort())
# print(even.sort(reverse=True))
even.sort()
print(even)

even.sort(reverse=True)
print(even)



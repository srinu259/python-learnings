even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

even.extend(odd)
# even = even + odd
even.sort()
print(even)

even.sort(reverse=True)
print(even)


# Why is output None for the below print statements
# This is because even.sort() function does not return anything
# It only modifies the original list
even_sorted = even.sort()
print(even_sorted)



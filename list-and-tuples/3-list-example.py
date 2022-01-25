computer_parts = ["Monitor",
                  "Keyboard",
                  "Mouse",
                  "CPU",
                  "RAM"]

for parts in computer_parts:
    print(parts)

print()
print(computer_parts)
print(computer_parts[0])
print(computer_parts[0:3])
print(computer_parts[-1])

print()
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
print(f"Even min: {min(even)} and max: {max(even)}")
# print("Even min: {} and max: {}".format(min(even), max(even)))
print("Odd min: {} and max: {}".format(min(odd), max(odd)))
print("Mississippi".count("iss"))

print()
empty_list=[]
numbers = even + odd
print(numbers)
print(sorted(numbers))
print(numbers)

print()
digits = sorted('4365128970')
print(digits)

# A list does not sort the input values
# more_numbers = numbers
more_numbers = list(numbers)

# python 2 way of copying list
# more_numbers = numbers[:]
# python 3 way of copying list
# more_numbers = numbers.copy()
print(more_numbers)

# ID of numbers is not same as more_numbers
print(numbers is more_numbers)
print(numbers == more_numbers)
numbers = [1, 8, 15, 23, 31]

# Bizzare else loop in python
for number in numbers:
    if number % 8 == 0:
        print("Some or all of numbers are divisible by 8")
        break
else:
    print("None of the numbers are divisible by 8")
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
print("Even min: {} and max: {}".format(min(even), max(even)))
print("Odd min: {} and max: {}".format(min(odd), max(odd)))
print("Mississippi".count("iss"))
parrot = 'Norwegian Blue'

for chars in parrot:
    print(chars)

print()
number = "9,234;3534;232;245;24f"
sequence = ""
for char in number:
    if not char.isnumeric():
        sequence = sequence + char
print(sequence)

char.is
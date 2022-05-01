name = input("Please enter your name: ")
age = int(input("Hello, {0}. Please enter your age: ".format(name)))

if age >= 100:
    print("You lived your life!")
elif age >= 18:
    print("You are eligible for voting")
else:
    print("You have to wait for {0} years before you can vote".format(18-age))

print()
print("Every vote matters")
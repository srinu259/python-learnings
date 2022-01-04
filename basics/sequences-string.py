# 1. string
# 2. list
# 3. tuple
# 4. range
# 5. byte and bytearray

string1 = "This "
string2 = "is "
string3 = "it"

print(string1 + string2 + string3)
print("This " "is " "it")  # Few bad things about python is this example. It would have been clear with a concatenation operator

print("Hello" * 5) # Well, what is the need for this ?
today = "thursday"
print("day" in today)       # True
print("thur" in today)      # True
print("fri" in today)       # False
print("day" in "today")     # True
print("day" in "Hello")     # False

age = 39
print("My age is", age , "years")
#print("My age is " + age + " years") # This fails as string cannot be concatenated to integer
print("My age is " + str(age) + " years")
print("My age is {0} years".format(age))
print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7} months"
      .format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))
print("Jan: {2}, Feb: {0}, Mar: {2}, Apr: {1}, May: {2}, Jun: {1}, Jul: {2}, Aug: {2}, Sep: {1}, Oct: {2}, Nov: {1}, Dec: {2}"
      .format(28, 30, 31))
print("""Jan: {2}
Feb: {0}
Mar: {2}
Apr: {1}
May: {2}
Jun: {1}
Jul: {2}
Aug: {2}
Sep: {1}
Oct: {2}
Nov: {1}
Dec: {2}
""".format(28, 30, 31))

for i in range(1, 13):
    print("No. {0} square is {1} and cube is {2}".format(i, i ** 2, i ** 3))

print()
print("--Right-alignment-defaults-to-greater-than(>)--")
for i in range(1, 13):
    print("No. {0:2} square is {1:4} and cube is {2:4}".format(i, i ** 2, i ** 3))

print()
print("--Right-alignment-with-greater-than(>)--")
for i in range(1, 13):
    print("No. {0:2} square is {1:>4} and cube is {2:>4}".format(i, i ** 2, i ** 3))

print()
print("--Left-alignment-with-less-than(<)--")
for i in range(1, 13):
    print("No. {0:2} square is {1:<4} and cube is {2:<4}".format(i, i ** 2, i ** 3))

print()
print("--Center-alignment-with-cap(^)--")
for i in range(1, 13):
    print("No. {0:2} square is {1:^4} and cube is {2:^4}".format(i, i ** 2, i ** 3))

days = "Mon, Tue, Wed, Thu, Fri, Sat, Sun"
print(days[::5])

data = "1:A, 2:B, 3:C, 4:D, 5:E, 6:F, 7:G, 8:H"
print(data[::5])
print(data[0:1:5])
print(data[0:-1:5])
print(data[:-1:5])

flower = 'blue violet'
print('blue' in flower)
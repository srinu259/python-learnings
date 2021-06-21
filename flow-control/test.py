x = 5
y = 7

if x > y:
    print("{0} is greater than {1}".format(x,y))
elif x < y:
    print("{0} is smaller than {1}".format(x,y))
else:
    print("{0} is equals {1}".format(x,y))

print("Number 1"+'\t'+"The Larch")
print("Number 2"+'\t'+"The Horse Chestnut")

bun_price = 2.40
money = 15
print(int(money//bun_price))

# IF Exercise challenge
age = int(input("Enter your age: "))

if (18 <= age < 31):
    print("Right, have a good day at school")
else:
    print("Time to get busy in life!")
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

# CONTINUE challenge
i = 0
for i in range(0,20):
    if i%3 == 0 or i%5 == 0:
        continue
    else:
        print(i)

# FLOW CONTROL challenge
option = "0"
while option != "4":
    if option in "123":
        print("The option you selected is {} ".format(option))
    else:
        print("Please choose your option from list below:")
        print("1. Learn Python")
        print("2. Learn Java")
        print("3. Learn R")
        print("4. EXIT")
    option = input()
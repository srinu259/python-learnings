# Using for loop here
# for i in range(10):
#     print("i is now {} ".format(i))

# the same example with a while loop
print()
i = 0
while(i < 10):
    print("i is now {}".format(i))
    i += 1

# another example
print()
available_exits = ["east", "west", "north", "south"]
choose_an_exit = ""
while choose_an_exit not in available_exits:
    choose_an_exit = input("Please choose an exit: ")

print("Well, glad you know where you are going")

# WHILE with BREAK
print()
available_exits = ["east", "west", "north", "south"]
choose_an_exit = ""
while choose_an_exit.casefold() not in available_exits:
    choose_an_exit = input("Please choose an exit: ")
    if choose_an_exit.casefold() == 'quit':
        print("Game Over")
        break

print("Well, glad you know where you are going")

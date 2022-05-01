def fizz_buzz(num: int) -> str:
    '''
    A simple fizz buzz program
    :param series: Number to count
    :return: Return the fizz buzz
    '''
    if num%3 == 0 and num%5 == 0:
        element = "fizz buzz"
    elif num%3 == 0:
        element = "fizz"
    elif num%5 == 0:
        element = "buzz"
    else:
        element = str(num)
    return element


computer_turn = True
for i in range(101):
    if computer_turn:
        print("{} is {}".format(i, fizz_buzz(i)))
    else:
        computer_turn = True
        result = input("{} is ".format(i))
        if result == fizz_buzz(i):
            continue
        else:
            print("You failed!")
            break
    computer_turn = False




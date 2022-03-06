def is_int(prompt):
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        print("Invalid Number")


print("Guess a number between 1 and 1000")
answer = 672

while True:
    guess = is_int(": ")
    if guess < answer:
        print("Guess a higher number")
    elif guess > answer:
        print("Guess a lower number")
    else:
        print("You got it right!")
        break

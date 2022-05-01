# Improved version of guess with usage of random module
import random

max_guess = 10
var = random.randint(1, max_guess)
print("Random variable is {}".format(var))
print("Please guess a number between 1 - {}: ".format(max_guess))
guess = 0
guess_count = 0

# Using IF condition
# if guess < var:
#     print("Guess a higher value")
# elif guess > var:
#     print("Guess a lower value")
# else:
#     print("You got it!")

while guess != var:
    guess_count += 1
    guess = int(input())
    if guess == 0:
        break
    elif guess < var:
        print("Guess a higher value")
    elif guess > var:
        print("Guess a lower value")
    else:
        print("You got it! You took {} guesses to find the right number".format(guess_count))


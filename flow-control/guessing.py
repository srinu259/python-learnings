answer = 5
print("Enter a number between 1 -10: ")
guess = int(input())

# First Attempt
# if guess < answer:
#     print("Enter a higher value")
# elif guess > answer:
#     print("Enter a lower value")
# else:
#     print("You got it right first time!")

# Second Attempt
# if guess < answer:
#     print("Enter a higher value")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you got it right")
#     else:
#         print("Sorry, incorrect guess")
# elif guess > answer:
#     print("Enter a lower value")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you got it right")
#     else:
#         print("Sorry, incorrect guess")
# else:
#     print("You got it right first time!")

# Third Attempt
# if guess != answer:
#     if guess < answer:
#         print("Enter a higher value")
#     else:
#         print("Enter a lower value")
#     guess = int(input())
#     if guess == answer:
#         print("Thats the right answer!")
#     else:
#         print("Sorry, try again!")
# else:
#     print("You got it right first time!")

# Fourth Attempt
if guess == answer:
    print("You got it right first time!")
else:
    if guess < answer:
        print("Enter a higher value")
    else:
        print("Enter a lower value")
    guess = int(input())
    if guess == answer:
        print("That's the right answer!")
    else:
        print("Sorry, try again!")


# Fifth Attemp

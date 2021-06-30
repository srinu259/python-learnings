# import random

# print("Binary Search")
# highest_number = 100
# system_guess = random.randint(1, highest_number)
# print("System guess number is: {} ".format(system_guess))
# guess = 0
# counter = 0
# print("Guess a number between 1 - {}: ".format(highest_number))
#
# while guess != system_guess or counter == 0:
#     guess = int(input())
#     counter += 1
#     if guess < system_guess:
#         print("Guess higher number: ")
#     elif guess > system_guess:
#         print("Guess lower number: ")
#
# print("You guessed {} in {} round(s) ".format(system_guess, counter))


print("Binary Search")
highest_number = 10000
guess_a_number = int(input("Guess a number between 1 and {} : ".format(highest_number)))
low_number = 1
mid_number = (1 + highest_number) // 2
start_number = low_number
end_number = highest_number
counter = 0
if guess_a_number == start_number or guess_a_number == end_number or guess_a_number == mid_number:
    counter = 1
else:
    while guess_a_number != mid_number:
        counter += 1
        if guess_a_number < mid_number:
            print("Guess is lower than mid number :", end=" ")
            print("Low number: {} Mid number: {} High number: {} ".format(start_number, mid_number, end_number))
            end_number = mid_number
            mid_number = (start_number + end_number) // 2

        elif guess_a_number > mid_number:
            print("Guess is higher than mid number:", end=" ")
            print("Low number: {} Mid number: {} High number: {} ".format(start_number, mid_number, end_number))
            start_number = mid_number
            mid_number = (start_number + end_number) // 2

print("Sytem guessed {} in {} round(s) ".format(guess_a_number, counter))
"""
1-100
guess=30|low=1|high=100|mid=50
counter1|guess < mid|low=1|high=50|mid=25
counter2|guess > mid|low=25|high=high|mid=37
counter3|guess < mid|low=
"""



#     guess = int(input())
#     counter += 1
#     if guess < system_guess:
#         print("Guess higher number: ")
#     elif guess > system_guess:
#         print("Guess lower number: ")
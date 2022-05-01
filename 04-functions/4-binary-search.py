import random


def get_int(message: str) -> int:
    print(message)
    while True:
        num = input(": ")
        if num.isnumeric():
            return int(num)


def binary_search(low: int = 0, high: int = 0, guess: int = 0) -> int:
    loop = 0
    mid = (low + high)//2
    while True:
        loop += 1
        if low < guess < mid:
            high = mid
            mid = (low + high)//2
        elif mid < guess < high:
            low = mid
            mid = (low + high)//2
        elif low == guess or high == guess or mid == guess:
            break
    return  loop


# low_num = get_int("Enter start number")
# high_num = get_int("Enter end number")
low_num = 1
high_num = 100
max_guesses = 0
correct_count = 0

for i in range(low_num, high_num+1):
    guess_num = random.randint(low_num, high_num)
    rounds = binary_search(low_num, high_num, guess_num)
    print("Round {}: {} is guessed in {} rounds".format(i, guess_num, rounds))

    if rounds > max_guesses:
        max_guesses, correct_count = rounds, 1
        # print("max_guesses: {} correct_count: {}".format(max_guesses, correct_count))
    elif rounds == max_guesses:
        correct_count += 1
        # print("correct_count: {}".format(correct_count))

print("I guesses without being told {} times. Max {} guesses".format(correct_count, rounds))





import random2 as r

def sum_eo(n, t):
    total = 0

    if n <= 0:
        return -1

    if not t in ('e', 'o'):
        return -1

    for num in range(n):
        if t == 'e' and num%2 == 0:
            total += num
        elif t == 'o' and num%2 != 0:
            total += num

    # return total


print(sum_eo(10, 'e'))
print(sum_eo(7, 'o'))
print(sum_eo(5, 'spam'))


def sum_numbers(*args: float) -> float:
    """
    Returns sum of the numbers
    :param args: pass arbitary number of arguments
    :return: sum of number
    """
    return sum(args)


print(sum_numbers(1, 2, 3))
print(sum_numbers(1.1, 2.2, 5.5))
# print(sum_numbers('a'))

def multiply(x, y):
    return x*y
print(multiply(3, 4))

def is_palindrome(s):
    x = s[::-1]
    return s.casefold() == x.casefold()
print(is_palindrome("Radar"))

def is_sent_palindrome(sentence: str):
    stc = ""
    for st in sentence:
        if st.isalnum():
            stc = stc + st
    rev_sent = stc[::-1]
    print(rev_sent)
    return stc.casefold() == rev_sent.casefold()
sen = "The quick brown fox \txaof nworb kciuq ehT"
print(is_sent_palindrome(sen))

def is_int(n: str):
    if n.isnumeric():
        return True
    else:
        return False
print(is_int("A"))

# def guessf(num: int):
#     to_guess = 100
#     if num > to_guess:
#         print("Guess lower number: ")
#     elif num < to_guess:
#         print("Guess higher number: ")
#     else:
#         print("You got it right")
#
# guess = int(input("Guess a number: "))
# while True:
#     guessf(guess)
# print(guessf(guess))


def is_palindrome(str):
    if str.casefold() == str.casefold()[::-1]:
        print(f"{str} is palindrome")
    else:
        print(f"{str} is NOT palindrome")


is_palindrome("MADAm")

sntc = "The quick brown fox \t xof nworb kciuq eht"


def is_sntc_palindrome(sntc):
    s2 = ""
    for s1 in sntc:
        if s1.isalnum():
            s2.join(s1)
    if s2.casefold() == s2.casefold()[::-1]:
        print(f"{sntc} is palindrome")
    else:
        print(f"{sntc} is NOT palindrome")


# is_sntc_palindrome(sntc)
#
# ans = 289
# guess = int(input("Guess number between 1 - 500: "))
#
#
# def guessf(guess: int):
#     while True:
#         if guess > ans:
#             print("Guess a lower number")
#             guess= int(input(": "))
#         elif guess < ans:
#             print("Guess a higher number")
#             guess = int(input(": "))
#         else:
#             print(f"You got it, the guess is {ans}")
#             break
#
#
# guessf(guess)

seq1 = (1, 2, 3, 4, 5)
print(seq1, sep= " : ")
print(*seq1)
print(*seq1, sep=' : ')


t_low_num = 1
t_high_num = 100


def test_run_binary_search(t_low_num1: int, t_high_num1: int):
    for i in range(t_low_num1, t_high_num1):
        t_num1 = r.randint(t_low_num1, t_high_num1)
        # print(t_low_num1, t_high_num1, t_num1)
        rnd1 = test_binary_search(t_low_num1, t_high_num1, t_num1)
        print(f"Round {i} random number: {t_num1} guessed in {rnd1} rounds")


def test_binary_search(t_low_num2: int, t_high_num2: int, t_num2: int):
    t_mid_num2 = (t_low_num2+t_high_num2)//2
    rnd = 0
    while True:
        rnd = rnd+1
        if t_mid_num2 < t_num2 < t_high_num2:
            t_low_num2 = t_mid_num2
            t_mid_num2 = (t_low_num2+t_high_num2)//2
        elif t_low_num2 < t_num2 < t_mid_num2:
            t_high_num2 = t_mid_num2
            t_mid_num2 = (t_low_num2+t_high_num2)//2
        elif t_num2 == t_low_num2 or t_num2 == t_high_num2 or t_num2 == t_mid_num2:
            return rnd


test_run_binary_search(t_low_num, t_high_num)
# test_binary_search(1, 100, 100)


def test_factorial(num: int) -> int:
    rslt = 1
    for i in range(num):
        rslt = rslt * num
        num = num - 1
    return rslt


print(test_factorial(6))


def test_fibonnaci_series(n: int):
    # n p n p
    # 0 1 1 2 3 5
    fc = ""
    first_num = 0
    second_num = 1
    series = [0, 1]

    if n >= 1:
        print([0])

    if n >= 2:
        print([0, 1])

    if n >= 3:
        for i in range(n-2):
            third_num = first_num + second_num
            series.append(third_num)
            first_num = second_num
            second_num = third_num
            print(series)


test_fibonnaci_series(15)


def test_is_fizz_buzz(n: int):
    if n%3 == 0 and n%5 == 0:
        return "fizz buzz"
    elif n%3 == 0:
        return "fizz"
    elif n%5 == 0:
        return "buzz"
    else:
        return n


# n = input("Enter the number: ")
n = "25"
if not n.isnumeric():
    print("Incorrect number, start program again")
else:
    for i in range(int(n)):
        rslt = test_is_fizz_buzz(i)
        print(f"{i} is {rslt}")


def is_leap_year(year: int) -> bool:
    if year%4 == 0:
        if year%100 != 0:
            return True
        elif year%100 == 0 and year%400 == 0:
            return True
        else:
            return False
    else:
        return False


for i in range(1981, 2050):
    print(f"{i} is leap year - {is_leap_year(i)}")

#               0  1  2  3  4  5  6  7  8  9  10
num_sequence = (1, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8)
seq1 = []
seq2 = []
skip = "N"
for i in range(len(num_sequence)-1):
    if num_sequence[i] == num_sequence[i+1]:
        seq2.append(num_sequence[i])
        skip = "Y"
    else:
        if skip == "N":
            print(num_sequence[i])
            seq1.append(num_sequence[i])
        else:
            skip = "N"

print(seq1)
print(seq2)


p1 = [("t1", 4), ("t2", 8), ("t3", 2), ("t4", 6)]
p2 = [("t1", 2), ("t2", 6), ("t3", 1), ("t4", 4)]

c_p = [("p1", p1), ("p2", p2)]
fast_proc = ""
taskId = ""
time = ""

for proc_name, proc in c_p:
    for tasks in proc:
        if time == "":
            time = tasks[1]
            taskId = tasks[0]
            fast_proc = proc_name
        elif time <= tasks[1]:
            pass
        else:
            time = tasks[1]
            taskId = tasks[0]
            fast_proc = proc_name
print(fast_proc, taskId, time)


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

    return total


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

def guessf(num: int):
    to_guess = 100
    if num > to_guess:
        print("Guess lower number: ")
    elif num < to_guess:
        print("Guess higher number: ")
    else:
        print("You got it right")

guess = int(input("Guess a number: "))
while True:
    guessf(guess)
print(guessf(guess))
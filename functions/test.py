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





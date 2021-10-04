def fibonnaci(n: int = 0) -> list:
    """
    Returns the nth series of fibonacci numbers

    :param n: number of series you want to return
    :return: return the fibonacci series
    :raises ValueError: only for documentation, nothing to raise
    """
    num1, prev_num = 0, 1
    series = [0, 1, 1]
    total = 1
    # 1 2 3 4 5 6 7
    # 0 1 1 2 3 5 8
    if n <= 0:
        return None
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        for i in range(n-3):
            old_num = total
            total = total+prev_num
            prev_num = old_num
            series.append(total)
    return series


print(fibonnaci(0))
print(fibonnaci(1))
print(fibonnaci(2))
print(fibonnaci(3))
print(fibonnaci(4))
print(fibonnaci(-1))

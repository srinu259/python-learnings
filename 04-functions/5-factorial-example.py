def factorial(n: int = 0) -> int:
    '''
    Return factorial of a number
    :param n: factorial to calculate
    :return: factorial
    '''
    if n == 0:
        return 1
    else:
        product = 1
        for i in range(1, n+1):
            product *= i
        return product


for k in range(10):
    print("{} factorial is {}".format(k, factorial(k)))
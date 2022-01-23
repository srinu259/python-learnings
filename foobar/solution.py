import math


def solution(idx: int = 0) -> int:
    min_number = 1
    max_number = 10001
    prime = 2
    prime_flag = False

    for i in range(2, max_number):
        sqrt = round(math.sqrt(i))
        for j in range(2, sqrt + 1):
            if i % j == 0:
                prime_flag = False
                break
            else:
                prime_flag = True
        if prime_flag:
            prime = f"{prime}{i}"
        prime_flag = False

    minion_ids = list(range(1, 1001))
    first_index = idx
    last_index = first_index + 5
    # print(prime[first_index:last_index:1])
    return prime[first_index:last_index:1]


print(solution(0))
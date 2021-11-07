def is_leap(year) -> bool:
    leap = False

    # Write your logic here
    if year % 4 == 0 and year % 100 == 0 and year % 400 ==0:
        leap = True
    elif year % 4 == 0 and year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True

    return leap


# year = int(input())
year = [1992, 2000, 2400, 1800, 1900, 2100, 2200, 2300, 2500]

for i in year:
    print(i, is_leap(i))
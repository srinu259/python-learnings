first_number = int(input("Enter the first number: "))
last_number = int(input("Enter the last number: "))
guess_number = int(input("Enter the number you guessed: "))

if last_number <= first_number or guess_number < first_number or guess_number > last_number:
    print("You are not interested in playing the game")
else:
    print(f"Beginning binary search to guess your number {guess_number}")
    i = 1

    if guess_number == first_number or guess_number == last_number:
        print(f"No need of binary search! The number {guess_number} is guessed in round: {i}")

    else:
        i += 1
        mid_number = (first_number + last_number)//2
        while guess_number != mid_number:
            i += 1
            if guess_number < mid_number:
                last_number = mid_number
                mid_number = (first_number + last_number)//2
            else:
                first_number = mid_number
                mid_number = (first_number + last_number)//2
        print(f"Binary search guessed your number {guess_number} in round: {i}")




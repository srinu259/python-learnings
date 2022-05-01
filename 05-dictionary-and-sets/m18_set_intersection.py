from m17_primes_and_squares import squares_generator, primes_generator

even = set(range(0, 50, 2))
odd = set(range(1, 50, 2))
print(even)
print(odd)
print(set(squares_generator(50)))
print(set(primes_generator(50)))

# Get odds that are perfect square
# Get odds that are primes
# Get evens that are perfect square
# Get evens that are primes

odds_perfect_square = odd.intersection(set(squares_generator(50)))
print(odds_perfect_square)
odds_primes = odd.intersection(set(primes_generator(50)))
print(odds_primes)
print(even & set(squares_generator(50)))
print(even & set(primes_generator(50)))
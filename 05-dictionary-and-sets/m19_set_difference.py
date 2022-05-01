from m17_primes_and_squares import primes_generator, squares_generator

evens = set(range(0, 50, 2))
odds = set(range(1, 50, 2))
squares = set(squares_generator(100))
primes = set(primes_generator(100))
print(evens)
print(odds)
print(squares)
print(primes)

print(odds.difference(primes))
print(odds - primes)
# difference are non-commutative
print(primes - odds)
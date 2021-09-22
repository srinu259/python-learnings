# sorted sorts the input and returns the sorted-ouput
# sorted does not change the original input
# whereas sort function modifies the original list

pangram = 'The quick brown fox jumps over laxy dog'
print(sorted(pangram))
print(pangram)

numbers = [1.3, 5.6, 2.3, 4.8, 2.2]
print(sorted(numbers))
print(numbers)

numbers.sort()
print(numbers)

# pangram = 'The quick brown fox jumps over laxy dog'
# sorted_list = sorted(pangram)
# sorted = sorted(pangram)
# text = 'The quick brownie is a humble pie'
# print(sorted(text))
# This gives an error, because of line 18 python rebinded sorted function to a list
# python does not give error for the key words, it will rebind them in the program

# key=str.casefold will sort the characters / list is case-sensitive order
print(sorted(pangram, key=str.casefold))
names = ["John",
         "Annie",
         "eric",
         "sham",
         "Don"]
names.sort(key=str.casefold)
print(names)



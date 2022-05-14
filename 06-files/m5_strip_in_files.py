# strip() strips characters from both the ends
# If no argument is passed to either of strip(), lstrip(), rstrip() space is trimmed
# if an argument is passed, then python will take each and every character
# from either of the end depending on the lstrip or rstrip and trim each character
# if the character is present in list of characters to be trimmed
# in the below example when we are trimming from the left side,
# python takes character by character from left side of the line and
# verifies if the character is present in the list of characters to be trimmed
# if python cannot find a character present in the set of trimmed characters
# then it will stop there.


with open('m4_nirvana_ashtakam.txt') as poem:
    line = poem.readline()
print(line.strip())
print(line.strip().lstrip('I,amno t'))
print(line.strip().rstrip('I,amno t'))

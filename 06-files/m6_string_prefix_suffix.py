# strip validates one character at a time from the string and removes if it exists
# in characters to be removed
# if you need to remove a string either from start|end
# then use removeprefix() / removesuffix() methods
# these methods are only introduced in python 3.9

with open("m4_nirvana_ashtakam.txt") as poem:
    first_line = poem.readline()

print(first_line)
print(first_line.removeprefix("I am not"))
print(first_line.removesuffix("the memory,\n"))
print("-"*80)


# build your own functions if you are in python < 3.9 version
def remove_prefix(string: str, prefix: str) -> str:
    if string.startswith(prefix):
        return string[len(prefix):]
    else:
        return string


def remove_suffix(string: str, suffix: str) -> str:
    if suffix and string.endswith(suffix):   # avoid string[:-0]
        return string[:-len(suffix)]
    else:
        return string


backslash_char = "\\"
print(f"Remove-prefix: {remove_prefix(first_line, 'I am not')}")
print("Remove-suffix: {}".format(remove_suffix(first_line, "the memory,\n")))
# print(f"Remove-suffix: {remove_suffix(first_line, 'the memory,{backslash_char}n')}")

test = "I am not the mind, the intellect, the ego or the memory"
print("abc "+test[:-0])
print((remove_suffix(test, "")))
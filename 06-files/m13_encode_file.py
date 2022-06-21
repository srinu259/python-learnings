# If encoding is not specified, then the program will use the underlying platform encoding
# this is not good, as your program may show different outputs on different platforms
# so the best way is to pass the encoding required when reading or writing to files

with open("m4_nirvana_ashtakam.txt") as poem:
    print(poem.read())

print("-"*20)
with open("m4_nirvana_ashtakam.txt", encoding="utf-8") as poem:
    print(poem.read())
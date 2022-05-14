# open is one of the way to open a file
# not a popular way though
# make sure to close the file, else you might run out of file handlers
# file handlers are handled by OS to keep track of number of open files
# file open will read all the invisible characters like new line char etc
poem = open('m1_invictus_poem.txt', 'r')
for line in poem:
    print(line)
poem.close()

# strip, strips the characters on both the sides
poem = open('m1_invictus_poem.txt', 'r')
print(20*'-')
for line in poem:
    print(line.strip())
poem.close()

# rstrip, strips the characters on the right sides - from the end
poem = open('m1_invictus_poem.txt', 'r')
print(20*'-')
for line in poem:
    print(line.rstrip())
poem.close()

# lstrip, strips the characters on the left sides - from the beginning
poem = open('m1_invictus_poem.txt', 'r')
print(20*'-')
for line in poem:
    print(line.lstrip())
poem.close()

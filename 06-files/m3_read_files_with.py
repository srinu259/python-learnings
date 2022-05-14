# python way to open a file
# python will automatically close the file
# python will do the memory management
with open('m1_invictus_poem.txt', 'r') as poem:
    for line in poem:
        print(line.rstrip())

# readlines method will read the entire file and store as a list
# dont use this for a large file, you may be consuming full memory
with open('m1_invictus_poem.txt', 'r') as poem:
    line = poem.readlines()
print(line)
print(line[-1:0:-1])

for rline in reversed(line):
    print(rline, end='')

# read method reads the entire text as a string
with open('m1_invictus_poem.txt') as poem:
    line = poem.read()
print(line)
print(line[-1:0:-1])

# readline method reads one line at a time
# this is similar to reading file and iterating over the fileobject
# but make sure to include a breaking condition, else you are into infinite loop
with open('m1_invictus_poem.txt') as poem:
    while True:
        line = poem.readline()
        if line.casefold() in 'invictus':
            break
        print(line.rstrip())
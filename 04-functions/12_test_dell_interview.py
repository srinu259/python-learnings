# DELL interview
# Get the first non occurence character in a String

input = "sweetsmile"
# list = ['s', 'w', 'e', 'e', 't', 's']
# emtpy_set = ();
# unique_list = []
# non_unique_list = []

# with python OOB functions
def get_unique_char(string):
    for c in string:
        if string.count(c) == 1:
            return c

# print(get_unique_char(input))

# without python OOB functions
def get_unique_char_custom(string):
    custom_list = list(string)
    unique_list = []
    non_unique_list = []
    upd_unique_list = []
    unique_set = set()
    counter1, counter2 = 0, 0

    for c in custom_list:

        unique_list.append(c)
        upd_unique_list.append(c)
        unique_set.add(c)
        counter1 = len(unique_list)
        counter2 = len(unique_set)

        if counter1 == counter2:
            pass
        else:
            non_unique_list.append(c)
            unique_list.remove(c)
            while True:
                if c in upd_unique_list:
                    upd_unique_list.remove(c)
                else:
                    break
        print(c, unique_list, non_unique_list, upd_unique_list)

    return upd_unique_list
#    print(custom_list)

print(get_unique_char_custom(input))
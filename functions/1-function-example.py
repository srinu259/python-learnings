def multiply(x, y):
    result = x * y
    return result


product = multiply(3, 4)
print(product)


#  function palindrome
def is_palindrome(string):
    reverse_string = string[::-1]
    return string.casefold() == reverse_string.casefold()

string = "Radar"
print("{} is palindrome - {}".format(string, is_palindrome(string)))


# function sentence palindrome
def is_sent_palindrome(sentence):
    new_str = ""
    for s in sentence:
        if s.isalnum():
            new_str = new_str+s;
        else:
            continue

    print(new_str)
    # return new_str.casefold() == new_str[::-1].casefold()
    return is_palindrome(new_str)


sentence = "The quick brown fox \t xof nworb kciuq eht"
print("'{}' is palindrome - {}".format(sentence, is_sent_palindrome(sentence)))
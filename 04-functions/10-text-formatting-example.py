# def formatter(message):
#     screen_width = 80
#     if len(message)-4 > screen_width:
#         print("Length exceeds the printing value")
#     elif message == "*":
#         print("*" * screen_width)
#     else:
#         print("**{}**".format(str(message).center(screen_width-4)))
#
#
# text = "The quick brown fox jumps over lazy dog"
# formatter("*")
# formatter(text)

# default values are provided with =, dont put spaces around equal sign
# Function definition is added inside the function. This is contrast to Java where it is kept outside
def formatter(message="-", screen_width=80):
    '''
    A simple text formatter function
    :param message: The message to format. Default value is `-`
    :param screen_width: Width of the message. Default value is `80`
    :return: Returns the formatted message
    '''
    if len(message)-4 > screen_width:
        raise ValueError("'{}' is more than {}".format(message, screen_width))
    elif message == "*":
        print("*" * screen_width)
    else:
        print("**{}**".format(str(message).center(screen_width-4)))


text = "The quick brown fox jumps over lazy dog"
width = 80
formatter("*") # positional arguments
formatter(text, width)
formatter(screen_width=20) # keyword arguments
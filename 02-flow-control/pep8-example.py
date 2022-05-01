print("The pet shop owner said \"No, no, 'e's uh,...he's resting\".")

# with a \ even though we use """ we don't print in a new line
print("""The pet shop owner said "No, no, \
'e's uh,...he's resting". """)

# python does not like camel case variable names, another_string is python way
anotherString = """This string has been \
split over \
several \
lines"""

print(anotherString)

# not here that we are not escaping \ at a letter
print("C:\\Users\am\\notes.txt")
print(r"C:\\Users\am\\notes.txt")
# r means raw-string. Treat everything as rawstring and all escapecodes are ignored

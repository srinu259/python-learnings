print("Hello, Madhav")
print("Hello, with single/double quotes "
      "I cannot be in new line")
print("""Hello with 3 single/double quotes
 I am in new line""")

# Escape Characters
print('Let\'s look into escape character')
print("Let's look into escape character")
print('Let\'s\tlook\tinto\tescape\tcharacter-tabbed sequence')
print('c:\\Madhav\\Learn\\Python3\\newLang') #Escape the backslash with a backslash

#Get input from user
#name = input("Enter your name")
#print("Hello", name)

#Python is dynamically typed language, so you don't need to declare the variable type
name = 'Madhav'
age = 39    # age is INT
print("Hello", name, "\nAge", age)
print("type(name)", type(name))
print("type(age)", type(age))

age = '39 years' # age is STRING
print("Hello", name, "\nAge", age)
print("type(name)", type(name))
print("type(age)", type(age))

#Python is strongly type language. So there is no implicit conversion of data types
#Python cannot add a STRING and INT. Java can do implicit converstions.
age = 39
#print("Hello "+ name + " Age is " + age)
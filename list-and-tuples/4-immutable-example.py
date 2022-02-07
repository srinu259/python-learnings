# Following data types are immutable in python
# - int
# - float
# - bool
# - str
# - tuple
# - frozenset
# - bytes

# Following below example
# Probably in Java, name will have the same id, its value will be changed
# But in python you bind a value to a variable, so when value changes, id also is changed
# This is how immutable properties behave in python

name = "Python"
another_name = name
print(id(name))
print(id(another_name))

print()
name = "Python 3.x"
another_name = name
print(id(name))
print(id(another_name))
another_name = "Python 3.8"
print(id(another_name))

# Following data types are immutable in python
# - int
# - float
# - bool
# - str
# - tuple
# - frozenset
# - bytes

# Immutable means an object once created with a value set cannot be modified
# In python you bind a value to a variable, so when value changes, id also is changed
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

# similar example to mutable-example, but different results as expected
print()
name = "Python 3.9"
another_name = name
print(name, another_name)
name = "Python 3.10"
print(name, another_name)
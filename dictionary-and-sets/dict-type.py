a = dict(one=1, two=2, three=3)
print(a)

b = {'one': 1, 'two': 2, 'three': 3}
print(b)

c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
print(c)

d = dict([('two', 2), ('one', 1), ('three', 3)])
print(d)

e = dict({'three': 3, 'one': 1, 'two': 2})
print(e)

f = dict({'one': 1, 'three': 3}, two=2)
print(f)

print(a == b == c == d == e == f)

g = {(1, "Nightflight"): 1}
print(g)

# a dictionary key has to be immutable, else it is considered invalid
# h = {(1, ["a", "b", "c"]): 1}
# print(h)


# tuple is always immutable, but if the tuple contains mutable objects, then those objects can be changed
tup1 = (1, ["a", "b"])
#print(hash(tup1))
tup1[1].append("c")
for i in tup1:
    print(i)

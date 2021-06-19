a,b = 12,4
print(a+b)  # 16
print(a-b)  # 8
print(a*b)  # 48
print(a/b)  # 3.0 integer division will give floating point result
print(a//b) # 3 // is for integer division
print(a%b)  # 0 % is for reminder or modulus

print()
for i in range(1, 4):
    print(i)

print()
for i in range(1, a//b):  # range only works for integer and not floating results
    print(i)

# a * unpacks/packs a sequence
# * indicates python should get an unpacked tuple and python will pack it
# if *args represent an unpacked tuple, args will represent a packed tuple
seq1 = (0, 1, 2, 3, 4, 5)
print(seq1, sep=";")
print(*seq1, sep=";")
print(0, 1, 2, 3, 4, 5, sep=";")


def unpack(*seq: tuple) -> None:
    print()
    print(seq)
    for x in seq:
        print(x)


unpack(1, 2, 3, 4, 5)
unpack()

###########


def args(p1, p2, *args, k, **kwargs):
    print("positional or keyword arguments  - {}, {}".format(p1, p2))
    print("var-positional arguments (*args) - {}".format(args))
    print("keyword argument ............... - {}".format(k))
    print("var-keyword argument ........... - {}".format(kwargs))


args(1, 2, 3, 4, 5, k=6, k1=7, k2="abc")

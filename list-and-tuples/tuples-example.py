temp = ("a", "simple", "tuple",)
print(temp)

# paranthesis around the string will make it a tuple
print("a", "simple", "tuple",)
print(("a", "simple", "tuple",))
      
# tuples are immutable, the below code will fail
test = ("a", "b", "c")
#test.append("d")

# however tuples can be modified into list
test1 = list(test)
test1.append("d")
print(test1)

# unpacking tuples
a = b = c = d = e = f = 12
print(c)

x, y, z = 1, 2, 3
print(x, y, z)

data = (3, 4, 5)
x, y, z = data
print(x, y, z)

# unpacking lists
test2 = [6, 7, 8]
# test2.append(9) # this will break the code
x, y, z = test2
print(x, y, z)

# enumerate function returns a tuple in each loop of iteration
for t in enumerate("abcdefgh"):
    index, character = t
    print(index, character)

albums = [
    ("Thriller", "Michael Jackson", 1982),
    ("Bad", "Michael Jackson", 1987),
    ("Blood On Dance Floor", "Michael Jackson", 1992),
    ("History", "Michael Jackson", 1996),
    ("Invincible", "Michael Jackson", 2002)
]

for album in albums:
    name, artist, year = album
    #print("Album: {}, Artist: {}, Year: {}".format(album[0], album[1], album[2]))
    print("Album: {}, Artist: {}, Year: {}".format(name, artist, year))

# nested tuples example
albums = (
    ("Thriller", "Michael Jackson", 1982,
     [(1, "Beat It"),
      (2, "Billie Jean"),
      (3, "Human Nature"),
      (4, "P.Y.T. (Pretty Young Thing)"),
      (5, "The Lady in My Life")
    ]),
    ("Bad", "Michael Jackson", 1987,
     [(1, "Bad"),
      (2, "The Way You Make Me Feel"),
      (3, "Dirty Diana"),
      (4, "Smooth Criminal"),
      (5, "Man in the Mirror"),
      (6,  "I Just Can't Stop Loving You")
    ]),
    ("Blood On Dance Floor", "Michael Jackson", 1992,
     [(1, "Blood on the Dance Floor"),
      (2, "Morphine"),
      (3, "Superfly Sister"),
      (4, "Money"),
      (5, "2 Bad"),
      (6, "Stranger in Moscow"),
      (7, "Earth Song"),
      (8, "You Are Not Alone")
    ]),
    ("History", "Michael Jackson", 1995,
     [(1, "Scream"),
      (2, "They Don't Care About Us"),
      (3, "Stranger in Moscow"),
      (4, "Come Together"),
      (5, "You Are Not Alone")
      ]),
    ("Invincible", "Michael Jackson", 2002,
     [(1, "You Rock My World"),
      (2, "Butterflies"),
      (3, "Speechless"),
      (4, "2000 Watts"),
      (5, "You Are My Life")]
     ))

for name, artist, year, songs in albums:
    print(name, artist, year, songs)

print()
print(albums[2])
print(albums[2][3])
print(albums[2][3][1])
print(albums[2][3][1][1])

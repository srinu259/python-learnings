import random

data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac - Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

flowers = []
shrubs = []

# write your code here
for info in data:
    if "flower".casefold() in info.casefold():
        flowers.append(info.removesuffix(" - Flower".casefold()))
    else:
        shrubs.append(info)

print(flowers)
print(shrubs)

#######################
# check = '012345689, '
# temp = input("Enter 3 numbers separated by comma: ")
# new_temp = temp.split(",")
#
# a = int(new_temp[0])
# b = int(new_temp[1])
# c = int(new_temp[2])
# print(a+b-c)

#######################
albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975,
     [
         (1, "Welcome to my Nightmare"),
         (2, "Devil's Food"),
         (3, "The Black Widow"),
         (4, "Some Folks"),
         (5, "Only Women Bleed"),
     ]
     ),
    ("Bad Company", "Bad Company", 1974,
     [
         (1, "Can't Get Enough"),
         (2, "Rock Steady"),
         (3, "Ready for Love"),
         (4, "Don't Let Me Down"),
         (5, "Bad Company"),
         (6, "The Way I Choose"),
         (7, "Movin' On"),
         (8, "Seagull"),
     ]
     ),
    ("Nightflight", "Budgie", 1981,
     [
         (1, "I Turned to Stone"),
         (2, "Keeping a Rendezvous"),
         (3, "Reaper of the Glory"),
         (4, "She Used Me Up"),
     ]
     ),
    ("More Mayhem", "Imelda May", 2011,
     [
         (1, "Pulling the Rug"),
         (2, "Psycho"),
         (3, "Mayhem"),
         (4, "Kentish Town Waltz"),
     ]
     ),
]

# Add your code below this comment.
print(albums[1][3][5][1])
print(albums[2][2])
print(albums[3][3][3][0])
print(albums[2][3][1])


# print the following pattern
# *****
# ****
# ***
# **
# *

for i in range(5, 0, -1):
    print('*'*i)


def get_weather_data():
    return random.randrange(90, 110)


# list comprehensions: without walrus operator
hot_temps = [temp for temp in range(20) if get_weather_data() >= 100]
print(hot_temps)

# list comprehensions: walrus operator
hot_temps = [temp for _ in range(20) if (temp := get_weather_data()) >= 100]
print(hot_temps)


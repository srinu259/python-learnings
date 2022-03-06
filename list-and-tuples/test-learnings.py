test = sorted('246733358901')
print(test)

test = sorted('238956efd#@^*$')
print(test)

# spam challenge
menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

# for items in menu:
#     while items.__contains__("spam"):
#         items.remove("spam")
#     print(items)

for items in menu:
    for i in range(len(items)-1, -1, -1):
        if items[i] == "spam":
            del items[i]
    print(items)

# for items in menu:
#     for i in range(0, len(items)):
#         if items[i] == "spam":
#             items.remove("spam")
#             # del items[i]
#     print(items)

numbers = "9,234,563,123,567,036,857"
separator = ","
value = " ".join(" " if char in separator else char for char in numbers).split()
print(value)
print(float("-inf"))


def find_max(nums):
    max_num = float("-inf") # smaller than all other numbers
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num


print(find_max([1, 12, 3]))

# spam challenge
menu1 = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

for item_list in menu1:
    for item in item_list:
        if item == "spam":
            item_list.remove("spam")
            break

print(menu1)
print(menu)

temp = '9 234,563,123,567,036,857'
print(temp.split())

temp = '9,234,563,123,567,036,857'
print(temp.split(','))

temp_list = []
for temp_item in temp[:]:
    if temp_item == ',':
        temp_list.append(' ')
    else:
        temp_list.append(temp_item)
print(temp_list)

# #use list-comprehension to do the same code
# for temp_item in temp[:]
# if temp_item == ',' then ' ' else temp_item

# spam challenge
menu2 = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"]
]

for new_menu in menu2:
    for new_item in new_menu[::-1]:
        if new_item == "spam":
            new_menu.remove("spam")
    print(new_menu)
print(menu2)

menu3 = ["spam", "egg", "spam", "spam", "bacon", "spam"]
print(menu3[::-1])
for i in range(len(menu3)-1, -1, -1):
    print(menu3[i])

numbers = "9,234,563,123,567,036,857"
sep = ","
n_list = []
for n in numbers:
    if n in sep:
        n = " "
    else:
        n = int(n)
    n_list.append(n)
print(n_list)

numbers = "9,234,563,123,567,036,857"
num_list = []
for n in numbers.split(","):
    num_list.append(int(n))
print(num_list)

separators = ","
value = " ".join(char if char not in separators else " " for char in numbers).split()
print(value)


selected_parts = []
computer_parts = ["Computer",
                   "Monitor",
                   "Keyboard",
                   "Mouse",
                   "Floppy",
                   "HDMI Cable"
                   ]

print("Please select the parts you need from the below list:")
for part_id, part in enumerate(computer_parts):
    print("{0}. {1}".format(part_id+1, part))
print("0. Exit")
# choice = input()
choice = "0"
print(f"{choice}")

while choice != '0':
    if choice in '123456':
        if computer_parts[int(choice)-1] in selected_parts:
            selected_parts.remove(computer_parts[int(choice)-1])
        else:
            selected_parts.append(computer_parts[int(choice)-1])
    choice = input()
print(selected_parts)

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

while True:
    print("Select an album to play: ")
    for album_id, album in enumerate(albums):
        print("{0}. {1}".format(album_id+1, album[0]))
    print("0. Exit")
    album_id = input()
    songlist = ""
    if album_id in '12345':
        print(f"Select song to play from album: {albums[int(album_id)-1][0]}")
        print("-"*20)
        for song_id, song in albums[int(album_id)-1][3]:
            print("{0}. {1}".format(song_id, song))
            songlist = songlist + str(song_id)
        song_id = input()

        if song_id in songlist:
            print(f"Playing song: {albums[int(album_id)-1][3][int(song_id)-1][1]}....")
            print("="*30)
        else:
            print("Invalid choice, start with album again")
        print("="*30)
    elif album_id == 0:
        break
    else:
        print("Invalid choice, select again")
        print("="*30)


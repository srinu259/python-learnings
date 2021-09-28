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

# print("Enter the album number you would like to play: ")
# for index, name in enumerate(albums):
#     print(str(index+1)+".", name[0])
# album_number = int(input())
#
# if not ( 0 < album_number <= len(albums)):
#     print("Incorrect number selected, exiting now")
#     exit(-1)
#
# album_name = albums[album_number-1][0]
#
# print("Enter the song you would like to listen: ")
# for song_number, song in albums[album_number-1][3]:
#     print(str(song_number)+".", song)
# song_number = int(input())
#
# if not ( 0 < song_number <= len(albums[album_number-1][3])):
#     print("Incorrect number selected, exiting now")
#     exit(-2)
#
# print("Playing '{}' from album '{}'".format(song, album_name))

ALBUM_NAME_INDEX = 0
SONG_LIST_INDEX = 3
SONG_NAME_INDEX = 1


while True:
    print("Enter the album number you would like to play: ")
    for index, (name, artist, year, songs) in enumerate(albums):
        print("{}. {}".format(index+1, name))
    album_number = int(input())

    if 1 <= album_number <= len(albums):
        song_list = albums[album_number-1][SONG_LIST_INDEX]
    else:
        print("Exiting now. Good day!")
        break

    album_name = albums[album_number-1][ALBUM_NAME_INDEX]
    print("Enter the song you would like to listen: ")

    for track, song in song_list:
        print("{}. {}".format(track, song))

    song_number = int(input())
    if 1 <= song_number <= len(song_list):
        print("Playing '{}' from album '{}'".format(song_list[song_number-1][SONG_NAME_INDEX], album_name))
    else:
        print("Invalid choice, try again!")
        # print("Exiting now. Good day!")
        # break
    print("="*50)
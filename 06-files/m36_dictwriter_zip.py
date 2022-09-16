import csv

albums = [
    ("Thriller", "Michael Jackson", 1982),
    ("Bad", "Michael Jackson", 1987),
    ("Blood On Dance Floor", "Michael Jackson", 1992),
    ("History", "Michael Jackson", 1996),
    ("Invincible", "Michael Jackson", 2002)
]

header = ['Album', 'Artist', 'Year']
file_to_write = 'm37_albums_list.csv'
with open(file_to_write, 'w', encoding='utf-8', newline='') as data:
    writer = csv.DictWriter(data, fieldnames=header)
    writer.writeheader()
    for album in albums:
        # print(album)
        zip_objects = zip(header, album)
        # print(zip_objects)
        # for things in zip_objects:
        #     print(things)
        album_dict = dict(zip_objects)
        print(album_dict)
        writer.writerow(album_dict)

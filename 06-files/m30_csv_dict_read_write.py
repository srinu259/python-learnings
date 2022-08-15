import csv

file_read = 'm19_olympic_medals_2020.csv'
file_write = 'm31_olympic_medals_2020_data.txt'
ordering = ['Country', 'Gold', 'Silver', 'Bronze', 'Rank']

with open(file_read, 'r', encoding='utf-8') as olympic_read, \
        open(file_write, 'w', encoding='utf-8') as olympic_write:
    reader = csv.DictReader(olympic_read)
    writer = csv.writer(olympic_write)
    print("import csv", file=olympic_write)
    print("", file=olympic_write)
    print("medals_table = [", file=olympic_write)
    for row in reader:
        new_dict = {}
        print(row)
        for key in ordering:
            value = row[key]
            if value.isnumeric():
                new_dict[key.casefold()] = int(value)
            else:
                new_dict[key.casefold()] = value
        print(f"    {new_dict}", file=olympic_write)
    print("]", file=olympic_write)



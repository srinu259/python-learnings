import csv

file_to_open = "m19_olympic_medals_2020.csv"
with open(file_to_open, encoding='utf-8', newline='') as file:
    reader = csv.reader(file)
    header = file.readline().strip('\n').split(',')
    print(f'Header Row: {header}')
    for row in reader:
        print(row)
    # line = file.readline()
    # while line:
    #     print(line)
    #     line = file.readline()



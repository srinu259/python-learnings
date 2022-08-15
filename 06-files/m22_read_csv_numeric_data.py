# quoting provides you the flexibility to set the numeric value in the data
# by default csv.reader converts every field to string, this may not be ideal situation if you need numbers
# csv.QUOTE_NONNUMERIC means all non-numeric columns are converted to numbers (float)
# So if you have a string column that does not have quotes, it will lead to error
import csv

file_name = "m21_cereal_grains.csv"
with open(file_name, 'r', encoding='utf-8') as file:
    reader = csv.reader(file, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        print(row)
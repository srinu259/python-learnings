import csv

# csv can read with any delimiter, not with just comma
# just use the delimiter option and provide the delimiter in your case

file_name = "m7_country_info.txt"
with open(file_name, 'r', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter='|')
    for row in reader:
        print(row)

print("*"*80)

# there can be cases where you have different delimiters in different files
# in such cases, you can use dialect
# csv has Sniffer class that helps you to identify the delimiter in your data
# in the below example we are loading the full data and passing to the Sniffer
# we can also pass a sample data instead of full data to identify the delimiter

file_name = "m7_country_info.txt"
with open(file_name, 'r', encoding='utf-8') as file:
    country_data = file.read()
    file.seek(0)
    country_dialect = csv.Sniffer().sniff(country_data)
    reader = csv.reader(file, dialect=country_dialect)
    for row in reader:
        print(row)

print("*"*80)
# Get all the attributes of the dialect
# dialect is an object that encompasses all the csv properties
attributes = ['delimiter', 'quoting', 'quotechar', 'escapechar',
              'doublequote', 'lineterminator', 'skipinitialspace']
for attribute in attributes:
    print(f"{attribute}: {getattr(country_dialect, attribute)}")

# repr represents printable representation of an object
print("*"*80)
for attribute in attributes:
    print(f"{attribute}: {repr(getattr(country_dialect, attribute))}")

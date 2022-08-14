import csv

file_name = 'm21_cereal_grains.csv'
with open(file_name, 'r', newline='') as cereal:
    reader = csv.DictReader(cereal)
    for row in reader:
        print(row)


# Country challenge. Get capital by country name or country code
print()
print("*"*80)
print()

country_file_name = 'm7_country_info.txt'
countries = {}
with open(country_file_name, 'r', newline='') as country:
    sample_data = ''
    for row in range(3):
        sample_data += country.readline()
    country.seek(0)
    country_dialect = csv.Sniffer().sniff(sample_data)
    reader = csv.DictReader(country, dialect=country_dialect)
    for row in reader:
        countries[row['Country'].casefold()] = row
        countries[row['CC'].casefold()] = row

print(countries)
cntry = input("Enter the country whose capital is required: ")
if cntry.casefold() in countries:
    print(f"Capital of {cntry} is {countries[cntry.casefold()]['Capital']}")
else:
    print("No such country exists")
import csv

file_name = 'm7_country_info.txt'
with open(file_name, 'r', encoding='utf-8') as country:

    # a dialect cannot be created by calling csv.dialect. Program will crash if you do this
    # instead we have to use one of the existing dialects of an object
    # here we are using excel
    country_dialect = csv.excel
    country_dialect.delimiter = '|'

    # Goal is to update the header and ensure all of them are in lower-case
    # Country|Capital|CC|CC3|IAC|TimeZone|Currency to
    # country|capital|cc|cc3|iac|timezone|currency

    firstLine = country.readline().strip('\n').split(country_dialect.delimiter)
    header_row = []
    for header in firstLine:
        header_row.append(header.casefold())
    reader = csv.DictReader(country, dialect=country_dialect, fieldnames=header_row)
    countries = {}
    for row in reader:
        countries[row['country']] = row
        countries[row['cc']] = row

while True:
    select_country = input("Enter the country name to get the capital: ")
    if select_country in countries:
        print(f"Capital of {select_country} is {countries[select_country]['capital']}")
    elif select_country.casefold() == 'quit':
        break

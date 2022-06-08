country_file_name = "m7_country_info.txt"

countries = {}
with open(country_file_name) as country:
    country.readline()
    for data_row in country:
        # print the entire row
        # print(data)
        # print the entire row by stripping new line characters
        # print(data.strip())
        data = data_row.strip().split("|")
        country, capital, cc, cc3, iac, timezone, currency = data
        # print(country, capital, cc, cc3, iac, timezone, currency, sep="\n\t")
        country_dict = {
            "name": country,
            "capital": capital,
            "code": cc,
            "code3": cc3,
            "dialing_code": iac,
            "timezone": timezone,
            "currency": currency
        }
        print(country_dict)
        # countries[country_dict["name"].casefold()] = country
        # We can have multiple keys added to dictionary like country, country_code etc
        countries[country.casefold()] = country_dict
        countries[cc.casefold()] = country_dict
        # Alternatively create a new dictionary with country, country_code etc
        # country_code[cc.casefold] = country_dict


print(countries)
import io
import sys

# we are redirecting output to a in-memory text instead of printing it
text_trap = io.StringIO()
sys.stdout = text_trap
from m9_parse_country_data import countries

sys.stdout = sys.__stdout__
# In this example we can either enter Country or Country Code (cc)
while True:
    country_name = input("Enter the country for which capital is required: ")
    if country_name.casefold() in countries:
        print(f"The {country_name} capital is {countries[country_name.casefold()].get('capital')}")
    else:
        break


# Print the countries that do not have a capital city
print(countries)
for key, value in countries.items():
    if not value['capital']:
        print(f"Country {key} does not have a capital")
    else:
        print(f"Country {key} capital is {value['capital']}")
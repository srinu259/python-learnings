# https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/
import json

languages = [
    ["C", 1999],
    ["C++", 2000],
    ["Java", 2001],
    ["JSP", 2004],
    ["R", 2011],
    ["Python", 2022]
]

# json.dump is used for creating a JSON file
# here we create a new file m15_lang.json
with open("m15_lang.json", "w") as lang:
    json.dump(languages, lang)

# json.load is for reading json file
with open("m15_lang.json", "r") as lang_read:
    data = json.load(lang_read)
print(data)
# https://www.ncei.noaa.gov/cag/global/time-series/globe/land_ocean/1/5/1880-2022/data.json
# In this example we will read the data from internet
# once the data is available in the object, it is as good as reading from a file
# we can use read, readlines(), readline()
import json
import urllib.request

weather_data_link = 'https://www.ncei.noaa.gov/cag/global/time-series/globe/land_ocean/1/5/1880-2022/data.json'
with urllib.request.urlopen(weather_data_link) as streaming_data:
    data = streaming_data.read().decode('utf-8')

# json.loads() will work on a string object, data above is a str object
# json.load() will work on a JSON document read from a file
json_data = json.loads(data)
print(json_data['description'])
for key, value in json_data['data'].items():
    print(f"{key} ... {value}")

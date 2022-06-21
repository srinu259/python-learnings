import json

file_name = 'm16_weather_anomalies_data.json'
with open(file_name, encoding='utf-8') as data:
    climate_data = json.load(data)

print(climate_data['description'])
for key, value in climate_data['data'].items():
    year, temp = int(key), float(value)
    print(f"{year} ... {temp:5.2f}")
print("*"*80)
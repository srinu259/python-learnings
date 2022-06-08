country_file_name = "m7_country_info.txt"

with open(country_file_name) as country:
    for data in country:
        # print the entire row
        # print(data)
        # print the entire row by stripping new line characters
        # print(data.strip())
        print(data.strip().split("|"))
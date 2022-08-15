import csv

# In this example we will add an initial space in one of the columns in the cereals data
# without csv_dialect.skipinitialspace, data will contain space
# with the flag added we can do the clean up as required
file_name = "m25_cereal_grains.txt"
with open(file_name) as cereals:
    test_data = ""
    for line in range(3):
        test_data += cereals.readline()
    print(test_data)
    csv_dialect = csv.Sniffer().sniff(test_data)
    csv_dialect.skipinitialspace = False
    cereals.seek(0)

    reader = csv.reader(cereals, dialect=csv_dialect)
    for read in reader:
        print(read)

        # This below part of code is important
        # If the file has already double quotes around the columns, then csv_dialect will not work
        # this is because csv_dialect thinks it is string column

        # col1 = []
        # for col in read:
        #     col1.append(col.strip())
        # print(col1)

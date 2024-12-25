import time
import cx_Oracle
import json
from jinja2 import Template

def execute():

    db_config = {}
    db_config["db_user"] = "pdbadmin"
    db_config["db_password"] = "qadb"
    db_config["db_hostname"] = "localhost"
    db_config["db_port"] = "1521"
    db_config["db_service_name"] = "qadb"
    db_config["client_lib_dir"] = r"C:\Users\am\Downloads\instantclient-basic-windows.x64-23.6.0.24.10\instantclient_23_6"

    sql = "SELECT * FROM PDBADMIN.STAFF_DET_V WHERE ROWNUM <= 200"
    person_list = []
    person_json = """{
            "Upn": "{{ data[0] }}",
            "Email": "{{ data[1] }}",
            "FirstName": "{{ data[2] }}",
            "LastName": "{{ data[3] }}"
    }"""

    # client_lib_dir = "C:\Users\am\Downloads\instantclient-basic-windows.x64-23.6.0.24.10\instantclient_23_6"
    # connection = "pdbadmin/qadb@localhost:1521/qadb"

    try:
        db_connection = get_db_connection(db_config)
        template = Template(person_json)
        with db_connection.cursor() as cursor:
            cursor.arraysize = 256
            for row_data in cursor.execute(sql):
                rendered_form = (template.render(data=row_data))
                person_list.append(json.loads(rendered_form))
        release_db_connection(db_connection)
        size_in_kb = str(person_list.__sizeof__()/1000)
        print("Length of the array:", len(person_list))
        print("Size of person_array: ", size_in_kb, " KB")
        print(json.dumps(person_list))

    except Exception as e:
        release_db_connection(db_connection)
        return {"error": "Issue with DB Connection/Query"}

def get_db_connection(config):
    cx_Oracle.init_oracle_client(lib_dir= config['client_lib_dir'])
    # orcl = cx_Oracle.connect(
    #     user = config["db_user"],
    #     password = config["db_password"],
    #     host = config["db_hostname"],
    #     port = config["db_port"],
    #     service_name = config["db_service_name"])
    orcl = cx_Oracle.connect(
        user = config["db_user"],
        password = config["db_password"],
        dsn = config["db_hostname"]+":"+config["db_port"]+"/"+config["db_service_name"]
    )
    return orcl


def release_db_connection(connection):
    connection.close()

execute()

""""
# This is to validate the SQL query performance
array_sizes = (10, 100, 1000, 2500, 5000)
for size in array_sizes:
    start = time.time()
    curs.execute(sql).fetchall()
    elapsed = time.time() - start
    print("Time for", size, elapsed, "seconds")

for row_data in curs:
    if not row_data[0].startswith('BIN$'): # skip recycle bin tables
        tableName = row_data[0]

        # output each table content to a separate CSV file
        csv_file_dest = tableName + ".csv"
        outputFile = open(csv_file_dest,'w') # 'wb'
        output = csv.writer(outputFile, dialect='excel')
        sql = "select * from " + tableName
        curs2 = orcl.cursor()
        curs2.execute(sql)

        if printHeader: # add column headers if requested
            cols = []
            for col in curs2.description:
                cols.append(col[0])
            output.writerow(cols)

        for row_data in curs2: # add table rows
            output.writerow(row_data)

        outputFile.close()   
"""

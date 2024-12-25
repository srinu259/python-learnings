import time
import oracledb
import json
from jinja2 import Template
def execute(dbUsername, dbPassword, dbHostname, dbPort, dbServiceName, dbClientDirectory):

    db_config = {}
    db_config["db_user"] = dbUsername
    db_config["db_password"] = dbPassword
    db_config["db_hostname"] = dbHostname
    db_config["db_port"] = dbPort
    db_config["db_service_name"] = dbServiceName
    db_config["client_lib_dir"] = dbClientDirectory
    sql = "SELECT * FROM QAG_HR_SMAX_STAFF_DET_V WHERE ROWNUM <=10000 ORDER BY PERSON_ID ASC"
    person_list = []
    person_json = """{
            "Upn": "{{ data[0] }}",
            "Email": "{{ data[1] }}",
            "FirstName": "{{ data[2] }}",
            "LastName": "{{ data[3] }}"
    }"""

    try:
        db_connection = get_db_connection(db_config)
        template = Template(person_json)
        with db_connection.cursor() as cursor:
            cursor.arraysize = 256
            for row_data in cursor.execute(sql):
                rendered_form = (template.render(data=row_data))
                person_list.append(json.loads(rendered_form))
        release_db_connection(db_connection)
        size_in_kb = str(person_list.__sizeof__()/1000) + " KB"
        return {
            "person_list_len": len(person_list),
            "person_list_size": size_in_kb,
            "person_list": json.dumps(person_list)
        }
    except Exception as e:
        release_db_connection(db_connection)
        return {"error_message":"Unable to establish DB connection or Query execution "+e, "error":e}

def get_db_connection(config):
    oracledb.init_oracle_client(lib_dir= config['client_lib_dir'])
    orcl = oracledb.connect(
        user = config["db_user"],
        password = config["db_password"],
        host = config["db_hostname"],
        port = config["db_port"],
        service_name = config["db_service_name"])

    return orcl


def release_db_connection(connection):
    connection.close()
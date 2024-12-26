import json

from jinja2 import Template, Environment, Undefined
from datetime import datetime


# 01/12/2024 1733011200000
def format_date_time(value, format=""):
    if isinstance(value, str):
        value = datetime.strptime(value, "%d-%b-%Y")  # Assuming date format like "23-OCT-1996"

    if format == "unixtimestamp":
        return int(value.timestamp()*1000)
    else:
        return value


def get_value(key, dictionary):
    return dictionary.get(key, '')


def execute(company_json, department_json):
    row_data = ("01-DEC-2024", "01-DEC-2024", "qa", "hr")
    company_dict = json.loads(company_json)
    department_dict = json.loads(department_json)

    env = Environment()
    env.filters["format_date_time"] = format_date_time
    env.filters["dict_value"] = get_value
    person_json = """{
            "date_unix": "{{ data[0]|format_date_time("unixtimestamp") }}",
            "date": "{{ data[1]|format_date_time }}",
            "company": "{{ data[2]|dict_value(company_dict) }}",
            "department": "{{ data[3]|dict_value(department_dict) }}" 
    }"""
    template = env.from_string(person_json)
    rendered_form = template.render(
        data=row_data,
        company_dict=company_dict,
        department_dict=department_dict)
    print(rendered_form)


company_json = '''{
        "qa": "qa_c",
        "hp": "hp_c"
    }'''
department_json = '''{
        "sales": "sales_c",
        "it": "it_c",
        "hr": "hr_c"
    }'''
execute(company_json, department_json)

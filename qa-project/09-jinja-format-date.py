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
    print("{}: {}".format(dictionary, key))
    return dictionary.get(key, '')


def execute():
    row_data = ("01-DEC-2024", "01-DEC-2024", "abc")
    company_dict = {
        "def": "def_c",
        "abc": "abc_c"
    }
    env = Environment()
    env.filters["format_date_time"] = format_date_time
    env.filters["dict_value"] = get_value
    person_json = """{
            "var1": "{{ data[0]|format_date_time("unixtimestamp") }}",
            "var2": "{{ data[1]|format_date_time }}",
            "var3": "{{ data[2]|dict_value(company_dict) }}" 
    }"""
    template = env.from_string(person_json)
    rendered_form = template.render(data=row_data, company_dict=company_dict)
    print(rendered_form)


company_dict = '''{
        "def": "def_c",
        "abc": "abc_c"
    }'''
execute()

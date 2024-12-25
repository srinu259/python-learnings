from jinja2 import Template, Environment, Undefined
from datetime import datetime

# 01/12/2024 1733011200000
def datetime_format(value, format):
    if isinstance(value, str):
        value = datetime.strptime(value, "%d-%b-%Y")  # Assuming date format like "23-OCT-1996"

    if format == "unixtimestamp":
        return int(value.timestamp()*1000)
    else:
        return value.strftime("%H:%M %d-%m-%y")


def execute():
    date_to_format = "01-DEC-2024"
    env = Environment()
    env.filters["datetimeformat"] = datetime_format
    person_json = """{
            "date": "{{ data|datetimeformat("unixtimestamp") }}"
    }"""
    # template = Template(person_json)
    # template.globals['datetime_format'] = datetime_format
    # rendered_form = (template.render(data=date_to_format))
    template = env.from_string(person_json)
    rendered_form = template.render(data=date_to_format)
    print(rendered_form)

execute()

import jinja2
from jinja2 import Template, pass_context, Undefined
from datetime import datetime

# Define the datetime_format function that will be used as a custom filter
@pass_context
def datetime_format(value, format="%H:%M %d-%m-%y"):
    # Convert string to datetime object if it's a string
    if isinstance(value, str):
        value = datetime.strptime(value, "%d-%b-%Y")  # Assuming date format like "23-OCT-1996"
    return value.strftime(format)


def execute():
    date_to_format = "23-OCT-1996"  # The date string to be formatted
    person_json = """{
        "date": "{{ data | datetime_format }}"
    }"""

    try:
        template = Template(person_json, undefined=SilentUndefined)
        template.globals['datetime_format'] = datetime_format
        rendered_form = template.render(data=date_to_format)
        print(rendered_form)
    except Exception as e:
        print("General error: {} - {}, 1".format(e.__class__, e))
        raise



class SilentUndefined(Undefined):
    def _fail_with_undefined_error(self, *args, **kwargs):
        class EmptyString(str):
            def __call__(self, *_, **__):
                return ''

            __add__ = __radd__ = __mul__ = __rmul__ = __div__ = __rdiv__ = \
                __truediv__ = __rtruediv__ = __floordiv__ = __rfloordiv__ = \
                __mod__ = __rmod__ = __pos__ = __neg__ = \
                __getitem__ = __lt__ = __le__ = __gt__ = __ge__ = __int__ = \
                __float__ = __complex__ = __pow__ = __rpow__ = __getattr__ = \
                self._fail_with_undefined_error
        return EmptyString()

    __add__ = __radd__ = __mul__ = __rmul__ = __div__ = __rdiv__ = \
        __truediv__ = __rtruediv__ = __floordiv__ = __rfloordiv__ = \
        __mod__ = __rmod__ = __pos__ = __neg__ = __call__ = \
        __getitem__ = __lt__ = __le__ = __gt__ = __ge__ = __int__ = \
        __float__ = __complex__ = __pow__ = __rpow__ = __getattr__ = \
        _fail_with_undefined_error

# Execute the function
execute()

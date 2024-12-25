import json


def execute(s: str) -> bool:
    if len(json.loads(s)) == 0:
        return True
    else:
        return False
    # print(type(temp))


list_to_check = '''
[ ]
'''
print(execute(list_to_check))
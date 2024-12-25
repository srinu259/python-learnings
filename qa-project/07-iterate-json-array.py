import json


def execute(i, j, data):
    first = i
    step = 0
    last = j + step
    data_json = data[first:last]
    return data_json


data = '''[{"Upn": "0110013", "Email": "210013"},
        {"Upn": "0110014", "Email": "210014"},
        {"Upn": "0110015", "Email": "210015"},
        {"Upn": "0110016", "Email": "210016"},
        {"Upn": "0110017", "Email": "210017"},
        {"Upn": "0110018", "Email": "210018"},
        {"Upn": "0110019", "Email": "210019"},
        {"Upn": "0110020", "Email": "210020"},
        {"Upn": "0110021", "Email": "210021"},
        {"Upn": "0110022", "Email": "210022"},
        {"Upn": "0110023", "Email": "210023"},
        {"Upn": "0110024", "Email": "210024"},
        {"Upn": "0110025", "Email": "210025"},
        {"Upn": "0110026", "Email": "210026"},
        {"Upn": "0110027", "Email": "210027"}]
        '''

# temp = (data.split('#@#')[0]).replace('\n','')
# temp = (data.split('#@#')[0])
temp1 = json.loads(data)
print(json.dumps(temp1[0:2]))

print(len(json.dumps(temp1[100:102])))

data1 = []
print(len(data1))
#
# data1 = list(data)
# print(type(data1))
# print(data1)
#
# print(len(data))
# print(execute(0, 5, data1))
# print(execute(5, 10, data))
# print(execute(10, 13, data))
# print(execute(13, 18, data))
# print(execute(18, 28, data))
# print(execute(18, 28, data))
#
# (2, 3)
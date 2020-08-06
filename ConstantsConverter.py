import json
from collections import namedtuple
from ConstantPrint import ConstantPrint

fileString = ''
with open('test.json') as f:
    fileString = f.read()

json_data = json.loads(fileString)

variables = list()


for key in json_data['values']:
    variables.append(ConstantPrint(key))

for item in variables:
    print('{} {} = {};'.format(item.type, item.name, item.value))
    verilogDataType = ''
    if item.type == 'int' :
        if item.value < 256:
            verilogDataType = "8'd"
        elif item.value < 65535:
            verilogDataType = "16'd"
        else:
            verilogDataType = "32'd"
    print('localparam {} = {}{};'.format(item.name, verilogDataType, item.value))
    print(item.type)
    print(item.value)
    print()
    




# fileString = ''
# with open('test.json') as f:
#     fileString = f.read()

# # class ConstantPrint(object):
# #     def __init__(self, data):
# #         self.__dict__ = 

# x = json.loads(fileString, object_hook=lambda d:namedtuple('X', d.keys())(*d.values()))
# print(fileString)
# # x = json.loads(fileString)
# print(x)

# # var = ConstantPrint(fileString)

# print(x.name)
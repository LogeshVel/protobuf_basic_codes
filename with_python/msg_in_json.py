from google.protobuf import json_format
from python_pb2_files.person_pb2 import Person

a = Person(id=1,name="Logesh",age=21)
print(a)
print(type(a))

print("*"*30)

print("Message to JSON")
msg_in_json = json_format.MessageToJson(a)
print(msg_in_json)
print(type(msg_in_json))
print("+"*10)
print("JSON to Message")
json_to_msg = json_format.Parse(msg_in_json,Person())
print(json_to_msg)
print(type(json_to_msg))
print("*"*30)

print("Message to Dict")
msg_in_dict = json_format.MessageToDict(a)
print(msg_in_dict)
print(type(msg_in_dict))
print("+"*10)
print("Dict to Message")
dict_to_msg = json_format.ParseDict(msg_in_dict,Person())
print(dict_to_msg)
print(type(dict_to_msg))














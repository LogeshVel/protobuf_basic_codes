from google.protobuf.text_format import \
    MessageToString, MessageToBytes, Parse
from python_pb2_files.person_pb2 import Person

a = Person(id=1,name="Logesh",age=21)
print(a)
print(type(a))

print("*"*30)
# Str
print("Message to String")
msg_in_str = MessageToString(a)
print(msg_in_str)
print(type(msg_in_str))

print("+"*10)

print("String to Message")
str_to_msg = Parse(msg_in_str,Person())
print(str_to_msg)
print(type(str_to_msg))
print("*"*30)
# Bytes
print("Message to Bytes")
msg_in_bytes = MessageToBytes(a)
print(msg_in_bytes)
print(type(msg_in_bytes))

print("+"*10)

print("Bytes to Message")
bytes_to_msg = Parse(msg_in_bytes,Person())
print(bytes_to_msg)
print(type(bytes_to_msg))


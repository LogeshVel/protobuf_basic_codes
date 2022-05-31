from using_maps_pb2 import MapMessage

mm = MapMessage(
    map_field = {
        "Hi": "Hello",
        "Have": "Fun",
    }
)

print(mm)
print(type(mm))


from end_file_pb2 import Me, simple__pb2

me = Me(
    my_color = 2 
    # here i have given 2 by seeing the proto file which has GREEN color
)
print(me)
print(type(me))

print("*"*35)

me2 = Me(
    my_color = simple__pb2.MyColor.MY_COLOR_RED
)
print(me2)
print(type(me2))



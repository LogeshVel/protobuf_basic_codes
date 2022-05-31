from first_message_pb2 import FirstMessage, MessageType

msg1 = FirstMessage(
    msg="Hello world!!!",
    msg_type = MessageType.MESSAGE_TYPE_UPDATE
)

print(msg1)
print(type(msg1))


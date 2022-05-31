from proto_version_two_pb2 import \
    RequiredMessage, OptionalMessage, RepeatedMessage, OneOfMessage
from google.protobuf.text_format import \
    MessageToString, MessageToBytes, Parse
rm = RequiredMessage()
print(rm)
print(MessageToString(rm))
print(MessageToBytes(rm))

rm1 = RequiredMessage(
    coder_name = "Logesh"
)
print(rm1)

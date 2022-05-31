PROTO_DIR=proto_files
PYTHON_DIR=python_pb2_files

generate:
	protoc -I${PROTO_DIR} --python_out=${PYTHON_DIR} ${PROTO_DIR}/*.proto
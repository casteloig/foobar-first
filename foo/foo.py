import flask

import grpc
import sys
sys.path.append('./proto')
import service_pb2 as pb2
import service_pb2_grpc as pb2_grpc

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/foo', methods=['GET'])
def home():
    with grpc.insecure_channel('127.0.0.1:4001') as channel:
        stub = pb2_grpc.BarServiceStub(channel)
        response = stub.BarFunc(pb2.Request(a = True))
    return "foo" + response.result

app.run(port=4000)
import flask

import grpc
import sys
import os

from six import string_types
sys.path.append('./proto')
import service_pb2 as pb2
import service_pb2_grpc as pb2_grpc

app = flask.Flask(__name__)
app.config["DEBUG"] = True

ip = os.getenv('LIS_IP', '0.0.0.0')
port = os.getenv('LIS_PORT', '4000')
bar_endpoint = os.getenv('BAR_ENDPOINT', '4001')

@app.route('/foo', methods=['GET'])
def home():

    with grpc.insecure_channel(bar_endpoint) as channel:
        stub = pb2_grpc.BarServiceStub(channel)
        response = stub.BarFunc(pb2.Request(a = True))
    return "foo" + response.result

app.run(host=ip, port=port)
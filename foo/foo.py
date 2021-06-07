import flask

import grpc
import sys
import os

from six import string_types
sys.path.append('./proto')
import service_pb2 as pb2
import service_pb2_grpc as pb2_grpc

import logging
from pythonjsonlogger import jsonlogger


app = flask.Flask(__name__)
app.config["DEBUG"] = True

ip = os.getenv('LIS_IP', "0.0.0.0")
port = os.getenv('LIS_PORT', "4000")
bar_endpoint = os.getenv('BAR_ENDPOINT', "bar:4001")


log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
handler = logging.FileHandler('logs_foo.log', mode='a')

formatter = jsonlogger.JsonFormatter('%(asctime)s %(name)s %(levelname)s %(message)s')
handler.setFormatter(formatter)

log.addHandler(handler)

#logger.removeHandler(handler)
#handler.close()

log.info('Initialized')

@app.route('/foo', methods=['GET'])
def home():
    
    log.info('Listening')
    with grpc.insecure_channel(bar_endpoint) as channel:
        stub = pb2_grpc.BarServiceStub(channel)
        response = stub.BarFunc(pb2.Request(a = True))

    return "foo" + response.result


app.run(host=ip, port=port)


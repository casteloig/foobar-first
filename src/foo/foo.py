from flask import app, abort 

import grpc
import sys
import os

sys.path.append('./proto')
import service_pb2 as pb2
import service_pb2_grpc as pb2_grpc

import logging
from pythonjsonlogger import jsonlogger


app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Environment variables
ip = os.getenv('LIS_IP', "0.0.0.0")
port = os.getenv('LIS_PORT', "4000")
bar_endpoint = os.getenv('BAR_ENDPOINT', "bar:4001")

# Logs
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
handler = logging.FileHandler('logs_foo.log', mode='a')
formatter = jsonlogger.JsonFormatter('%(asctime)s %(name)s %(levelname)s %(message)s')
handler.setFormatter(formatter)
log.addHandler(handler)
log.info('Initialized')


# Error handlers
@app.errorhandler(400)
def bad_request(error):
    log.info('bad request')
    return 'Bad request :P '


@app.errorhandler(503)
def service_unavailable(error):
    log.info('service unavailable')
    return 'Service unavailable :P '



@app.route('/foo', methods=['GET'])
def home():    

    log.info('/foo called')

    try:
        with grpc.insecure_channel(bar_endpoint) as channel:
            stub = pb2_grpc.BarServiceStub(channel)
            response = stub.BarFunc(pb2.Request(a = True))
    except:
        abort(503)
    

    return "foo" + response.result


app.run(host=ip, port=port)


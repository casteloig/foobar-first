import flask
from flask import request, abort, jsonify

import logging
from pythonjsonlogger import jsonlogger

import os
import sys
sys.path.append('./')
import redis

import funcs as f



redis = redis.Redis(
    host = 'redis',
    port= '6379',
    db=0
)

app = flask.Flask(__name__)
app.config["DEBUG"] = True

ip = os.getenv('LIS_IP', "0.0.0.0")
port = os.getenv('LIS_PORT', "4002")

# Logs
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
handler = logging.FileHandler('logs_factorial.log', mode='a')
formatter = jsonlogger.JsonFormatter('%(asctime)s %(name)s %(levelname)s %(message)s')
handler.setFormatter(formatter)
log.addHandler(handler)
log.info('Initialized')



# Error handlers
@app.errorhandler(400)
def bad_request(error):
    log.info('bad request')
    response = {
        'Message': 'Bad request',
        'Code': '400'
    }
    return jsonify(response), 400


@app.errorhandler(503)
def service_unavailable(error):
    log.info('service unavailable')
    response = {
        'Message': 'Service unavailable',
        'Code': '503'
    }
    return jsonify(response), 503



@app.route('/factorial', methods=['POST'])
def factorial():
    # Getting field number on request
    try:
        number = request.get_json()["number"]
    except:
        abort(400)

    # Checking in cache, calculate otherwise
    try:
        result = redis.get(str(number))

        if result == None:
            result = f.factorial(int(number))
            redis.set(number, str(result))
            return str(result)
        else:
            return number
    
    except:
        abort(503)


@app.route('/fibonacci', methods=['POST'])
def fibonacci():
    # Getting field number on request
    try:
        number = request.get_json()["number"]
    except:
        abort(400)

    # Checking in cache, calculate otherwise
    try:
        result = redis.get(str(number))

        if result == None:
            result = f.fib(int(number))
            redis.set(number, str(result))
            return str(result)
        else:
            return number
    
    except:
        abort(503)


try:
    app.run(host=ip, port=port)
except:
    abort(503)


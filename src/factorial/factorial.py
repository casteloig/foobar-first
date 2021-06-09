import flask
from flask import request
import os
import sys
sys.path.append('.')

import redis

import logging
from pythonjsonlogger import jsonlogger

import func_factorial as f


redis = redis.Redis(
    host = 'redis',
    port= '6379',
    db=0
)

app = flask.Flask(__name__)
app.config["DEBUG"] = True

ip = os.getenv('LIS_IP', "0.0.0.0")
port = os.getenv('LIS_PORT', "4002")



@app.route('/', methods=['POST'])
def home():
    # Getting field number on request
    number = request.get_json()["number"]     

    # Checking in cache, calculate otherwise
    result = redis.get(str(number))
    if result == None:
        result = f.factorial(int(number))
        redis.set(number, str(result))
        return str(result)
    else:
        return result


app.run(host=ip, port=port)
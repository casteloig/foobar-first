import flask
from flask import request
import os

import redis

import logging
from pythonjsonlogger import jsonlogger


redis = redis.Redis(
    host = 'redis',
    port= '6379',
    db=0
)

app = flask.Flask(__name__)
app.config["DEBUG"] = True

ip = os.getenv('LIS_IP', "0.0.0.0")
port = os.getenv('LIS_PORT', "4002")


def factorial(number):
    if number > 1:
        return factorial(number-1)*number
    elif number < 1:
        return ("NAN")
    else:
        return 1



@app.route('/', methods=['POST'])
def home():
    # Getting field number on request
    number = request.get_json()["number"]     

    # Checking in cache, calculate otherwise
    result = redis.get(str(number))
    if result == None:
        result = factorial(int(number))
        redis.set(number, str(result))
        return str(result)
    else:
        return result


app.run(host=ip, port=port)
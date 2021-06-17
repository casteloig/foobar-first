import flask
from flask import request, abort, jsonify

import logging
from pythonjsonlogger import jsonlogger

import os
import sys

sys.path.append("./")
from redis import StrictRedis, ConnectionError, DataError

import funcs as f


redis_client = StrictRedis(
    host="redis", port="6379", db=0, charset="utf-8", decode_responses=True
)

app = flask.Flask(__name__)
app.config["DEBUG"] = True

ip = os.getenv("LIS_IP", "0.0.0.0")
port = os.getenv("LIS_PORT", "4002")

# Logs
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
handler = logging.FileHandler("logs_factorial.log", mode="a")
formatter = jsonlogger.JsonFormatter("%(asctime)s %(name)s %(levelname)s %(message)s")
handler.setFormatter(formatter)
log.addHandler(handler)
log.info("Initialized")


# Error handlers
@app.errorhandler(400)
def bad_request(error):
    log.info("bad request")
    details = f"{error.description}"
    response = {"Message": "Bad request", "Code": "400", "Details": details}
    return jsonify(response), 400


@app.errorhandler(500)
def internal_server_error(error):
    log.info("internal server error")
    details = f"{error.description}"
    response = {"Message": "Internal server error", "Code": "500", "Details": details}
    return jsonify(response), 500


@app.errorhandler(503)
def service_unavailable(error):
    log.info("service unavailable")
    details = f"{error.description}"
    response = {"Message": "Service unavailable", "Code": "503", "Details": details}
    return jsonify(response), 503


@app.route("/factorial", methods=["POST"])
def factorial():
    """
    Endpoint [POST] - Returns number's factorial corresponding to the
    number passed on the request

    Parameters
    ----------
        : Json
            "number": int/str (must have this field)

    Returns
    -------
        400:
            Bad request
        503:
            - Connection error with cache (Redis)
            - Data error setting values on cache (Redis)
        200:
            Everything is fine
    """
    # We dont handle error 400 manually bcause errorhandler does auto
    number = request.get_json()["number"]

    # Checking in cache, calculate otherwise
    try:
        result = redis_client.hget("factorial", number)

        if result == None:
            result = f.factorial(int(number))
            redis_client.hset("factorial", key=number, value=str(result))
            return str(result)
        else:
            return str(result)

    except (ConnectionError, DataError):
        abort(503)


@app.route("/fibonacci", methods=["POST"])
def fibonacci():
    """
    Endpoint [POST] - Returns the fibonacci's index number corresponding to the
    number passed on the request

    Parameters
    ----------
        : Json
            "number": int/str (must have this field)

    Returns
    -------
        400:
            Bad request
        503:
            - Connection error with cache (Redis)
            - Data error setting values on cache (Redis)
        200:
            Everything is fine
    """

    # Getting field number on request
    try:
        number = request.get_json()["number"]
    except:
        abort(400)

    # Checking in cache, calculate otherwise
    try:
        result = redis_client.hget("fibonacci", number)

        if result == None:
            result = f.fib(int(number))
            redis_client.hset("fobinacci", key=number, value=str(result))
            return str(result)
        else:
            return str(result)

    except (ConnectionError, DataError):
        abort(503)


try:
    app.run(host=ip, port=port)
except:
    abort(503)

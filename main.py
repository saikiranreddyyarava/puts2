#!/usr/bin/python3

from flask import Flask, request, jsonify
from fractions import Fraction
from decimal import Decimal

app = Flask(__name__)

@app.route('/')
def index():
    return 'Usage;\nOperation?A=<Value1>&B=<Value2>\n'

def check_value(num):
    value = 0
    try:
        value = int(num.strip())
        return value, "OK"
    except ValueError as e:
        try:
            val = float(Fraction(num))
            return val, "OK"
        except ValueError as e:
            return 0, "ERROR"
        except ZeroDivisionError as e:
            return 0, "ERROR"


@app.route('/add')
def addition():
    err = ""
    value1 = request.args.get('A',default = 0)
    value2 = request.args.get('B', default=0)
    v1, err1 = check_value(value1)
    v2, err2 = check_value(value2)
    if err1 == "ERROR":
        return jsonify("ERROR! invalid input"), 500
    if err2 == "ERROR":
        return jsonify("ERROR! invalid input"), 500
    output= eval('{} + {}'.format(value1, value2))
    return jsonify(output)


@app.route('/sub')
def subtraction():
    err = ""
    value1=request.args.get('A',default = 0)
    value2 = request.args.get('B', default=0)
    v1, err1 = check_value(value1)
    v2, err2 = check_value(value2)
    if err1 == "ERROR":
        return jsonify("ERROR! invalid input"), 500
    if err2 == "ERROR":
        return jsonify("ERROR! invalid input"), 500
    output= eval('{} - {}'.format(value1, value2))
    return jsonify(output)

@app.route('/mul')
def multiplication():
    err = ""
    value1=request.args.get('A',default = 0)
    value2 = request.args.get('B', default=0)
    v1, err1 = check_value(value1)
    v2, err2 = check_value(value2)
    if err1 == "ERROR":
        return jsonify("ERROR! invalid input"), 500
    if err2 == "ERROR":
        return jsonify("ERROR! invalid input"), 500
    output= eval('{} * {}'.format(value1, value2))
    return jsonify(output)

@app.route('/div')
def division():
    err = ""
    value1=request.args.get('A',default = 0)
    value2 = request.args.get('B', default=0)
    v1, err1 = check_value(value1)
    v2, err2 = check_value(value2)
    if err1 == "ERROR":
        return jsonify("ERROR! invalid input"), 500
    if err2 == "ERROR":
        return jsonify("ERROR! invalid input"), 500
    try:
        output = eval('{} / {}'.format(value1, value2))
    except ZeroDivisionError as e:
        return jsonify("division by zero error"), 500
    return jsonify(output)


if __name__ == "__main__":
    app.run()

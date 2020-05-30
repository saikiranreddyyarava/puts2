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
    #print("number: {}, type: {}".format(num, type(num)))
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
@app.route('/sub')
def subtraction():
    err = ""
    value1=request.args.get('A',default = 0)
    value2 = request.args.get('B', default=0)
    v1, err1 = check_value(value1)
    v2, err2 = check_value(value2)
    #print("debug: {} - {}\n{} - {}".format(v1, err1, v2, err2))
    if err1 == "ERROR":
        return jsonify("ERROR! invalid input"), 500
    if err2 == "ERROR":
        return jsonify("ERROR! invalid input"), 500
    #print('{} - {} = '.format(value1, value2))
    output= eval('{} - {}'.format(value1, value2))
    return jsonify(output)

if __name__ == "__main__":
    app.run()

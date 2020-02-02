import urllib.parse
from flask import Flask, jsonify, request
import os
import dateutil.parser
import time
import random

app = Flask(__name__)

print('init called')

@app.route('/preds', methods=['GET'])
def preds():
    data = request.form.get('data',None)
    result = '0'
    i=random.random()
    print(i)
    if i>0.5:
        result='1'

    return result


if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0',threaded=True)
    finally:
        print('finally called')
from flask import Flask
from elasticsearch import Elasticsearch
import os
from flask import jsonify
from flask import request

es_host = 'http://0.0.0.0'
print('Elastic host is {}'.format(es_host))
es = Elasticsearch(HOST=es_host, PORT=9200)
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

# @app.route('/', methods=['GET'])
# def index():
#     return jsonify(search_all.search_all(es))
from flask import Flask
from elasticsearch import Elasticsearch
import os
from flask import jsonify
from flask import request
from search.search_all import search_all
from search.search_param import search_by_param
from search.search_by_term import search_by_name
from search.faceted_search import faceted_search
from search.advance_search import advance_search

es_host = 'http://0.0.0.0'
print('Elastic host is {}'.format(es_host))
es = Elasticsearch(HOST=es_host, PORT=9200)
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return jsonify(search_all(es))


@app.route('/searchBy/param')
def searchby_param():
    parameter = request.args.get('searchby')
    term = request.args.get('term')
    return search_by_param(es, parameter, term)

@app.route('/searchBy/names')
def searchby_mission():
    names = request.args.get('names')
    names = names.strip()
    names = [x.strip() for x in names.split(',')]
    return search_by_name(es, names)    

@app.route('/facetedSearch', methods=['GET', 'POST'])
def search_faceted():                                                                                                                              
    data = request.get_json()
    print (request)
    return faceted_search(es, data)    

@app.route('/advanceSearch', methods=['GET', 'POST'])
def search_advanced():                                                                                                                              
    data = request.get_json()
    return advance_search(es, data)  

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
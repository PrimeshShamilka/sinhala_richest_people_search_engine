import urllib.request as urllib2
import urllib.parse as parse
from elasticsearch import Elasticsearch,helpers
import json
import pandas as pd
import os
import csv
import math
import re

def send_data():
    # es_host = os.environ['ELASTICSEARCH_URL']
    es_host = 'http://0.0.0.0'
    print('Elastic host is {}'.format(es_host))
    es = Elasticsearch(HOST=es_host, PORT=9200)
    # es.indices.delete(index="richest_people")
    try:
        request_body = {
                "settings" : {
                    "number_of_shards": 5,
                    "number_of_replicas": 1
                },

                # 'mappings': { 
                #         'properties': {
                #             'Name': {'index': True, 'type': 'text'},
                #             'BDay': {'type': 'date','format':'yyyy-MM-dd'},
                #             'Status': {'type': 'text'},
                #             'Nationality': {'type': 'text'},
                #             'Time': {'type': 'integer'},
                #             'Mission_names': {'type': 'keyword'},
                #             'Selection': {'type': 'text'},
                #             'Occupation': {'type': 'text'},
                #             'Summary': {'type': 'text'},
                #         }},


                'mappings': {
                        'properties': {
                            'PersonName': {'index': True, 'type': 'text'},
                            'Gender': {'type': 'text'},
                            'Age': {'type': 'text'},
                            'NetWorth': {'type': 'text'},
                            'Salary': {'type': 'text'},
                            'Profession': {'type': 'text'},
                            'Nationality': {'type': 'text'},
                            'KeyFacts': {'type': 'text'},
                        }
                }
            }
        es.indices.create(index='richest_people',body=request_body)
    except Exception as e:
        print(e) 

    df = pd.read_csv('./richest_people_sinhala.csv')
    df = df.fillna('')

    for i in range(len(df['person_name'])):

        person_name = df['person_name'][i]  
        gender = df['gender'][i]
        age = df['age'][i]
        net_worth = df['net_worth'][i]
        salary = df['salary'][i]
        profession = df['profession'][i]
        nationality = df['nationality'][i]
        key_facts = df['key_facts'][i]

        data_obj = {
            'PersonName': person_name,
            'Gender': gender,
            'Age': age,
            'NetWorth': net_worth,
            'Salary': salary,
            'Profession': profession,
            'Nationality': nationality,
            'KeyFacts': key_facts,            
        }


        try:
            es.index(index='richest_people', id=i, body=data_obj)
            
        except Exception as e:
                print(e)

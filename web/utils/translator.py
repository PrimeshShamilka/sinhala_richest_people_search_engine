import googletrans
from googletrans import Translator
import json
import csv
import pandas as pd
import time


def translate():
    df = pd.read_csv('richest_people.csv')
    translator = Translator()
    translator.raise_Exception = True
    cols_to_trans = ['person_name','gender','age','net_worth','salary','profession', 'nationality', 'key_facts']
    col = 'net_worth'

    for col in cols_to_trans:
        temp = []
        print(col)
        count = 0
        for i in df[col]:
            count += 1
            try:
                translated = translator.translate(i, src='english', dest='sinhala').text
            except Exception:
                translated = ""
                print ("e")
            temp.append(translated)
            time.sleep(1)
        df[col] = temp
    return df
    
    

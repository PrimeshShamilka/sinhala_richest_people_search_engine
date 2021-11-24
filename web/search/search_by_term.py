def search_by_name(es, names):
    query = {
        "query": {
            "terms": {
            "PersonName": names
            }
        }
    }

    res = es.search(index="richest_people", body=query)  
    hits = res['hits']['hits']
    richest_people = []    
    for person in hits:
        richest_people.append(person['_source'])

    response_body = {
        "hits" : len(richest_people),
        "results" : richest_people
    }
    return response_body


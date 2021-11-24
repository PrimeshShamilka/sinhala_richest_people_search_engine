def faceted_search(es,data):
    filters = []

    for filterobj in data['filter']:
        matchObj = {
            "match" : filterobj
        }
        filters.append(matchObj)

    query = {
            "query": {
                "bool": {
                "must": [
                    {
                    "query_string": {
                        "query": data['term']
                    }
                    }
                ],
                "filter": filters
                }
            },
            "aggs" : {
                "Gender filter" : {
                    "terms" : { 
                    "field" : "Gender.keyword",
                    "size": 5
                    } 
                },
                "Nationality filter" : {
                    "terms" : { 
                    "field" : "Nationality.keyword",
                    "size": 5
                    
                    } 
                },
                "Profession filter" : {
                    "terms" : { 
                    "field" : "Profession.keyword",
                    "size": 5
                    
                    } 
                },
                # "Mission_names filter" : {
                #     "terms" : { 
                #     "field" : "Mission_names.keyword",
                #     "size": 5
                #     } 
                # },
                # "Name filter" : {
                #     "terms" : { 
                #     "field" : "Name.keyword",
                #     "size": 5
                    
                #     } 
                # }
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
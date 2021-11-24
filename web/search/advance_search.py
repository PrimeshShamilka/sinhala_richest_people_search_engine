def advance_search(es, data):
    mustobj = []

    for filterobj in data['filter']:
        matchObj = {"term" : {filterobj['keyword'] : filterobj['value']}}
        mustobj.append(matchObj)

    print (mustobj)

    # ranges = []
    # for rangeObj in data['ranges']:
    #     obj = {rangeObj['keyword'] : rangeObj['range']}
    #     ranges.append(obj)

    query = {
            "size" : 10,
            "query" : {
                "bool" : {  
                "must" : [
                    {
                    "bool" : {
                        "must" : mustobj
                    }
                    },
                    # {
                    # "bool":{    
                    # "must" : [{
                    # "range" : range
                    # } for range in ranges]
                    # }
                    # }
                ]
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
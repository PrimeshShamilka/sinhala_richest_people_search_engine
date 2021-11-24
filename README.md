# sinhala_richest_people_search_engine

An Elasticsearch and Docker-based search engine for searching the world’s richest people in the Sinhala language. Data required for indexing are scrapped from https://www.celebritynetworth.com/list/top-100-richest-people-in-the-world/. The profile of a person will be stored as a document. Metadata stored in a document are as follows, 

- person_name
- gender
- age
- net_worth
- salary
- profession
- nationality 
- key facts


### How to Run 
1. Install Docker and Docker compose </br>
2. Clone the repository (https://github.com/PrimeshShamilka/sinhala_richest_people_search_engine) </br>
3. Run ```cd web``` </br>
4. Run ```docker-compose up -d --build``` </br>
5. Run ```docker-compose ps``` </br>
6. Run ```pip3 install -r requirements.txt``` </br>
7. Run ```python3 utils/scrap.py``` </br>
8. Run ```python3 app.py``` </br>

The techniques used in indexing and querying and the use of advanced features are shown in the table below. 

| Endpoint  | Request Type | Explanation | Example |
| ------------- | ------------- | ------------- | ------------- |
| /searchBy/param  | GET | Search using a specified field | /searchBy/param?searchby=KeyFacts&term=ඔහු |
| /searchBy/names  | GET  | Search by person name | /searchBy/names?names=එලන් |
| /searchBy/professions | GET | Search by profession | /searchBy/professions?professions=ව්යවසායකයා |
| /facetedSearch | POST | Apply filters to the search. Filter by gender, nationality and profession | { "term": "ඔහු", "filter" : [{"Nationality" : "දකුණු"}, {"Gender": "පිරිමි"}]} |
| advanceSearch | POST | Search with a given set of specified keywords | { "filter" : [ {"keyword" : "PersonName", "value": "ජෙෆ්" }, {"keyword" : "Gender", "value": "පිරිමි" }, {"keyword" : "Age", "value": "57" }]} |


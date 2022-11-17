import json

from elasticsearch import Elasticsearch, helpers

es = Elasticsearch("https://localhost:9200",
                   ca_certs="../../elasticsearch-8.5.0-linux-x86_64/elasticsearch-8.5.0/config/certs/http_ca.crt",
                   basic_auth=("elastic", "0pou6*5fBlq9=qkZQUuz"))

'''
Push bulk data from a JSON file into an Elasticsearch index
'''


def bulk_json_data(path):
    with open(path, encoding="utf8") as f:
        with open(path, 'r') as f:
            news = []
            for line in f:
                news.append(json.loads(line))
        return news


# make the bulk call, and get a response
b = bulk_json_data("../news.json")

response = helpers.bulk(es, b, index='news')
print("\nbulk_json_data() RESPONSE:", response)

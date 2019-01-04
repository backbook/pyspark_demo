from elasticsearch import Elasticsearch


es = Elasticsearch()
print(es)
print(es.info())
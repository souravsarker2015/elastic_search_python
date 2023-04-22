from elasticsearch import Elasticsearch

es = Elasticsearch([{
    "host": "localhost",
    "port": 9200,
    "scheme": "http",
}])
# es = Elasticsearch(
#     ['localhost'],
#     scheme='https',
#     port=9201,
# )

print(es.ping())
# es.indices.create(index="es1_22_april_2023")
# indices = es.indices.get_alias("*")
# print(indices)

indices = es.cat.indices(format='json')

# print the list of indices
for index in indices:
    print(index['index'])

# ESTE ARCHIVO NO SE DEBE EJECUTAR
# El índice ya ha sido creado y no es necesario volver a ejecutar este código

from elasticsearch import Elasticsearch

es = Elasticsearch("https://localhost:9200",
                   ca_certs="../../elasticsearch-8.5.0-linux-x86_64/elasticsearch-8.5.0/config/certs/http_ca.crt",
                   basic_auth=("elastic", "0pou6*5fBlq9=qkZQUuz"))

mappings = {
    "properties": {
        "url": {"type": "text"},
        "title": {"type": "text"},
        "extract": {"type": "text"},
        "image": {"type": "text"},
        "time": {"type": "text"},
        "tags": {"type": "text"},
    }
}

es.indices.create(index="news", mappings=mappings)

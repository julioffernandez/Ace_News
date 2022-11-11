from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

es = Elasticsearch(host="https://localhost:9200", ca_certs="path/to/CA_certs", basic_auth=("elastic", "hbKtK0I91gjzHhMpHswS"))

mappings = {
        "properties": {
            "url": {"type": "text", "analyzer": "english"},
            "equipo_1": {"type": "text", "analyzer": "standard"},
            "equipo_2": {"type": "text", "analyzer": "standard"},
            "set_1_equipo_1": {"type": "integer"},
            "set_1_equipo_2": {"type": "integer"},
            "set_2_equipo_1": {"type": "integer"},
            "set_2_equipo_2": {"type": "integer"},
            "set_3_equipo_1": {"type": "integer"},
            "set_3_equipo_2": {"type": "integer"},
            "set_4_equipo_1": {"type": "integer"},
            "set_4_equipo_2": {"type": "integer"},
            "set_5_equipo_1": {"type": "integer"},
            "set_5_equipo_2": {"type": "integer"},
            "resultadofinal_1": {"type": "integer"},
            "resultadofinal_2": {"type": "integer"},
    }
}

es.indices.create(index="games", mappings=mappings)

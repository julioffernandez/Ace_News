from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

es = Elasticsearch("https://localhost:9200", ca_certs="../../elasticsearch-8.5.0-linux-x86_64/elasticsearch-8.5.0/config/certs/http_ca.crt", basic_auth=("elastic", "Py_ZU5dk2C6RMTp0gkuA"))

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

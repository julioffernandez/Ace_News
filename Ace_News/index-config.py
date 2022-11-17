# ESTE ARCHIVO NO SE DEBE EJECUTAR
# El índice ya ha sido creado y no es necesario volver a ejecutar este código

from elasticsearch import Elasticsearch

es = Elasticsearch("https://localhost:9200", ca_certs="../../elasticsearch-8.5.0-linux-x86_64/elasticsearch-8.5.0/config/certs/http_ca.crt", basic_auth=("elastic", "Py_ZU5dk2C6RMTp0gkuA"))

mappings = {
        "properties": {
            "url": {"type": "text", "analyzer": "english"},
            "equipo_1": {"type": "text", "analyzer": "standard"},
            "equipo_2": {"type": "text", "analyzer": "standard"},
            "set_1_equipo_1": {"type": "text"},
            "set_1_equipo_2": {"type": "text"},
            "set_2_equipo_1": {"type": "text"},
            "set_2_equipo_2": {"type": "text"},
            "set_3_equipo_1": {"type": "text"},
            "set_3_equipo_2": {"type": "text"},
            "set_4_equipo_1": {"type": "text"},
            "set_4_equipo_2": {"type": "text"},
            "set_5_equipo_1": {"type": "text"},
            "set_5_equipo_2": {"type": "text"},
            "resultadofinal_1": {"type": "text"},
            "resultadofinal_2": {"type": "text"},
    }
}

es.indices.create(index="games", mappings=mappings)

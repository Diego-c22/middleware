"""Main Project Configurations"""

DATABASES = {
    "default": {
        "db": "electricity",
        "user": "Cortes",
        "password": "Cortes",
        "host": "192.168.191.172",
        "port": "3306",
    },
    "replica1": {
        "db": "electricity",
        "user": "Cortes",
        "password": "Cortes",
        "host": "192.168.191.174",
        "port": "3306",
    },
    "replica2": {
        "db": "electricity",
        "user": "Cortes",
        "password": "Cortes",
        "host": "192.168.191.3",
        "port": "3306",
    },
    "replica3": {
        "db": "electricity",
        "user": "root",
        "password": "",
        "host": "127.0.0.1",
        "port": "3306",
    },
}

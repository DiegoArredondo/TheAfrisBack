import os
db_config_local = {
    'development': {
        'driver': 'mysql',
        'database': 'theafris',
        'host':'127.0.0.1',
        'user': 'root',
        'password': 'the!afris@adatabase',
        'prefix': '',
        'charset':'utf8'
    }
}
db_config_production = {
    'development': {
        'driver': 'mysql',
        'database': 'theafris',
        'user': 'root',
        'password': 'the!afris@adatabase',
        'prefix': '',
        'unix_socket': '/cloudsql/theafrisback:us-central1:theafris',
        'charset':'utf8'
    }
}

if os.environ.get('FLASK_ENV',False)=='production':
    db_config = db_config_production
else:
    db_config = db_config_local

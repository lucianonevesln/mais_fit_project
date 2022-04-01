import os

DB = os.environ.get("DB") # mysql
USER = os.environ.get("USER") # root
PASS = os.environ.get("PASS") # dinossauro12
DB_URL = os.environ.get("DB_URL") # localhost/mais_fit

connect_string = f'{DB}://{USER}:{PASS}@{DB_URL}'
config = {
    'db.url': connect_string,
    'db.echo':'False'
}

import mariadb

config = {
    'host' : 'localhost',
    'port' : 3306,
    'user' : 'root',
    'password' : '',
    'database' : 'user',
}

DB = mariadb.connect(**config)
DB.autocommit = True
import sqlalchemy as db
import pymysql

# specify database configurations
config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'Admin123*',
    'database': 'softwaredb'
}
db_user = config.get('user')
db_pwd = config.get('password')
db_host = config.get('host')
db_port = config.get('port')
db_name = config.get('database')
# specify connection string
connection_str = f'mysql+pymysql://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}'
# connect to database
engine = db.create_engine(connection_str)
connection = engine.connect()
# pull metadata of a table
'''metadata = db.MetaData(bind=engine)
metadata.reflect(only=['historial'])

historial = metadata.tables['historial']
historial'''


def save_db(quantity, url, type):
    query = """INSERT INTO historial (url, quantity, filter) VALUES ( %s, %s, %s)"""
    record = (url, quantity, type)
    connection.execute(query, record)

def retreive_data():
    query = """ SELECT * FROM historial """
    result = connection.execute(query)
    records = result.fetchall()
    print("record")
    for row in records:
        print(row)
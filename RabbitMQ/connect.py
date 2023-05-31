import configparser
import pika

from mongoengine import connect



config = configparser.ConfigParser()
config.read('config.ini')

mongo_user = config.get('DB', 'user')
mongodb_pass = config.get('DB', 'pass')
db_name = config.get('DB', 'db_name')
domain = config.get('DB', 'domain')

# connect to cluster on AtlasDB with connection string

connect(host=f"""mongodb+srv://{mongo_user}:{mongodb_pass}@{domain}/{db_name}?retryWrites=true&w=majority""", ssl=True)



rabbit_user = config.get('DB_RABBIT', 'user')
rabbit_pass = config.get('DB_RABBIT', 'pass')
host = config.get('DB_RABBIT', 'host')
port = config.get('DB_RABBIT', 'port')

creds = pika.PlainCredentials(rabbit_user, rabbit_pass)
conn_string = pika.ConnectionParameters(host=host, port=port, credentials=creds)
connection_Rabbit = pika.BlockingConnection(conn_string)
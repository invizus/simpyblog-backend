import yaml
import mysql.connector

Config = yaml.load(open("config.yml","r"))
dbsession = mysql.connector.connect(
        host = Config['mysql.host'],
        user = Config['mysql.user'],
        database = Config['mysql.database']
        )
apiURL = Config['api.url']

import yaml
import mysql.connector
from sys import argv

Config = yaml.load(open("config.yml","r"))
dbsession = mysql.connector.connect(
        host = Config['mysql.host'],
        user = Config['mysql.user']
        )

# below code block is to init new database
# TODO check paths from config.yaml (to be implemented)
def init_db():
        cmd = dbsession.cursor()
        cmd.execute("CREATE DATABASE IF NOT EXISTS " +str(Config['mysql.database']) )
        cmd.execute("USE "+str(Config['mysql.database']))
        cmd.execute('''CREATE TABLE IF NOT EXISTS posts (
                id SMALLINT(5) UNIQUE KEY auto_increment,
                post_author VARCHAR(40),
                post_date DATETIME,
                post_title text,
                post_text longtext,
                post_category text,
                link varchar(20)
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8
                ''')

# for new installations run this script with install argument:
# python3 init-project.py install
if __name__ == '__main__':
    print("usage: python3 init-project.py install")
    if argv[1] == "install":
            init_db()

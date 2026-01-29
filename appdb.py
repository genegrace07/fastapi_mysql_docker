import mysql.connector
from dotenv import load_dotenv
import os
from pydantic import BaseModel

load_dotenv()

db = mysql.connector.connect(
    host=os.getenv('dbhost'),
    user=os.getenv('dbuser'),
    password=os.getenv('dbpassword'),
    database=os.getenv('dbdatabase')
)

##COLUMNS ON THIS TABLE
# dbcursor.execute('create table users('
#                  'id int auto_increment primary key,'
#                  'name varchar(50) not null,'
#                  'email varchar(100) not null )')
##FIRST DATA ON USERS TABLE
# dbcursor.execute('insert into users(name,email) '
#                  'values("luffy","luffy@gmail.com"),'
#                  '("zoro","zoro@gmail.com"),'
#                  '("sanji","sanji@gmail.com")')

class Users(BaseModel):
    name = str
    email = str
    def view(self):
        db.ping(reconnect=True)
        dbcursor = db.cursor(dictionary=True,buffered=True)
        dbcursor.execute('select * from users')
        result=dbcursor.fetchall()
        dbcursor.close()
        return result
    def add(self,name,email):
        db.ping(reconnect=True)
        dbcursor = db.cursor(dictionary=True,buffered=True)
        querry = 'insert into users(name,email) values(%s,%s)'
        dbcursor.execute(querry,(name,email,))
        db.commit()
        dbcursor.close()




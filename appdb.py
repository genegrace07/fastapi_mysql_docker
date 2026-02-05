import mysql.connector
from dotenv import load_dotenv
import os
from pydantic import BaseModel
import time

load_dotenv()

for t in range(15):
    try:
        db = mysql.connector.connect(
            host=os.getenv('dbhost'),
            user=os.getenv('dbuser'),
            password=os.getenv('dbpassword'),
            database=os.getenv('dbdatabase')
        )
        print('mysql connected')
        break
    except mysql.connector.Error:
        print('mysql connecting...')
        time.sleep(3)

##COLUMNS ON THIS TABLE
dbcursor = db.cursor()
create_table = """
                create table if not exists users(
                id int auto_increment primary key,
                name varchar(50) not null,
                email varchar(100) not null )
                """
# dbcursor.execute('create table users('
#                  'id int auto_increment primary key,'
#                  'name varchar(50) not null,'
#                  'email varchar(100) not null )')
dbcursor.execute(create_table)
db.commit()
##FIRST DATA ON USERS TABLE
# dbcursor.execute('insert into users(name,email) '
#                  'values("luffy","luffy@gmail.com"),'
#                  '("zoro","zoro@gmail.com"),'
#                  '("sanji","sanji@gmail.com")')

class Users(BaseModel):
    id:int
    name:str
    email:str

class Usersdb():
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
    def update(self,name,email,id):
        db.ping(reconnect=True)
        dbcursor = db.cursor(dictionary=True, buffered=True)
        querry = 'update users set name = %s,email = %s where id = %s'
        dbcursor.execute(querry,(name,email,id,))
        db.commit()
        dbcursor.close()
    def delete(self,id):
        db.ping(reconnect=True)
        dbcursor = db.cursor(dictionary=True, buffered=True)
        querry = 'delete from users where id = %s'
        dbcursor.execute(querry,(id,))
        db.commit()
        dbcursor.close()




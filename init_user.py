
import psycopg2
from model import User



def connnectUsers():
    connection=psycopg2.connect(
        database="BookStore",
        host="localhost",
        user="postgres",
        password="mysecretpassword",
        port="5432"
    )

    cursor=connection.cursor()
    cursor.execute(''' CREATE TABLE IF NOT EXISTS users(id SERIAL PRIMARY KEY , Name TEXT , Email TEXT , Password TEXT ) ;''')
    connection.commit()
    
    cursor.close()
    connection.close()
    
    
    
def RegisterUsers(User):
    connection=psycopg2.connect(
        database="BookStore",
        host="localhost",
        user="postgres",
        password="mysecretpassword",
        port="5432"
    )
    
    cursor=connection.cursor()
    cursor.execute(" INSERR INTO VALUES (%s,%s,%s,%s)",(
        
    ))

    
    


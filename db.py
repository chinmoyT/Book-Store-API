import random
import psycopg2
from model import Book, User

connection=psycopg2.connect(
        database="BookStore",
        host="localhost",
        user="postgres",
        password="mysecretpassword",
        port="5432"
    )


example_books=[
  {
    "ISBN": 9780545010221,
    "Title": "Harry Potter and the Sorcerer's Stone",
    "Author": "J.K. Rowling",
    "Price": 12.99,
    "Quantity": 5,
    "Available": True,
    "UpdatedTime": "2024-01-25T01:04:00Z"
  },
  {
    "ISBN": 9780062315005,
    "Title": "To Kill a Mockingbird",
    "Author": "Harper Lee",
    "Price": 8.99,
    "Quantity": 2,
    "Available": False,
    "UpdatedTime": "2024-01-24T15:30:00Z"
  },
  {
    "ISBN": 9780451524935,
    "Title": "The Lord of the Rings",
    "Author": "J.R.R. Tolkien",
    "Price": 19.99,
    "Quantity": 10,
    "Available":True,
    "UpdatedTime": "2024-01-25T05:15:00Z"
  }
]

new_user=[
{
  "Name": "Michael Brown",
  "Email": "michaelbrown@example.com",
  "Password": "strongpassword!"
},


]

def getNewId():
    return random.getrandbits(40) >> 4


def connect():
    
    cursor=connection.cursor()
    cursor.execute(''' CREATE TABLE IF NOT EXISTS books(ISBN NUMERIC(14,0) PRIMARY KEY , Title TEXT, Author TEXT ,Price FLOAT, Qunatity INTEGER, Available BOOLEAN, UpdatedTime TIMESTAMP);''')
    connection.commit()
    for i in example_books:
        bk=Book(getNewId(),i["Title"],i["Author"],i["Price"],i["Quantity"],i["Available"],i["UpdatedTime"])
        insert(bk)
    cursor.close()
    connection.close()




    

def insert(book):
    connection=psycopg2.connect(
        database="BookStore",
        host="localhost",
        user="postgres",
        password="mysecretpassword",
        port="5432"
    )
    
    curr=connection.cursor()
    curr.execute("INSERT INTO books VALUES (%s, %s, %s, %s, %s, %s, %s)",(
        book.ISBN,
        book.Title,
        book.Author,
        book.Price,
        book.Quantity,
        book.Available,
        book.UpdatedTime
       ))
  

    connection.commit()
    curr.close()
    connection.close()
    
    
def RetrieveAllBooks():
    connection=psycopg2.connect(
        database="BookStore",
        host="localhost",
        user="postgres",
        password="mysecretpassword",
        port="5432"
    )
    curr=connection.cursor()
    curr.execute("SELECT * FROM books")
    row= curr.fetchall()
    
    books=[]
    for i in row:
        book=Book(i[0],i[1],i[2],i[3],i[4],i[5],i[6])
        books.append(book)
    
    curr.close()
    connection.close()
    return books



def UpdateBooks(book):
    connection=psycopg2.connect(
        database="BookStore",
        host="localhost",
        user="postgres",
        password="mysecretpassword",
        port="5432"
    )
    
    cursor=connection.cursor()

    cursor.execute("UPDATE books SET Available=%s, Title=%s, UpdatedTime=%s WHERE ISBN=%s ", (book.Available, book.Title,book.UpdatedTime, book.ISBN))
    connection.commit()
    cursor.close()
    connection.close()
    
test_book = Book(
    ISBN=45353654604, 
    Title="Test Book Title",
    Author="Test Author",
    Price=19.99,
    Quantity=10,
    Available=True,
    UpdatedTime="2024-01-26T04:57:00Z"  
)
    
def DeleteById(id):
    connection=psycopg2.connect(
        database="BookStore",
        host="localhost",
        user="postgres",
        password="mysecretpassword",
        port="5432"
    )
    cursor= connection.cursor()
    cursor.execute("DELETE FROM books WHERE ISBN=%s", (id,))
    connection.commit()
    cursor.close()
    connection.close()
    
    

def RetrievebyId(id):
    connection=psycopg2.connect(
        database="BookStore",
        host="localhost",
        user="postgres",
        password="mysecretpassword",
        port="5432"
    )
    cursor= connection.cursor()
    cursor.execute("SELECT * FROM books WHERE ISBN=%s", (id,),)
    row=cursor.fetchall()
    for i in row:
        book=Book(i[0],i[1],i[2],i[3],i[4],i[5],i[6])
    
    
   
    connection.commit()
    cursor.close()
    connection.close()
    return book



def createUserTable():
    connection=psycopg2.connect(
        database="BookStore",
        host="localhost",
        user="postgres",
        password="mysecretpassword",
        port="5432"
    )
    
    
    cursor=connection.cursor()
    cursor.execute(''' CREATE TABLE IF NOT EXISTS users (ID SERIAL  PRIMARY KEY ,NAME TEXT , EMAIL TEXT , PASSWORD TEXT );''')
    connection.commit()
    for i in new_user:
            ur=User(i["Name"],i["Email"],i["Password"])
            insertUsers(ur)
    
    cursor.close()
    connection.close()
    

def insertUsers(User):
    connection=psycopg2.connect(
        database="BookStore",
        host="localhost",
        user="postgres",
        password="mysecretpassword",
        port="5432"
    )
    
    curr=connection.cursor()
    
    curr.execute("INSERT INTO users VALUES (%s, %s, %s)",(
        User.Name,
        User.Email,
        User.Password
       ))
  

    connection.commit()
    curr.close()
    connection.close()



    
    
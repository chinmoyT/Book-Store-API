from flask import Flask,request, jsonify
import datetime
import db
from model import Book

app=Flask(__name__)

app.config['USERS_TABLE_CREATED'] = False

with app.app_context():
    db.connect()

@app.route("/books/add",methods=["POST"])
def addBookRequest():
      req_data=request.get_json()
      print(req_data)
      title=req_data["title"]
      bks = [b.serialize() for b in db.RetrieveAllBooks()]
      #print("Books in lib: ",bks)
      for b in bks:
          if b['Title']== title:
              return jsonify({
                'res': f'Error ⛔❌! Book with title {title} is already in library!',
                'status': '404'
            })
      bk=Book(db.getNewId(),title,req_data["author"],req_data["price"],req_data["qunatity"],True,datetime.datetime.now())
      print("books in lib: ",bk.serialize())
      db.insert(bk)
      return jsonify({
                
                'res': bk.serialize(),
                'status': '200',
                'msg': 'Success creating a new book!👍😀'
            })
      
      
      

@app.route("/books/all",methods=["GET"])
def getAllBooks():
    books=db.RetrieveAllBooks()
    serialized_books = []
    for book in books:
        serialized_books.append(book.serialize())
    
    return jsonify({
        'res':serialized_books,
        'status':'200',
        'msg':'Success Fetched all the books!👍😀'
    })
    

@app.route("/books/<ISBN>",methods=['GET'])
def fetchBasedOnISBN(ISBN):
    book = db.RetrievebyId(ISBN) 
  
    if book:
        return jsonify({
            'res': book.serialize(),  
            'status': '200',
            'msg': 'Success getting book by ISBN!'
        })
    else:
        return jsonify({
            'res': [],
            'status': '404',
            'msg': 'Book not found'
        }), 404 
        
        
 
        
@app.route("/books/update",methods=["PUT"])
def udpateRequest():
    req_data=request.get_json()
    availability = req_data['available']
    title = req_data['title']
    the_id = req_data['ISBN']
    quant=req_data['quantity']
    price=req_data['price']
    author=req_data['author']
   
    
    bks = [b.serialize() for b in db.RetrieveAllBooks()]
    for b in bks:
            if b['ISBN'] == the_id:
                bk = Book(
                    the_id, 
                    title, 
                    author,
                    price,
                    quant,
                    availability,
                    datetime.datetime.now()
                )
                print('new book: ', bk.serialize())
                db.UpdateBooks(bk)
                new_bks = [b.serialize() for b in db.RetrieveAllBooks()]
                print('books in lib: ', new_bks)
                return jsonify({
                   
                    'res': bk.serialize(),
                    'status': '200',
                    'msg': f'Success updating the book titled {title}!👍😀'
                })        
    return jsonify({
            
                'res': f'Error ⛔❌! Failed to update Book with title: {title}!',
                'status': '404'
            })
    
 
    
    
@app.route("/books/delete/<ISBN>",methods=['GET'])
def DeleteBooks(ISBN):

  try:
        db.DeleteById(ISBN)  
        return jsonify({
            'status': '200', 
            'msg': 'Book deleted successfully'
        }), 200  
  except Exception as e:
        return jsonify({
            'status': '400',
            'msg': 'Error deleting book',
            'error': str(e)  
        }), 400 
    
    
    


@app.route("/users/register",methods=["GET"])
def registerUser():
    db.createUserTable()
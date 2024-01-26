class Book:
    def __init__(self,ISBN,Title,Author,Price,Quantity, Available, UpdatedTime):
        self.ISBN=ISBN
        self.Title=Title
        self.Author=Author
        self.Price=Price
        self.Quantity=Quantity
        self.Available=Available
        self.UpdatedTime=UpdatedTime
        
        
    def serialize(self):
        return{
            'ISBN':self.ISBN,
            'Title':self.Title,
            'Author':self.Author,
            'Price':self.Price,
            'Quantity':self.Quantity,
            'Available':self.Available,
            'UpdatedTime':self.UpdatedTime
            }
        

class User:
    def __init__(self,Name,Email,Password):
        self.Name=Name
        self.Email=Email
        self.Password=Password
        
        
    
    def serialize(self):
        return{
            'Name':self.Name,
            'Email':self.Email,
            'Password':self.Password
        }
        
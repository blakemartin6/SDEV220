#blake martin 
#Basic CRUD API where we can add a book, delete a book, 
#get all the books, or specific book 
#Half way through I realized I used description instead of book_title as a parameter but description is just the title of book 

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True,nullable=True )
    description = db.Column(db.String(120))
    publisher = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.name} - {self.description} - {self.publisher}"



@app.route('/')
def index():
    return 'Hello'

@app.route('/book_name')
def get_books():
    books = Book.query.all()

    output = []
    for book in books:
        book_data = {'name': book.name, 'description': book.description, 'publisher': book.publisher}
        output.append(book_data)

    return {"Books": output}

@app.route('/book_name/<id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    return {"name": book.name, "description": book.description, "publisher": book.publisher}

@app.route('/book_name', methods=['POST'])
def add_book():
    book = Book(name=request.json['name'], description=request.json['description'], publisher=request.json['publisher'])
    db.session.add(book)
    db.session.commit()
    return {'id': book.id}

@app.route('/book_name/<id>', methods=[DELETE])
def delete_book(id):
    book = Book.query.get(id)
    if book is None:
        return {"erorr": "not found"}
    db.session.delete(Book)
    db.session.commit()
    return {"message": "Nice"}


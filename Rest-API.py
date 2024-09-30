from flask import Flask, request, jsonify, abort

app = Flask(__name__)

# In-memory data store
books = []
next_id = 1

# Create a new book
@app.route('/books', methods=['POST'])
def create_book():
    global next_id
    if not request.json or 'title' not in request.json or 'author' not in request.json:
        abort(400, description="Missing 'title' or 'author' in request body.")
    new_book = {
        'id': next_id,
        'title': request.json['title'],
        'author': request.json['author']
    }
    books.append(new_book)
    next_id += 1
    return jsonify(new_book), 201

# Retrieve all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books), 200

# Retrieve a single book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((item for item in books if item['id'] == book_id), None)
    if book is None:
        abort(404, description="Book not found.")
    return jsonify(book), 200

# Update an existing book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    if not request.json:
        abort(400, description="Request body must be JSON.")
    book = next((item for item in books if item['id'] == book_id), None)
    if book is None:
        abort(404, description="Book not found.")
    book['title'] = request.json.get('title', book['title'])
    book['author'] = request.json.get('author', book['author'])
    return jsonify(book), 200

# Delete a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    book = next((item for item in books if item['id'] == book_id), None)
    if book is None:
        abort(404, description="Book not found.")
    books = [item for item in books if item['id'] != book_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)

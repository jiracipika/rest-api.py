# rest-api.py
Basic Rest api

Instructions to Run:

Install Dependencies:
pip install flask

Run the Application:
python app.py

Test the API:
Use tools like curl or Postman to interact with the API endpoints.

Example Usage with curl:
Create a Book:
curl -X POST -H "Content-Type: application/json" -d '{"title": "1984", "author": "George Orwell"}' http://localhost:5000/books
Get All Books:
curl http://localhost:5000/books
Get a Book by ID:
curl http://localhost:5000/books/1
Update a Book:
curl -X PUT -H "Content-Type: application/json" -d '{"title": "Animal Farm"}' http://localhost:5000/books/1
Delete a Book:
curl -X DELETE http://localhost:5000/books/1

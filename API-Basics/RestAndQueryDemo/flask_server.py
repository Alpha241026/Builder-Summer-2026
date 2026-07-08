from flask import Flask, request, jsonify #pullig in Flask class from flask package...and request & jsonify helper functions

app = Flask(__name__) #boilerplate for creating actual app instance

books = [
    {"id": 1, "title": "Dune", "category": "scifi", "price": 15, "stock": 12},
    {"id": 2, "title": "1984", "category": "scifi", "price": 10, "stock": 8},
    {"id": 3, "title": "Sapiens", "category": "nonfiction", "price": 20, "stock": 15},
    {"id": 4, "title": "The Hobbit", "category": "fantasy", "price": 12, "stock": 20},
    {"id": 5, "title": "Neuromancer", "category": "scifi", "price": 14, "stock": 6},
    {"id": 6, "title": "Educated", "category": "nonfiction", "price": 18, "stock": 11},
    {"id": 7, "title": "The Silent Patient", "category": "mystery", "price": 16, "stock": 9},
    {"id": 8, "title": "A Game of Thrones", "category": "fantasy", "price": 25, "stock": 14},
    {"id": 9, "title": "Thinking, Fast and Slow", "category": "nonfiction", "price": 22, "stock": 5},
    {"id": 10, "title": "The Girl with the Dragon Tattoo", "category": "mystery", "price": 13, "stock": 18}
]


@app.route("/books",methods=["GET"]) #decorator to register below function as handler for any request hitting the url path "/books"...also note that this would've run just with the url path as @app.route defaults to handling GET
def get_books():
    return jsonify(books) #returning dictionary in a json format when get route called from client side


@app.route("/books", methods=["POST"]) #decorator to register below func as handler for any request creating a new book record from the url path
def post_book():
    r = request.get_json() #converting incoming json back to Python dictionary
    books.append(r) #adding new record
    return jsonify({"message" : "Book added successfully!"}), 201 #returning success message and status code


@app.route("/books/<int:id>", methods=["PATCH"]) #decorator to register below function to update specific records...here with id...done as an extension to the url path
def patch_book(id):
    s = request.get_json()
    for rec in books: #looping through list books
        if rec["id"]==id: #checking if passed id exists in any dictionary
            if "price" in s: #checking if the client wants to update a price field
                rec["price"]=s["price"]
            if "stock" in s:
                rec["stock"]=s["stock"] #checking if the client wants to update a stock field
            return jsonify({"message" : "Record updated successfully!"}), 200

    return jsonify({"message" : "Book not found!"}), 404 #error message and code if no such id found


@app.route("/books/<int:id>", methods=["DELETE"]) #decorator to register below function to delete specific records...here with id...done as an extension to the url path
def delete_book(id):

    for rec in books: #looping through list books
        if rec["id"]==id: #checking if passed id exists in any dictionary
            
            books.remove(rec) #deleting the book record
            
            return jsonify({"message" : "Record deleted successfully!"})

    return jsonify({"message" : "Book not found!"}) #error message if no such id found


if __name__ == "__main__": #to make sure file run only when executed directly
    app.run(debug=True) #starts server and auto reloads on updates
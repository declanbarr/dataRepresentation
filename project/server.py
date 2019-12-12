# Import Flask
from flask import Flask, jsonify

# Creating an instance of the flask class
app = Flask(__name__, static_url_path='', static_folder='.')

products=[
    {"id":1, "Product":"TV", "Brand":"Samsung", "Model":"Ru7100", "Price":399.84},
    {"id":2, "Product":"TV", "Brand":"Philips", "Model":"32PHT4504/05", "Price":159.00},
    {"id":3, "Product":"Laptop", "Brand":"ASUS", "Model":"E406MA", "Price":214.99},
    {"id":4, "Product":"Printer", "Brand":"Brother", "Model":"DCP-J572DW", "Price":90.00},
]
nextId=5

# curl "http://127.0.0.1:5000/products"
# URL that will trigger the getAllProducts function
@app.route('/products')
# Function to return all products as a http response
def getAllProducts():
	return jsonify(products)

# curl "http://127.0.0.1:5000/products/1"
# URL that will trigger the findProductById function
@app.route('/products/<int:id>')
# Function to return product by id as a http response
def findProductById(id):
    foundProducts = list(filter(lambda t: t['id'] == id, products))
    # Return status code 204 if no content found
    if len(foundProducts) == 0:
        return jsonify ({}), 204

    return jsonify(foundProducts[0])

# URL that will trigger the create function
@app.route('/products', methods=['POST'])
# Function to return "In create" as a http response
def create():
    return "In create"

# URL that will trigger the update function
@app.route('/products/<int:id>', methods=['PUT'])
# Function to return "In update for id" as a http response
def update(id):
    return "In update for id" + str(id)

# URL that will trigger the delete function
@app.route('/products/<int:id>', methods=['DELETE'])
# Function to return "In delete for id" as a http response
def delete(id):
    return "In delete for id " + str(id)


if __name__ == '__main__':
    app.run(debug= True)
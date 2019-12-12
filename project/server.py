# Import Flask
from flask import Flask, jsonify, request, abort

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

# curl -i -H "Content-Type:application/json" -X POST -d "{\"Product\":\"newProduct\",\"Brand\":\"newBrand\",\"Model\":\"newModel\", \"Price\":99.99}" http://127.0.0.1:5000/products
# URL that will trigger the create function
@app.route('/products', methods=['POST'])
# Function to create a new product
def create():
    global nextId
    # If server is unable to process request then abort with 400 message code
    if not request.json:
        abort(400)
    product = {
        "id": nextId,
        "Product": request.json['Product'],
        "Brand": request.json['Brand'],
        "Model": request.json['Model'],
        "Price": request.json['Price']
    }
    nextId += 1
    products.append(product)
    return jsonify(product)

# curl -i -H "Content-Type:application/json" -X PUT -d "{\"Price\":1000}" http://127.0.0.1:5000/products/1
# URL that will trigger the update function
@app.route('/products/<int:id>', methods=['PUT'])
# Function to update a Product
def update(id):
    foundProducts = list(filter(lambda t: t['id']== id, products))
    # If there are no products found then abort with 404 message code
    if (len(foundProducts) == 0):
        abort(404)
    
    foundProduct = foundProducts[0]
    # If server is unable to process request then abort with 400 message code
    if not request.json:
        abort(400)
    
    reqJson = request.json
    
    # If price is not an int then abort with 400 message code
    if 'Price' in reqJson and type(reqJson['Price']) is not int:
        abort(400)
    if 'Product' in reqJson:
        foundProduct['Product'] = reqJson['Product']
    if 'Brand' in reqJson:
        foundProduct['Brand'] = reqJson['Brand']
    if 'Model' in reqJson:
        foundProduct['Model'] = reqJson['Model']
    if 'Price' in reqJson:
        foundProduct['Price'] = reqJson['Price']
    
    return jsonify(foundProduct)


# URL that will trigger the delete function
@app.route('/products/<int:id>', methods=['DELETE'])
# Function to return "In delete for id" as a http response
def delete(id):
    return "In delete for id " + str(id)


if __name__ == '__main__':
    app.run(debug= True)
# Import Flask
from flask import Flask, jsonify, request, abort, session
from productDAO import productDAO

# Creating an instance of the flask class
app = Flask(__name__, static_url_path='', static_folder='.')

# Creating the secret key
app.secret_key = 'secretKey2983475837hk43yuwerit7y'

# Creating page counter
# curl "http://127.0.0.1:5000/session"
@app.route("/session")
def mySession():
    # Starting page counter at 1
    count = 0
    count += 1

    # Set counter to 0 if counter not in session
    if not 'counter' in session:
        session['counter'] = 0
        print('New Session')

    # Increase sessionCount by 1 if the user revists the page    
    sessionCount = session['counter']
    sessionCount += 1
    session['counter'] =  sessionCount

    # Displaying the session count
    sessionCount =   "Session Count =" + str(sessionCount) 
    
    return sessionCount

# Clearing the session
@app.route('/clear')
def clear():
    session.pop('counter', None)

    return 'Session Cleared'

# curl "http://127.0.0.1:5000/products"
# URL that will trigger the getAllProducts function
@app.route('/product')
# Function to return all products as a http response
def getAll():
    results = productDAO.getAll()
    return jsonify(results)

# curl "http://127.0.0.1:5000/products/1"
# URL that will trigger the findProductById function
@app.route('/product/<int:id>')
# Function to return product by id as a http response
def findById(id):
    foundProduct = productDAO.findByID(id)
    return jsonify(foundProduct)

# curl -i -H "Content-Type:application/json" -X POST -d "{\"Product\":\"newProduct\",\"Brand\":\"newBrand\",\"Model\":\"newModel\", \"Price\":99.99}" http://127.0.0.1:5000/products
# URL that will trigger the create function
@app.route('/product', methods=['POST'])
# Function to create a new product
def create():
    # If server is unable to process request then abort with 400 message code
    if not request.json:
        abort(400)
    product = {
        "Product": request.json['Product'],
        "Brand": request.json['Brand'],
        "Model": request.json['Model'],
        "Price": request.json['Price'],
    }
    values =(product['Product'],product['Brand'],product['Model'],product['Price'])
    newId = productDAO.create(values)
    product['id'] = newId
    return jsonify(product)

# curl -i -H "Content-Type:application/json" -X PUT -d "{\"Price\":1000}" http://127.0.0.1:5000/products/1
# URL that will trigger the update function
@app.route('/product/<int:id>', methods=['PUT'])
# Function to update a Product
def update(id):
    foundProduct = productDAO.findByID(id)
    # If there are no products found then abort with 404 message code
    if not foundProduct:
        abort(404)
    
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
    values = (foundProduct['Product'], foundProduct['Brand'], foundProduct['Model'], foundProduct['Price'])
    productDAO.update(values)
    return jsonify(foundProduct)

# curl -X DELETE "http://127.0.0.1:5000/products/1"
# URL that will trigger the delete function
@app.route('/product/<int:id>', methods=['DELETE'])
# Function to delete record
def delete(id):
    productDAO.delete(id)
    return jsonify({"done":True})

if __name__ == '__main__':
    app.run(debug= True)
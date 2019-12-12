# Import Flask
from flask import Flask

# Creating an instance of the flask class
app = Flask(__name__, static_url_path='', static_folder='.')


# URL that will trigger the getAllProducts function
@app.route('/products')
# Function to return "In getAllProducts" as a http response
def getAllProducts():
	return "In getAllProducts"

# URL that will trigger the findProductById function
@app.route('/products/<int:id>')
# Function to return "In In findProductById for id" as a http response
def findProductById(id):
    return "In findProductById for id " +str(id)

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
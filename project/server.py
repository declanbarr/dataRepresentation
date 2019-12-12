# Import Flask
from flask import Flask

# Creating an instance of the flask class
app = Flask(__name__, static_url_path='', static_folder='.')

# URL that will trigger the index function
@app.route('/')
# Function to return "This is a test" as a http response
def index():
	return "This is a test"

if __name__ == '__main__':
    app.run(debug= True)
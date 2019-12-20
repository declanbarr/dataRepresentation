# Data Representation Project

## This folder contains the final project for the Data Representation Module

### What's contained in this project?

* dbconfigtemplate.py
* createDatabase.py
* createTable.py
* insertData.py
* productDAO.py
* productviewer.html
* requirements.txt
* server.py

### Instructions on how to run the project.

1. First start by cloning the repository to your machine. 
2. Open a virtual environment within the project folder of the repository.
3. The requirements.txt file contains all the packages needed for the app to run. To install these type: • pip install -r path/to/requirements.txt

4. Then alter the dbconfigtemplate.py to enable the app server to connect to mysql server
5. Start up mysql server.
6. If you need to create the database, the table and insert some initial data into the database you can run the python files:
    * createDatabase.py
    * createTable.py
    * insertData.py
7. Run Flask server and open the productviewer.html page by typing http://127.0.0.1:5000/productviewer.html into your browser
8. From here you can perform CRUD operations on the product table

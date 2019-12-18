import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    port="3308",
    user="root",
    password="",
    database="datarepresentation"
)

mycursor = mydb.cursor()
sql="CREATE TABLE product (id INT AUTO_INCREMENT PRIMARY KEY, Product VARCHAR(255), Brand VARCHAR(255), Model VARCHAR(255), Price FLOAT)"

mycursor.execute(sql)
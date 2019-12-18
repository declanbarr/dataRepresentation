import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    port="3308",
    user="root",
    password=""
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE datarepresentation")
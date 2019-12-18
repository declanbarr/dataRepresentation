import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    port="3308",
    user="root",
    password="",
    database="datarepresentation"
)

products=[
    {"Product":"TV", "Brand":"Samsung", "Model":"Ru7100", "Price":399.84},
    {"Product":"TV", "Brand":"Philips", "Model":"32PHT4504/05", "Price":159.00},
    {"Product":"Laptop", "Brand":"ASUS", "Model":"E406MA", "Price":214.99},
    {"Product":"Printer", "Brand":"Brother", "Model":"DCP-J572DW", "Price":90.00},
]


cursor = db.cursor()


for i in range(len(products)):

    sql="insert into product (Product, Brand, Model, Price) values (%s, %s, %s, %s)"
    values = (products[i]["Product"], products[i]["Brand"], products[i]["Model"], products[i]["Price"])

    cursor.execute(sql, values)

    db.commit()
    print("1 record inserted, ID:", cursor.lastrowid)
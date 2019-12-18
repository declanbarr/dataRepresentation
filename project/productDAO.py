import mysql.connector
class ProductDAO:
    db=""
    def __init__(self): 
        self.db = mysql.connector.connect(
        host="localhost",
        port="3308",
        user="root",
        password="",
        database="datarepresentation"
        )
        
    def create(self, values):
        cursor = self.db.cursor()
        sql="insert into product (Product,Brand,Model,Price) values (%s,%s,%s,%s)"
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql="select * from product"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        
        for result in results:
            print(result)
            returnArray.append(self.convertToDictionary(result))

        return returnArray

    def findByID(self, id):
        cursor = self.db.cursor()
        sql="select * from product where id = %s"
        values = (id,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        
        return self.convertToDictionary(result)

    def update(self, values):
        cursor = self.db.cursor()
        sql="update product set Product=%s, Brand=%s, Model=%s, Price=%s  where id=%s"
        cursor.execute(sql, values)
        self.db.commit()
    
    def delete(self, id):
        cursor = self.db.cursor()
        sql="delete from product where id = %s"
        values = (id,)

        cursor.execute(sql, values)

        self.db.commit()
        print("delete done")

    def convertToDictionary(self, result):
        colnames=["id","Product","Brand","Model","Price"]  
        item = {}
        
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        
        return item
        
productDAO = ProductDAO()
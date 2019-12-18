import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    port="3308",
    user="root",
    password="",
    database="datarepresentation"
)

cursor = db.cursor()
sql="delete from student where id = %s"
values=(1,)

cursor.execute(sql, values)

db.commit()
print("delete done")
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    port="3308",
    user="root",
    password="",
    database="datarepresentation"
)

cursor = db.cursor()
sql="select * from student where id = %s"
values = (1, )

cursor.execute(sql, values)
result = cursor.fetchall()
for x in result:
    print(x)
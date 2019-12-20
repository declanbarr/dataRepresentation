import mysql.connector

mydb =  mysql.connector.connect(
        host=cfg.mysql['host'],
        port=cfg.mysql['port'],
        user=cfg.mysql['user'],
        password=cfg.mysql['password'],
        database=cfg.mysql['database']
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE datarepresentation")
import pymysql
from modules import connectmysql as conn

#สร้างฟังก์ชันในการสร้างตารางใหม่
def createtable():
    connection = conn.connectdb()
    cursor = connection.cursor()


    #SQL Create Table
    sql = """
        CREATE TABLE person(
            id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            fullname VARCHAR(255),
            email VARCHAR(255),            
            age INT
        )
    """

    try:
        cursor.execute(sql)
        connection.commit()
        print("Create Table Person Success!!")
    except Exception as e:
        print(e)

createtable()


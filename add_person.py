import pymysql
from modules import connectmysql as conn

#สร้างฟังก์ชัน Insert into
def addperson():
    connection = conn.connectdb()
    cursor = connection.cursor()


    #Insert into person
    sql = """
        INSERT INTO person(fullname, email, age) VALUES ('Somchai Sawaddee', 'somchai@gmail.com','45')
    """

    try:
        cursor.execute(sql)
        connection.commit()
        print("Add data Person Success!!")
    except Exception as e:
        print(e)

addperson()


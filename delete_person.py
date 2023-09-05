import pymysql
from modules import connectmysql as conn

#สร้างฟังก์ชัน Delete
def delperson():
    connection = conn.connectdb()
    cursor = connection.cursor()


    #Delete person
    sql = """
        DELETE FROM person WHERE id = '2'
    """

    try:
        cursor.execute(sql)
        connection.commit()
        print("DELETE Person Success!!")
    except Exception as e:
        print(e)

delperson()


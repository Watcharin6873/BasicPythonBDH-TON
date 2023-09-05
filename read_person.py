import pymysql
from modules import connectmysql as conn
from tabulate import tabulate

#สร้างฟังก์ชันอ่านข้อมูล
def readperson():
    connection = conn.connectdb()
    cursor = connection.cursor()


    #SQL read person
    sql = """
        SELECT * FROM person
    """

    try:
        cursor.execute(sql)
        connection.commit()
        
        #ดึงข้อมูลทั้งหมด
        print(tabulate(cursor))

    except Exception as e:
        print(e)

readperson()


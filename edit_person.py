import pymysql
from modules import connectmysql as conn

#สร้างฟังก์ชัน Update
def updateperson():
    connection = conn.connectdb()
    cursor = connection.cursor()


    #Update person
    sql = """
        UPDATE person SET fullname = 'วัชรินทร์ โสภาพ' WHERE id = '1'
    """

    try:
        cursor.execute(sql)
        connection.commit()
        print("UPDATE Person Success!!")
    except Exception as e:
        print(e)

updateperson()


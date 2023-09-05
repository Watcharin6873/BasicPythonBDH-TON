import pymysql

#สร้างฟังก์ชันก์เชื่อมต่อฐานข้อมูล
def connectdb():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        db='pythondatabase',
        port=3306,
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection

#ทดสอบเรียกใช้งาน
print(connectdb())
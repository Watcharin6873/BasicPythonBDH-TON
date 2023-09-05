#สร้างตัวแปรเก็บข้อมูลชนิดต่างๆ

a = 10
b = 3.14
c = "hello"

#แสดงผลลัพธ์
print(a)
print(b)
print(c)

#ชนิดของตัวแปร
print(type(a))
print(type(b))
print(type(c))

#ตัวแปรเก็บหลายค่า
x=y=z = 10
j,k,l = 10,20,30

print(x,y,z)
print(j,k,l)


#ตัวแปรแบบ boolean
status = True
msg = False

print(status)
print(msg)

print(status == 1)
print(msg == 0)


#การแสดงตัวแปรร่วมกับข้อความ
price = 200.50
qty = 5

#แบบที่ 1
print("ราคาสินค้า", "{:.2f}".format(price), "บาท จำนวน",qty, "ชิ้น")

#แบบที่ 2
print("ราคาสินค้า %.2f บาท จำนวน %d ชิ้น" % (price,qty))

#แบบที่ 3
print(f"ราคาสินค้า {price:.2f} บาท จำนวน {qty} ชิ้น")
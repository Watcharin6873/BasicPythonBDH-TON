import qrcode 
# import time
# import calendar
from datetime import datetime

print('QR Code Generator Program')
print("Please type 'quit' to exit")

while True:
    data = input("Please enter your qrcode data: ")
    if data == 'quit':
        break
    else:
        image = qrcode.make(f'{data}')
        type(image)
        # image.save(f'images/{calendar.timegm(time.gmtime())}.png')
        image.save(f"images/{datetime.today().strftime('%Y%m%d%H%M%S')}.png")
        print("QR Code Generated Successfully")
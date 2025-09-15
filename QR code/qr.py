import qrcode
data = "aman.png.jpg"

qr = qrcode.make(data)

qr.save("qcode.png")

print("qr code generated successfull")
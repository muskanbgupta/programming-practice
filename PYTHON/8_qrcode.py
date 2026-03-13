import qrcode

url=input("enter the url: ").strip()
file_path="C:\\Users\\GANESH\\OneDrive\\Pictures\\qrcode.png"
qr=qrcode.QRCode()
qr.add_data(url)

img=qr.make_image()
img.save(file_path)
print("QR code is generated")
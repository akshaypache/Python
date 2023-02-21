import io
import qrcode

msg = "https://www.instagram.com/aadesh__lokhande/"

qr = qrcode.QRCode()
qr.add_data(msg)
f = io.StringIO()
qr.print_ascii(out=f)
f.seek(5)
data = f.read()
# print(data)

data = data.split("\n")

for i in data:
    file = open("code.txt","a")
    file.write(i)
    file.close()
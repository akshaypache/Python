import io
import qrcode

msg = "https://www.instagram.com/aadesh__lokhande/"

qr = qrcode.QRCode()
qr.add_data(msg)
f = io.StringIO()
qr.print_ascii(out=f)
f.seek(5)
data = f.read()
# data = data.replace("\xa0"," ")
print(data)
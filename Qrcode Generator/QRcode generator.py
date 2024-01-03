import pyqrcode
from pyqrcode import QRCode

s="https://github.com/selvan01"

url=pyqrcode.create(s)
#saving as png file in a specific directory
url.svg("D:\VS Code\Sample\Qrcode Generator/mygithub.png", scale=8)
print("QR Code Generated and saved successfully")
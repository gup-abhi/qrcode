# importing pyqrcode
import pyqrcode

# creating qrcode for the www.instagram.com
qr = pyqrcode.create('www.instagram.com')
# saving the qrcode with abc.png name
qr.png('abc.png', scale = 8)

# import pyzbar to decode
from pyzbar.pyzbar import decode
# import PIL module to open the png image
from PIL import Image

# storing decoded part from image
d = decode(Image.open('abc.png'))
# print the decoded message
print (d)

import os
import qrcode

img = qrcode.make("https://youtu.be/dQw4w9WgXcQ")

img.save("qr.png", "PNG")

os.startfile("qr.png")

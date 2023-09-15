from PIL import Image
import qrcode

text=input('Enter text : ')

qr=qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=3,
)

qr.add_data(text)
qr.make(fit=True)

img=qr.make_image(fill_color="black",back_color="white")

img.save('qr.png')

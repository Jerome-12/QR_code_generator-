import qrcode

text=input('Enter text : ')

qr=qrcode.QRCode(
    box_size=10,
    border=3,
)

qr.add_data(text)
qr.make(fit=True)

img=qr.make_image(fill_color="black",back_color="white")

img.save('qr.png')

print("Qr code generated")

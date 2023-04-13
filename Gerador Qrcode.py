# # **Exemplo de Qrcode comum**

import qrcode

qrcode = qrcode.make('link/mensagem aqui')
display(qrcode)

#qrcode.save('') #dê o nome do arquivo e a extensão que queira

# # **Exemplo de Qrcode estilizado com imagem**

import qrcode
from PIL import Image

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('link/mensagem aqui')

heart = Image.open('heart.jpg')
heart = heart.resize((75, 75))

qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.paste(heart, (100, 150))

#img.save('')


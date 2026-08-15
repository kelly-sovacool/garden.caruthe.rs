import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
qr.add_data('http://garden.caruthe.rs')
colors = []
img = qr.make_image(image_factor=StyledPilImage, color_mask=SolidFillColorMask(),
                    fill_color="#000000") #, back_color="#77928A")
# longmeadow: #77928A
img.save("img/qrcode.png")


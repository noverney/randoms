import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.svg import SvgImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from  qrcode.image.styles.colormasks import SolidFillColorMask

import PIL
from PIL import Image, ImageDraw

if not hasattr(PIL.Image, 'Resampling'):
  PIL.Image.Resampling = PIL.Image
# Now PIL.Image.Resampling.BICUBIC is always recognized.

import tempfile
import os

#Custom function for eye styling. These create the eye masks
# Set up parameters
w_cm, h_cm = (10, 10)      # Real label size in cm we are just setting it for the new rounded image
res_x, res_y = (300, 300)  # Desired resolution
# Inch-to-cm factor
f = 2.54

# Determine image size w.r.t. resolution
w = int(w_cm / f * res_x)
h = int(h_cm / f * res_y)

def add_corners(im, rad, size=(w,h)):
    #circle = Image.new('L', (rad * 2, rad * 2), 0)
    circle = Image.new('L', size, 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2 - 1, rad * 2 - 1), fill=255)
    alpha = Image.new('L', im.size, 255)
    w, h = im.size
    alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
    im.putalpha(alpha)
    return im

def create_rounded_image(image_path, output_path):
    im = Image.open(image_path)
    radius = 100
    im = add_corners(im, radius)
    im.save(output_path, transparent=True)

def create_qr(center_logo_path, output_path, data='https://meetingmunch.com/welcome'):

    # create a temp path 
    temp_dir = tempfile.TemporaryDirectory()
    print(temp_dir.name)
    image_path = os.path.join(temp_dir.name, "rounded.png")

    create_rounded_image(center_logo_path, image_path)

    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=100,
        border=4,
    )

    qr.add_data(data)
    
    qr_img = qr.make_image(image_factory=StyledPilImage,
                        module_drawer=RoundedModuleDrawer(),
                        embeded_image_path=image_path,)
                        # just in case our sticker has different backgound color than white
                        #color_mask=SolidFillColorMask(front_color=(0,0,0,255), back_color=(255,255,255,0)))
    qr_img.save(output_path)

    # use temp_dir, and when done:
    temp_dir.cleanup()

# call the function given the first path being logo 
# and the second path being the ouput file path 
# I also have the function which creates an SVG of the QR code instead of image
create_qr('../website/static/img/SVG/justlogo.png', "fancy-qr-code.png")
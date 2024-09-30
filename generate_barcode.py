from barcode import Code128
from barcode.writer import ImageWriter
from PIL import Image, ImageDraw, ImageFont

FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

def generate_barcode(code, output_file, size=(5, 3), dpi=300):
    if not code:
        print(f"Invalid code for barcode generation: {code}")
        return
    try:
        width, height = int(size[0] * dpi), int(size[1] * dpi)
        text_height = height // 7
        barcode_height = height - text_height
        
        barcode = Code128(code, writer=ImageWriter())
        barcode.default_writer_options['write_text'] = False

        barcode_img = barcode.render()
        
        barcode_img = barcode_img.resize((width, barcode_height))
        
        img = Image.new("RGB", (width, height), "white")
        img.paste(barcode_img, (0, 0))
        
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(FONT_PATH, text_height)
        box = draw.textbbox((0, barcode_height), code, font=font)
        text_width = box[2] - box[0]
        text_x = (width - text_width) // 2
        text_y = barcode_height - (text_height // 4)
        draw.text((text_x, text_y), code, font=font, fill="black")

        img.save(output_file, quality=95)
        
    except Exception as e:
        print(f"Error generating barcode: {e}")
        
from barcode import Code128
from barcode.writer import ImageWriter
from PIL import Image

def generate_barcode(code, output_file, size=(5, 3), dpi=300):
    if not code:
        print(f"Invalid code for barcode generation: {code}")
        return
    try:
        width, height = int(size[0] * 100), int(size[1] * 100)
        barcode = Code128(code, writer=ImageWriter())
        barcode_img = barcode.render()
        width_scale = width / barcode_img.width
        height_scale = height / barcode_img.height
        scale = min(width_scale, height_scale)
        barcode_img = barcode_img.resize((int(barcode_img.width * scale), int(barcode_img.height * scale)))
        label = Image.new("RGB", (width, height), "white")
        y_offset = (width - barcode_img.width) // 2
        label.paste(barcode_img, (y_offset, 0))
        label.save(output_file, dpi=(dpi, dpi))

    except Exception as e:
        print(f"Error generating barcode: {e}")
        
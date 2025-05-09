from PIL import Image

# Load the image with background
input_path = 'Descargas/log.jpg'
output_path = 'Descargas/dragon_logo_no_background.png'

# Open the image
image = Image.open(input_path).convert("RGBA")

# Convert white background to transparent
datas = image.getdata()
new_data = []
for item in datas:
    # Change all white (also shades of whites)
    # pixels to transparent
    if item[0] > 200 and item[1] > 200 and item[2] > 200:
        # Making the pixel transparent
        new_data.append((255, 255, 255, 0))
    else:
        new_data.append(item)

# Update image data
image.putdata(new_data)
image.save(output_path, "PNG")

output_path
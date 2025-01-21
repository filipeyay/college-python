from PIL import Image

img = Image.open("convert.jpeg")  # get the JPEG image you want to convert

img.save("converted.png")  # generates the converted image already in PNG

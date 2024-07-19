from PIL import Image

img = Image.open("converter.jpeg")  # pega a imagem em JPEG que desejar converter
img.save("convertido.png")  # gera a imagem convertida já em PNG

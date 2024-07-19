import sys
import img2pdf
import os

caminho_arquivo = sys.argv[1]
if os.path.isdir(caminho_arquivo):
    with open("convertido.pdf", "wb") as f:
        img = []
        for fname in os.listdir(caminho_arquivo):
            if not fname.endswith(".jpg"):
                continue
            caminho = os.path.join(caminho_arquivo, fname)
            if os.path.isdir(caminho):
                continue
            img.append(caminho)
        f.write(img2pdf.convert(img))
elif os.path.isfile(caminho_arquivo):
    if caminho_arquivo.endswith(".jpg"):
        with open("convertido.pdf", "wb") as f:
            f.write(img2pdf.convert(caminho_arquivo))
else:
    print("insira o nome do arquivo ou diretorio")

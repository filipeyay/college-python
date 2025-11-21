import sys
import img2pdf
import os

path_to_file = sys.argv[1]
if os.path.isdir(path_to_file):
    with open("converted.pdf", "wb") as f:
        img = []
        for fname in os.listdir(path_to_file):
            if not fname.endswith(".jpg"):
                continue
            path = os.path.join(path_to_file, fname)
            if os.path.isdir(path):
                continue
            img.append(path)
        f.write(img2pdf.convert(img))
elif os.path.isfile(path_to_file):
    if path_to_file.endswith(".jpg"):
        with open("converted.pdf", "wb") as f:
            f.write(img2pdf.convert(path_to_file))
else:
    print("Insert file or directory name: ")

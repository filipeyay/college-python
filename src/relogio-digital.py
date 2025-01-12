# TODO: Translate to english

import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Rélogio Digital")
canvas = tk.Canvas(root, height=140, width=400)
canvas.pack()
frame = tk.Frame(root, bg="#232634")
frame.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)
lbl = tk.Label(
    frame, font=("monospace", 40, "bold"), background="#232634", foreground="#babbf1"
)
lbl.pack(anchor="s")


def time():
    string = strftime("%H:%M:%S")
    lbl.config(text=string)
    lbl.after(1000, time)


time()


def tema_escuro():
    frame = tk.Frame(root, bg="#232634")
    frame.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)
    lbl_1 = tk.Label(
        frame,
        font=("monospace", 40, "bold"),
        background="#232634",
        foreground="#babbf1",
    )
    lbl_1.pack(anchor="s")

    def time():
        string = strftime("%H:%M:%S")
        lbl_1.config(text=string)
        lbl_1.after(1000, time)

    time()


def tema_claro():
    frame = tk.Frame(root, bg="#babbf1")
    frame.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)
    lbl_2 = tk.Label(
        frame,
        font=("monospace", 40, "bold"),
        background="#babbf1",
        foreground="#232634",
    )
    lbl_2.pack(anchor="s")

    def time():
        string = strftime("%H:%M:%S")
        lbl_2.config(text=string)
        lbl_2.after(1000, time)

    time()


menu = tk.Menu(root)
tema_menu = tk.Menu(menu, tearoff=0)
tema_menu.add_command(label="Escuro", command=tema_escuro)
tema_menu.add_command(label="Claro", command=tema_claro)
menu.add_cascade(label="Tema", menu=tema_menu)
root.config(menu=menu)
root.mainloop()

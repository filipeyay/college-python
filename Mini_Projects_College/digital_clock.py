import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")
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


def dark_theme():
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


def light_theme():
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
theme_menu = tk.Menu(menu, tearoff=0)
theme_menu.add_command(label="Dark", command=dark_theme)
theme_menu.add_command(label="Light", command=light_theme)
menu.add_cascade(label="Theme", menu=theme_menu)
root.config(menu=menu)
root.mainloop()

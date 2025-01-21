from tkinter import Label
from functools import partial
from tkinter import Tk, END, Entry, N, E, S, W, Button
from tkinter import font


def get_input(entry, argu):
    entry.insert(END, argu)


def delete(entry):
    input_len = len(entry.get())
    entry.delete(input_len - 1)


def clear(entry):
    entry.delete(0, END)


def calc(entry):
    input_info = entry.get()
    try:
        output = str(eval(input_info.strip()))
    except ZeroDivisionError:
        popupmsg()
        output = ""
    clear(entry)
    entry.insert(END, output)


def popupmsg():
    popup = Tk()
    popup.resizable(0, 0)
    popup.geometry("120x100")
    popup.title("Alert")
    label = Label(popup, text="Not possible divide by 0! \n Insert a valid value.")
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(popup, text="Ok", bg="#ddd", command=popup.destroy)
    B1.pack()


def cal():
    root = Tk()
    root.title("Calc")
    root.resizable(0, 0)

    entry_font = font.Font(size=15)
    entry = Entry(root, justify="right", font=entry_font)
    entry.grid(row=0, column=0, columnspan=4, sticky=N + W + S + E, padx=5, pady=5)

    cal_btn_bg = "#ff6600"
    num_btn_bg = "#4b4b4b"
    other_btn_bg = "#ddd"
    text_fg = "#fff"
    btn_active_bg = "#c0c0c0"

    num_btn = partial(
        Button,
        root,
        fg=text_fg,
        bg=num_btn_bg,
        padx=10,
        pady=3,
        activebackground=btn_active_bg,
    )
    cal_btn = partial(
        Button,
        root,
        fg=text_fg,
        bg=cal_btn_bg,
        padx=10,
        pady=3,
        activebackground=btn_active_bg,
    )

    btn7 = num_btn(text="7", bg=num_btn_bg, command=lambda: get_input(entry, "7"))
    btn7.grid(row=2, column=0, pady=5)

    btn8 = num_btn(text="8", command=lambda: get_input(entry, "8"))
    btn8.grid(row=2, column=1, pady=5)

    btn9 = num_btn(text="9", command=lambda: get_input(entry, "9"))
    btn9.grid(row=2, column=2, pady=5)

    btn10 = cal_btn(text="+", command=lambda: get_input(entry, "+"))
    btn10.grid(row=4, column=3, pady=5)

    btn4 = num_btn(text="4", command=lambda: get_input(entry, "4"))
    btn4.grid(row=3, column=0, pady=5)

    btn5 = num_btn(text="5", command=lambda: get_input(entry, "5"))
    btn5.grid(row=3, column=1, pady=5)

    btn6 = num_btn(text="6", command=lambda: get_input(entry, "6"))
    btn6.grid(row=3, column=2, pady=5)

    btn11 = cal_btn(text="-", command=lambda: get_input(entry, "-"))
    btn11.grid(row=3, column=3, pady=5)

    btn1 = num_btn(text="1", command=lambda: get_input(entry, "1"))
    btn1.grid(row=4, column=0, pady=5)

    btn2 = num_btn(text="2", command=lambda: get_input(entry, "2"))
    btn2.grid(row=4, column=1, pady=5)

    btn3 = num_btn(text="3", command=lambda: get_input(entry, "3"))
    btn3.grid(row=4, column=2, pady=5)

    btn12 = cal_btn(text="*", command=lambda: get_input(entry, "*"))
    btn12.grid(row=2, column=3, pady=5)

    btn0 = num_btn(text="0", command=lambda: get_input(entry, "0"))
    btn0.grid(row=5, column=0, pady=5)

    btn13 = num_btn(text=".", command=lambda: get_input(entry, "."))
    btn13.grid(row=5, column=1, pady=5)

    btn14 = Button(
        root,
        text="/",
        fg=text_fg,
        bg=cal_btn_bg,
        padx=10,
        pady=3,
        command=lambda: get_input(entry, "/"),
    )
    btn14.grid(row=1, column=3, pady=5)

    btn15 = Button(
        root,
        text="<-",
        bg=other_btn_bg,
        padx=10,
        pady=3,
        command=lambda: delete(entry),
        activebackground=btn_active_bg,
    )
    btn15.grid(row=1, column=0, columnspan=2, padx=3, pady=5, sticky=N + S + E + W)

    btn16 = Button(
        root,
        text="C",
        bg=other_btn_bg,
        padx=10,
        pady=3,
        command=lambda: clear(entry),
        activebackground=btn_active_bg,
    )
    btn16.grid(row=1, column=2, pady=5)

    btn17 = Button(
        root,
        text="=",
        fg=text_fg,
        bg=cal_btn_bg,
        padx=10,
        pady=3,
        command=lambda: calc(entry),
        activebackground=btn_active_bg,
    )
    btn17.grid(row=5, column=3, pady=5)

    btn18 = Button(
        root,
        text="^",
        fg=text_fg,
        bg=cal_btn_bg,
        padx=10,
        pady=3,
        command=lambda: get_input(entry, "**"),
    )
    btn18.grid(row=5, column=2, pady=5)

    def quit():
        exit["command"] = root.quit()

    exit = Button(
        root, text="Exit", fg="white", bg="black", command=quit, height=1, width=7
    )
    exit.grid(row=6, column=1)

    root.mainloop()


if __name__ == "__main__":
    cal()

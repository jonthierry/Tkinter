import random
import tkinter as tk


def increase():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value + 1}"


def decrease():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value - 1}"


def roll():
    value = int(lbl_value["text"])
    lbl_value["text"] = str(random.randint(1, 6))


def both_decrease(event):
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value - 1}"


def both_increase(event):
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value + 1}"


window = tk.Tk()

window.rowconfigure([0, 1, 2], minsize=50, weight=1)
window.columnconfigure([0, 1, 2], minsize=50, weight=1)

btn_decrease = tk.Button(master=window, text="-", command=decrease)
btn_decrease.grid(row=0, column=0, sticky="nsew")

lbl_value = tk.Label(master=window, text="0")
lbl_value.grid(row=0, column=1)

btn_increase = tk.Button(master=window, text="+", command=increase)
btn_increase.grid(row=0, column=2, sticky="nsew")

btn_both = tk.Button(master=window, text="+/-")
btn_both.grid(row=1, column=1, sticky="nsew")
btn_both.bind("<Button-1>", both_decrease)
btn_both.bind("<Button-3>", both_increase)

btn_roll = tk.Button(master=window, text="Roll", command=roll)
btn_roll.grid(row=2, column=1, sticky="nsew")

window.mainloop()

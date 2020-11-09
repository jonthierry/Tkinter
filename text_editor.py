import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename


def open_file():
    """Open a file for editing"""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"TEXT EDITOR - {filepath}")


def save_as_file():
    """Save the current file as a new file"""
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"TEXT EDITOR - {filepath}")


window = tk.Tk()
window.title("TEXT EDITOR")

window.rowconfigure(0, weight=1)
window.columnconfigure(1, weight=1)

# Create a frame for button labels and buttons
frm_btn = tk.Frame(master=window, borderwidth=5)
btn_open = tk.Button(master=frm_btn, text="OPEN", command=open_file)
# btn_save = tk.Button(master=frm_btn, text="SAVE", command=save_file)
btn_save_as = tk.Button(master=frm_btn, text="SAVE AS", command=save_as_file)

# Pack buttons into the frame and frame into the window
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
# btn_save.grid(row=1, column=0, sticky="ew", padx=5)
btn_save_as.grid(row=2, column=0, sticky="ew", padx=5)
frm_btn.grid(row=0, column=0, stick="ns")

# Create a text label and pack it in window
txt_edit = tk.Text()
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()

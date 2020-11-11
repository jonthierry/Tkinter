import tkinter as tk
from tkinter.filedialog import *
from tkinter import ttk
from tkinter.ttk import *

models = []  # To store model paths
imgs = []  # To append image paths


# Defining functions to make our interface alive

def load_model():
    """Upload the model"""

    model_path = askopenfilename(
        # initialdir="/", # Toggle to start from the initial directory, C:
        title="Select a Model",
        filetypes=[("Model Files", "*.net"), ("All Files", "*.*")]
    )
    if not model_path:
        return

    # lbl_model["text"] = f"{filepath}"
    models.append(model_path)  # To append model paths in model library

    print(model_path)  # To display the model path on the screen/ console

    for model_name in models:  # To loop over stored model paths
        lbl_model = tk.Label(frm_out, text=model_name, bg="black", fg="white", pady=5, width=70
                             )  # To set the model name as the new label name

        # Progress bar (Not connected to the action of uploading yet)
        #    prgrss_model = Progressbar(frm_out, orient=HORIZONTAL, mode="determinate", length=300)
        #    prgrss_model.grid(row=1, column=0, pady=5, sticky='ew')  # To pack the progress bar in the frame
        lbl_model.grid(row=0, column=0, sticky="ew", pady=5)  # To upload explicitly one model


def load_imgs():
    img_path = askopenfilenames(
        title="Select an image or image folder",
        filetypes=[("Image Files", "*.png"), ("All Files", "*.*")]
    )
    if not img_path:
        return
    # lbl_img["text"] = f"{img_path}"
    # lbl_img.grid(row=3, column=0)
    imgs.extend(img_path)  # To append model paths in model library
    #    print(img_path)  # To display the model path on the screen/ console
    for img_name in imgs:  # To loop over stored model paths
        lbl_img = tk.Label(frm_out, text=img_name, bg="black", fg="white", pady=5, width=70)
        # lbl_img.pack()  # To upload more than one model

        listbox_images = tk.Listbox(frm_out, bd=2, width=100)
        # listbox_images.insert(END, "Image list") # To give the list a title

        scr_imgs = Scrollbar(frm_out, orient="vertical")
        scr_imgs.config(command=listbox_images.yview)

        for item in imgs:
            listbox_images.insert(END, item)
        #        prgrss_imgs = Progressbar(frm_out, orient=HORIZONTAL, mode='determinate', length='300')

        listbox_images.grid(row=3, column=0, sticky="nsew", padx=5, pady=10)
        scr_imgs.grid(row=3, column=1, sticky="ns")
        listbox_images.config(yscrollcommand=scr_imgs.set)


#   listbox_images.config(yscrollcommand=scr_imgs.set)

def load_ids_cam():
    # Import PyuEye_API script
    import PyuEye_API


def select(event):
    if comb_load.current() == 1:
        load_imgs()

    elif comb_load.current() == 2:
        load_ids_cam()

    else:
        return


# Create a new window
window = tk.Tk()
window.title("One Class Segmentation")
window.rowconfigure(0, minsize=400, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

# Create necessary widgets

frm_input = tk.Frame(master=window, relief=tk.RAISED, bd=2)
choose = tk.IntVar()  # Creating the choice variable
# choose.set(1)  # Initializing the choice (i.e. Model upload)

btn_load_model = tk.Button(frm_input, text="Load a Model", bg='#c8e6ca', command=load_model)
btn_load_model.grid(row=0, column=0, sticky="ew", pady=5)

variable = tk.StringVar()
comb_load = ttk.Combobox(frm_input, textvariable=variable)
comb_load["values"] = ("Load Images from", "Gallery", "IDS camera")

# Pack the widgets into the frame, and the frame into the window

comb_load.grid(row=5, column=0, sticky="nsew", pady=5)
comb_load.current(0)
comb_load.bind("<<ComboboxSelected>>", select)
frm_input.grid(row=0, column=0, pady=5, sticky="ew", padx=5)

# Frame of output
frm_out = tk.Frame(window, relief=tk.RAISED, bd=2, bg="#f5f2e9")
btn_eval = tk.Button(window, text="EVALUATE", bg='#c8e6ca')

# Pack
btn_eval.grid(row=1, column=1, sticky="ew")
frm_out.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

# Run the application
window.mainloop()

import tkinter as tk
from tkinter import *
from tkinter.filedialog import *
from tkinter.ttk import *
import time

models = []  # To store model paths
imgs = []  # To append image paths


# Defining functions to make our interface alive

def model_upload_prgrss():
    """Monitor the model upload progress"""


def upload_model():
    """Upload the model"""

    """for widget in frm_out.winfo_children():
        widget.destroy() # To destroy previous list and update with another
        """
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
        lbl_model = tk.Label(frm_out, text=model_name, bg="black", fg="white", pady=5, width=30
                             )  # To set the model name as the new label name

        # Progress bar (Not connected to the action of uploading yet)
        prgrss_model = Progressbar(frm_out, orient=HORIZONTAL, mode="determinate", length=300)
        prgrss_model.grid(row=1, column=0, pady=5, sticky='ew')  # To pack the progress bar in the frame

        for x in range(100):
            prgrss_model['value'] += 20
            frm_out.update_idletasks()
            time.sleep(0.05)
            # print(prgrss_model['value'])
            if prgrss_model['value'] == 80:
                lbl_model.grid(row=0, column=0, sticky="ew", pady=5)  # To upload explicitly one model


def upload_img():
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

        listbox_images.grid(row=3, column=0, sticky="nsew", padx=5, pady=10)
        scr_imgs.grid(row=3, column=1, sticky="ns")

        listbox_images.config(yscrollcommand=scr_imgs.set)


# Create a new window
window = tk.Tk()
window.title("One Class Segmentation")
window.rowconfigure(0, minsize=400, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

# Create necessary widgets
"""
1. Frame with one row and two columns as frm_input
2. A radio button to choose btn Model and Images as radio_choose
2. If Model, a dropdown list/ combobox widget of models as comb_choose
3. Else, a load images button as btn_load
4. An evaluation button as btn_eval
5. A display panel (?)
6. A label for uploaded models and images
"""

frm_input = tk.Frame(master=window, relief=tk.RAISED, bd=2)
choose = tk.IntVar()  # Creating the choice variable
# choose.set(1)  # Initializing the choice (i.e. Model upload)

"""# Combobox
comb_upload = Combobox(frm_input)
items = ("Choose a Model", "Upload Images")
comb_upload["values"] = items
comb_upload.grid(row=2, column=0, pady=5)"""

radio_model = tk.Radiobutton(frm_input,
                             text="Choose a Model",
                             variable=choose, value="1",
                             padx=5, pady=5,
                             command=upload_model
                             )
radio_images = tk.Radiobutton(frm_input,
                              text="Upload Images",
                              variable=choose, value="2",
                              padx=5,
                              command=upload_img
                              )

# Pack the widgets into the frame, and the frame into the window
radio_model.grid(row=0, column=0, sticky="w")
radio_images.grid(row=1, column=0, sticky="w")
frm_input.grid(row=0, column=0, pady=5, sticky="ew", padx=5)

# Frame of output
frm_out = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_eval = tk.Button(window, text="EVALUATE")

# Pack
btn_eval.grid(row=1, column=1, sticky="ew")
frm_out.grid(row=0, column=1, pady=5, sticky="nsew")

# lbl_img = tk.Label(frm_out, text="")

# Run the application
window.mainloop()

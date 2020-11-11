from OneClassSegmentation import *


radio_imgs = tk.Radiobutton(frm_input,
                            text="Load Images",
                            variable=choose, value="1",
                            padx=5,
                            command=load_imgs,
                            bg='#f5f2e9'
                            )

radio_ids_cam = tk.Radiobutton(frm_input,
                               text="Load IDS camera",
                               variable=choose, value="2",
                               padx=5,
                               command=load_ids_cam,
                               bg='#f5f2e9'
                               )

radio_imgs.grid(row=3, column=0, sticky="w")
radio_ids_cam.grid(row=4, column=0, sticky="w")

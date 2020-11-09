import tkinter as tk


def fahrenheit_to_celsius():
    """Convert the value for Fahrenheit to Celsius and insert the
    result into lbl_result.
    """
    fahrenheit = ent_temperature.get()
    celsius = (5 / 9) * (float(fahrenheit) - 32)
    lbl_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"


def celsius_to_fahrenheit():
    """Convert the value for Celsius to Fahrenheit to and insert the
    result into lbl_result.
    """
    celsius = ent_temperature.get()
    fahrenheit = (9 / 5) * (float(celsius)) + 32
    lbl_result["text"] = f"{round(fahrenheit, 2)} \N{DEGREE FAHRENHEIT}"


# Set-up the window
window = tk.Tk()
window.title("Temperature Converter")
window.resizable(width=False, height=False)

# Create the Fahrenheit entry frame with an Entry
# widget and label in it
frm_entry = tk.Frame(master=window)
ent_temperature = tk.Entry(master=frm_entry, width=10)
# lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")

# Layout the temperature Entry and Label in frm_entry
# using the .grid() geometry manager
ent_temperature.grid(row=0, column=0, sticky="e")
# lbl_temp.grid(row=0, column=1, sticky="w")

# Create the conversion Button and result display Label
btn_convert_to_c = tk.Button(
    master=window,
    text="\N{DEGREE FAHRENHEIT}",
    command=fahrenheit_to_celsius
)

btn_convert_to_f = tk.Button(
    master=window,
    text="\N{DEGREE CELSIUS}",
    command=celsius_to_fahrenheit
)
lbl_result = tk.Label(master=window, text="")

# Set-up the layout using the .grid() geometry manager
frm_entry.grid(row=0, column=0, padx=10)
btn_convert_to_c.grid(row=0, column=1, pady=10)
btn_convert_to_f.grid(row=0, column=2, pady=10)
lbl_result.grid(row=0, column=3, padx=10)

# Run the application
window.mainloop()

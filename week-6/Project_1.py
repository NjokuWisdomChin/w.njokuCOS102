import tkinter as tk
from tkinter import messagebox

def calculate_charge():
    location = location_var.get()
    try:
        weight = float(weight_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for weight.")
        return

    if location == "Ibeju-Lekki":
        if weight >= 10:
            charge = 5000
        else:
            charge = 3500
    elif location == "Epe":
        if weight >= 10:
            charge = 10000
        else:
            charge = 5000
    else:
        messagebox.showerror("Invalid Location", "Please select a valid location.")
        return

    result_label.config(text=f"Delivery Charge: ₦{charge:,}")

root = tk.Tk()
root.title("Simi Services")
root.geometry("400x250")

tk.Label(root, text="Select Location:").pack(pady=5)
location_var = tk.StringVar(value="Enter location")
tk.OptionMenu(root, location_var, "Ibeju-Lekki", "Epe").pack(pady=5)

tk.Label(root, text="Package Weight (kg):").pack(pady=5)
weight_entry = tk.Entry(root)
weight_entry.pack(pady=5)

tk.Button(root, text="Calculate Charge", command=calculate_charge).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

root.mainloop()
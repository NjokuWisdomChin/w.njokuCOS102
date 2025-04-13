import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Sample mock employee data
employees = [
    {"name": "Alice", "department": "Logistics"},
    {"name": "Bob", "department": "Logistics"},
    {"name": "Charlie", "department": "IT"},
    {"name": "Diana", "department": "IT"},
    {"name": "Eve", "department": "HR"}
]

# Department mapping
department_map = {
    "1": "Logistics",
    "2": "IT",
    "3": "HR"
}

def welcome_employee(name, department):
    window = tk.Toplevel(root)
    window.title("Welcome")
    window.geometry("400x300")

    welcome_label = tk.Label(window, text=f"Welcome {name}!", font=('Arial', 14, 'bold'))
    welcome_label.pack(pady=10)

    dept_label = tk.Label(window, text=f"Here are your colleagues in {department} department:")
    dept_label.pack(pady=5)

    for emp in employees:
        if emp['department'].lower() == department.lower() and emp['name'].lower() != name.lower():
            tk.Label(window, text=emp['name']).pack()

def extract_dept_number(selection):
    # Get just the number (before the dash)
    if " - " in selection:
        return selection.split(" - ")[0].strip()
    return ""

def submit():
    name = name_entry.get().strip()
    selected = dept_combo.get()
    selected_dept_number = extract_dept_number(selected)

    if selected_dept_number not in department_map:
        messagebox.showerror("Invalid", "Please select a valid department number.")
        return

    department = department_map[selected_dept_number]
    found = False
    for emp in employees:
        if emp['name'].lower() == name.lower() and emp['department'].lower() == department.lower():
            found = True
            welcome_employee(name, department)
            break

    if not found:
        messagebox.showinfo("Not Found", f"No employee named {name} in {department} department.")

# GUI setup
root = tk.Tk()
root.title("Employee Verification")
root.geometry("400x300")

tk.Label(root, text="Enter Employee Name:").pack(pady=5)
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Select Department Number:").pack(pady=5)

dept_combo = ttk.Combobox(root, state="readonly")
dept_combo['values'] = [f"{key} - {value}" for key, value in department_map.items()]
dept_combo.pack()

submit_button = tk.Button(root, text="Verify", command=submit)
submit_button.pack(pady=20)

root.mainloop()
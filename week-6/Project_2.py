import tkinter as tk
from tkinter import messagebox

admitted = []
not_admitted = []

user_data = {
    "name": "",
    "department": "",
    "jamb_score": 0,
    "subject_scores": [],
    "interview_passed": False
}

def show_frame(frame):
    frame.tkraise()

def count_credits(scores):
    return sum(1 for score in scores if score >= 50)

def evaluate_admission():
    name = user_data["name"]
    dept = user_data["department"]
    jamb = user_data["jamb_score"]
    credits = count_credits(user_data["subject_scores"])
    passed = user_data["interview_passed"]

    if dept == "Computer Science":
        if jamb >= 250 and credits >= 5 and passed:
            admitted.append(name)
            messagebox.showinfo("Result", f"{name} is admitted into Computer Science!")
        else:
            not_admitted.append(name)
            messagebox.showinfo("Result", f"{name} is NOT admitted into Computer Science.")
    elif dept == "Mass Communication":
        if jamb >= 230 and credits >= 5 and passed:
            admitted.append(name)
            messagebox.showinfo("Result", f"{name} is admitted into Mass Communication!")
        else:
            not_admitted.append(name)
            messagebox.showinfo("Result", f"{name} is NOT admitted into Mass Communication.")

def confirm_name_department():
    name = entry_name.get()
    dept = dept_var.get()
    if name and dept:
        user_data["name"] = name
        user_data["department"] = dept
        setup_subjects()
        show_frame(frame2)
    else:
        messagebox.showerror("Error", "Please enter your name and select a department.")

def setup_subjects():
    for widget in subject_frame.winfo_children():
        widget.destroy()

    subjects = []
    if user_data["department"] == "Computer Science":
        subjects = ["Math", "English", "Physics", "Data Processing", "Biology", "Geography", "Chemistry"]
    else:
        subjects = ["English", "Math", "Economics", "Marketing", "Accounting", "Business Study", "ICT"]

    tk.Label(subject_frame, text="Enter subject scores (0-100):").pack()
    user_data["subject_entries"] = []
    for sub in subjects:
        lbl = tk.Label(subject_frame, text=sub)
        lbl.pack()
        ent = tk.Entry(subject_frame)
        ent.pack()
        user_data["subject_entries"].append(ent)

def save_scores_and_continue():
    try:
        jamb = int(entry_jamb.get())
        user_data["jamb_score"] = jamb
        scores = [int(e.get()) for e in user_data["subject_entries"]]
        if any(score < 0 or score > 100 for score in scores):
            raise ValueError
        user_data["subject_scores"] = scores
        show_frame(frame3)
    except:
        messagebox.showerror("Error", "Please enter valid JAMB and subject scores between 0 and 100.")

def submit_all():
    user_data["interview_passed"] = interview_var.get()
    evaluate_admission()
    
    entry_name.delete(0, tk.END)
    dept_var.set("Computer Science")
    entry_jamb.delete(0, tk.END)
    
    for entry in user_data.get("subject_entries", []):
        entry.delete(0, tk.END)
    
    interview_var.set(False)
    
    show_frame(frame1)

def show_results():
    result_window = tk.Toplevel(root)
    result_window.title("Admission Results")
    result_window.geometry("400x400")

    tk.Label(result_window, text=" Admitted Candidates", font=("Arial", 12, "bold")).pack(pady=5)
    for name in admitted:
        tk.Label(result_window, text=name).pack()

    tk.Label(result_window, text=" Not Admitted Candidates", font=("Arial", 12, "bold")).pack(pady=10)
    for name in not_admitted:
        tk.Label(result_window, text=name).pack()

root = tk.Tk()
root.title("University Admission System")
root.geometry("400x600")

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

frame1 = tk.Frame(root)
frame1.grid(row=0, column=0, sticky='nsew')

inner_frame1 = tk.Frame(frame1)
inner_frame1.place(relx=0.5, rely=0.5, anchor='center')  # Center it

tk.Label(inner_frame1, text="Enter Your Name:").pack(pady=10)
entry_name = tk.Entry(inner_frame1)
entry_name.pack(pady=5)

tk.Label(inner_frame1, text="Select Department:").pack(pady=10)
dept_var = tk.StringVar()
dept_var.set("Computer Science")
dept_menu = tk.OptionMenu(inner_frame1, dept_var, "Computer Science", "Mass Communication")
dept_menu.pack()

tk.Button(inner_frame1, text="Confirm", command=confirm_name_department).pack(pady=20)

frame2 = tk.Frame(root)
frame2.grid(row=0, column=0, sticky='nsew')

tk.Label(frame2, text="Enter JAMB Score:").pack(pady=10)
entry_jamb = tk.Entry(frame2)
entry_jamb.pack()

subject_frame = tk.Frame(frame2)
subject_frame.pack(pady=10)

tk.Button(frame2, text="Next", command=save_scores_and_continue).pack(pady=20)

frame3 = tk.Frame(root)
frame3.grid(row=0, column=0, sticky='nsew')

tk.Label(frame3, text="Did you pass the interview?").pack(pady=20)
interview_var = tk.BooleanVar()
tk.Radiobutton(frame3, text="Yes", variable=interview_var, value=True).pack()
tk.Radiobutton(frame3, text="No", variable=interview_var, value=False).pack()

tk.Button(frame3, text="Submit", command=submit_all).pack(pady=30)

tk.Button(frame3, text="View Results", command=show_results).pack(pady=10)

show_frame(frame1)

root.mainloop()
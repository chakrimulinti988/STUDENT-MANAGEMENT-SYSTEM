import tkinter as tk
from tkinter import messagebox

class Student:
    def __init__(self, name, rollno, m1, m2, age, gender):
        self.name = name
        self.rollno = rollno
        self.m1 = m1
        self.m2 = m2
        self.age = age
        self.gender = gender

    def accept(self, Name, Rollno, marks1, marks2, Age, Gender):
        ob = Student(Name, Rollno, marks1, marks2, Age, Gender)
        ls.append(ob)

    def display(self, ob):
        return (f"Name : {ob.name}\nRoll No : {ob.rollno}\nMarks 1 : {ob.m1}\nMarks 2 : {ob.m2}"
                f"\nAge : {ob.age}\nGender : {ob.gender}\n")

    def search(self, rn):
        for i in range(len(ls)):
            if ls[i].rollno == rn:
                return i
        return -1

    def delete(self, rn):
        i = self.search(rn)
        if i != -1:
            del ls[i]

    def update(self, rn, new_rn):
        i = self.search(rn)
        if i != -1:
            ls[i].rollno = new_rn

ls = []
obj = Student('', 0, 0, 0, 0, '')

def accept_student():
    name = name_entry.get()
    try:
        rollno = int(rollno_entry.get())
        marks1 = int(marks1_entry.get())
        marks2 = int(marks2_entry.get())
        age = int(age_entry.get())
        gender = gender_entry.get()
        obj.accept(name, rollno, marks1, marks2, age, gender)
        messagebox.showinfo("Success", "Student record added successfully!")
        clear_entries()
        display_students()
    except ValueError:
        messagebox.showerror("Input Error", "Invalid input for roll number, marks, or age.")

def clear_entries():
    name_entry.delete(0, tk.END)
    rollno_entry.delete(0, tk.END)
    marks1_entry.delete(0, tk.END)
    marks2_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    gender_entry.delete(0, tk.END)
    search_rollno_entry.delete(0, tk.END)
    delete_rollno_entry.delete(0, tk.END)
    update_old_rollno_entry.delete(0, tk.END)
    update_new_rollno_entry.delete(0, tk.END)

def display_students():
    result_text.config(state=tk.NORMAL)
    result_text.delete(1.0, tk.END)
    for i in range(len(ls)):
        result_text.insert(tk.END, obj.display(ls[i]) + "\n")
    result_text.config(state=tk.DISABLED)

def search_student():
    try:
        rollno = int(search_rollno_entry.get())
        s = obj.search(rollno)
        search_result_text.config(state=tk.NORMAL)
        search_result_text.delete(1.0, tk.END)
        if s != -1:
            search_result_text.insert(tk.END, obj.display(ls[s]) + "\n")
        else:
            search_result_text.insert(tk.END, "Student not found.\n")
        search_result_text.config(state=tk.DISABLED)
    except ValueError:
        messagebox.showerror("Input Error", "Invalid input for roll number.")

def delete_student():
    try:
        rollno = int(delete_rollno_entry.get())
        obj.delete(rollno)
        display_students()
        messagebox.showinfo("Success", "Student record deleted successfully!")
    except ValueError:
        messagebox.showerror("Input Error", "Invalid input for roll number.")

def update_student():
    try:
        old_rollno = int(update_old_rollno_entry.get())
        new_rollno = int(update_new_rollno_entry.get())
        obj.update(old_rollno, new_rollno)
        display_students()
        messagebox.showinfo("Success", "Student roll number updated successfully!")
    except ValueError:
        messagebox.showerror("Input Error", "Invalid input for roll number.")

# GUI
root = tk.Tk()
root.title("Student Management System")

# Setting up grid layout
for i in range(15):
    root.grid_rowconfigure(i, weight=1)
for i in range(2):
    root.grid_columnconfigure(i, weight=1)

# Labels and Entries
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

rollno_label = tk.Label(root, text="Roll No:")
rollno_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
rollno_entry = tk.Entry(root)
rollno_entry.grid(row=1, column=1, padx=10, pady=5)

marks1_label = tk.Label(root, text="Marks 1:")
marks1_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
marks1_entry = tk.Entry(root)
marks1_entry.grid(row=2, column=1, padx=10, pady=5)

marks2_label = tk.Label(root, text="Marks 2:")
marks2_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
marks2_entry = tk.Entry(root)
marks2_entry.grid(row=3, column=1, padx=10, pady=5)

age_label = tk.Label(root, text="Age:")
age_label.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)
age_entry = tk.Entry(root)
age_entry.grid(row=4, column=1, padx=10, pady=5)

gender_label = tk.Label(root, text="Gender:")
gender_label.grid(row=5, column=0, padx=10, pady=5, sticky=tk.W)
gender_entry = tk.Entry(root)
gender_entry.grid(row=5, column=1, padx=10, pady=5)

# Buttons
accept_button = tk.Button(root, text="Accept Student", command=accept_student)
accept_button.grid(row=6, column=0, columnspan=2, pady=5)

display_button = tk.Button(root, text="Display Students", command=display_students)
display_button.grid(row=7, column=0, columnspan=2, pady=5)

search_rollno_label = tk.Label(root, text="Search Roll No:")
search_rollno_label.grid(row=8, column=0, padx=10, pady=5, sticky=tk.W)
search_rollno_entry = tk.Entry(root)
search_rollno_entry.grid(row=8, column=1, padx=10, pady=5)

search_button = tk.Button(root, text="Search Student", command=search_student)
search_button.grid(row=9, column=0, columnspan=2, pady=5)

delete_rollno_label = tk.Label(root, text="Delete Roll No:")
delete_rollno_label.grid(row=10, column=0, padx=10, pady=5, sticky=tk.W)
delete_rollno_entry = tk.Entry(root)
delete_rollno_entry.grid(row=10, column=1, padx=10, pady=5)

delete_button = tk.Button(root, text="Delete Student", command=delete_student)
delete_button.grid(row=11, column=0, columnspan=2, pady=5)

update_old_rollno_label = tk.Label(root, text="Old Roll No:")
update_old_rollno_label.grid(row=12, column=0, padx=10, pady=5, sticky=tk.W)
update_old_rollno_entry = tk.Entry(root)
update_old_rollno_entry.grid(row=12, column=1, padx=10, pady=5)

update_new_rollno_label = tk.Label(root, text="New Roll No:")
update_new_rollno_label.grid(row=13, column=0, padx=10, pady=5, sticky=tk.W)
update_new_rollno_entry = tk.Entry(root)
update_new_rollno_entry.grid(row=13, column=1, padx=10, pady=5)

update_button = tk.Button(root, text="Update Student", command=update_student)
update_button.grid(row=14, column=0, columnspan=2, pady=5)

# Result display
result_text = tk.Text(root, height=10, width=50)
result_text.grid(row=15, column=0, columnspan=2, padx=10, pady=5)
result_text.config(state=tk.DISABLED)

search_result_text = tk.Text(root, height=4, width=50)
search_result_text.grid(row=16, column=0, columnspan=2, padx=10, pady=5)
search_result_text.config(state=tk.DISABLED)

root.mainloop()

import tkinter as tk
from tkinter import messagebox

shopping_list = []

# ---------------- Functions ----------------
def add_item():
    item = entry.get()
    if item == "":
        messagebox.showwarning("Warning", "Please enter an item!")
    else:
        shopping_list.append(item)
        listbox.insert(tk.END, item)
        entry.delete(0, tk.END)
        update_count()

def remove_item():
    try:
        index = listbox.curselection()[0]
        item = shopping_list.pop(index)
        listbox.delete(index)
        update_count()
        messagebox.showinfo("Removed", f"'{item}' removed successfully ❌")
    except IndexError:
        messagebox.showwarning("Warning", "Select an item to remove!")

def view_items():
    if len(shopping_list) == 0:
        messagebox.showinfo("Info", "Shopping list is empty 🛒")
    else:
        items = "\n".join(f"{i+1}. {item}" for i, item in enumerate(shopping_list))
        messagebox.showinfo("Shopping List", items)

def search_item():
    item = entry.get()
    if item in shopping_list:
        messagebox.showinfo("Found", f"'{item}' is in your shopping list ✔")
    else:
        messagebox.showinfo("Not Found", f"'{item}' not found ❌")

def clear_list():
    if messagebox.askyesno("Confirm", "Are you sure you want to clear the list?"):
        shopping_list.clear()
        listbox.delete(0, tk.END)
        update_count()

def update_count():
    count_label.config(text=f"Total Items: {len(shopping_list)}")

# ---------------- Main Window ----------------
root = tk.Tk()
root.title("Realistic Shopping List")
root.geometry("450x600")
root.resizable(False, False)
root.config(bg="#FFFFFF")  # Bright background

# ---------------- Title ----------------
title = tk.Label(root, text="🛒 Advanced Shopping List",
                 font=("Segoe UI", 20, "bold"), bg="#FFFFFF", fg="#1F2933")
title.pack(pady=15)

# ---------------- Entry ----------------
entry = tk.Entry(root, font=("Segoe UI", 13), width=25, bd=2, relief="groove")
entry.pack(pady=10)

# ---------------- Buttons ----------------
btn_frame = tk.Frame(root, bg="#FFFFFF")
btn_frame.pack(pady=15)

tk.Button(btn_frame, text="Add Item", width=12, bg="#2563EB", fg="white",
          font=("Segoe UI", 11, "bold"), command=add_item).grid(row=0, column=0, padx=6)

tk.Button(btn_frame, text="Remove Item", width=12, bg="#EF4444", fg="white",
          font=("Segoe UI", 11, "bold"), command=remove_item).grid(row=0, column=1, padx=6)

tk.Button(btn_frame, text="View Items", width=12, bg="#10B981", fg="white",
          font=("Segoe UI", 11, "bold"), command=view_items).grid(row=1, column=0, padx=6, pady=6)

tk.Button(btn_frame, text="Search Item", width=12, bg="#F59E0B", fg="white",
          font=("Segoe UI", 11, "bold"), command=search_item).grid(row=1, column=1, padx=6, pady=6)

tk.Button(root, text="Clear List", width=26, bg="#9333EA", fg="white",
          font=("Segoe UI", 11, "bold"), command=clear_list).pack(pady=8)

# ---------------- Listbox ----------------
listbox = tk.Listbox(root, font=("Segoe UI", 12), width=30, height=12,
                     bg="#F9FAFB", fg="#1F2933", selectbackground="#60A5FA", selectforeground="white")
listbox.pack(pady=15)

# ---------------- Count Label ----------------
count_label = tk.Label(root, text="Total Items: 0", font=("Segoe UI", 10, "bold"),
                       bg="#FFFFFF", fg="#1F2933")
count_label.pack()

# ---------------- Footer ----------------
footer = tk.Label(root, text="Professional Project • Python Tkinter",
                  font=("Segoe UI", 9), bg="#FFFFFF", fg="#6B7280")
footer.pack(pady=10)

# ---------------- Run ----------------
root.mainloop()

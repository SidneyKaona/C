import tkinter as tk
from tkinter import messagebox

# ---------- APP WINDOW ----------
root = tk.Tk()
root.title("Invoice Generator")
root.geometry("500x600")

# ---------- FUNCTIONS ----------
def generate_invoice():
    try:
        name = entry_worker.get()
        company= entry_company.get()
        description = entry_desc.get()

        rate_per_class = 1500
        classes_per_day = 2
        rate_per_day = rate_per_class * classes_per_day

        total_fridays = 8
        missed_fridays = 2
        days_worked = total_fridays - missed_fridays

        total_amount = days_worked * rate_per_day

        invoice_text.delete("1.0", tk.END)

        invoice_text.insert(tk.END, "========= INVOICE =========\n")
        invoice_text.insert(tk.END, f"Worker: {name}\n")
        invoice_text.insert(tk.END, f"Client: {company}\n")
        invoice_text.insert(tk.END, f"Work: {description}\n\n")

        invoice_text.insert(tk.END, f"Rate per class: Ksh {rate_per_class}\n")
        invoice_text.insert(tk.END, f"Classes per day: {classes_per_day}\n")
        invoice_text.insert(tk.END, f"Rate per day: Ksh {rate_per_day}\n\n")

        invoice_text.insert(tk.END, f"Days worked: {days_worked}\n")
        invoice_text.insert(tk.END, f"Total amount: Ksh {total_amount}\n")
        invoice_text.insert(tk.END, "===========================\n")

    except:
        messagebox.showerror("Error", "Please fill all fields")

# ---------- INPUT FIELDS ----------
tk.Label(root, text="Worker Name").pack()
entry_worker = tk.Entry(root)
entry_worker.pack()

tk.Label(root, text="Company's Name").pack()
entry_company = tk.Entry(root)
entry_company.pack()

tk.Label(root, text="Work Description").pack()
entry_desc = tk.Entry(root)
entry_desc.pack()

# ---------- BUTTON ----------
tk.Button(root, text="Generate Invoice", command=generate_invoice).pack(pady=10)

# ---------- OUTPUT BOX ----------
invoice_text = tk.Text(root, height=20, width=60)
invoice_text.pack()

# ---------- RUN APP ----------
root.mainloop()
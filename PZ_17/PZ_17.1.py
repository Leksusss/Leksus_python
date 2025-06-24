import tkinter as tk
from tkinter import ttk

def submit_form():
    print("Кнопка нажата")

root = tk.Tk()
root.title("Certificate Self Service Portal")


ttk.Label(root, text="Certificate Self Service Portal", font=("Arial", 14, "bold")).pack(pady=10)
ttk.Label(root, text="Fill out the form to get a certificate.").pack()

# весь ввод
form_frame = ttk.Frame(root, padding=10)
form_frame.pack(fill="x")

entries = {}
fields = [("Requester", "firstname lastname"), ("Short Name", "asdf"),
          ("Email", "mail@mail.com"), ("Organization", "Organization"),
          ("Country", "Austria"), ("IPv4 Address", "127.0.0.1"),
          ("Hostname", "host"), ("FQDN", "host.domain.tld")]

for i, (label, default) in enumerate(fields):
    ttk.Label(form_frame, text=label).grid(row=i, column=0, sticky="w", pady=2)
    if label == "Country":
        entry = ttk.Combobox(form_frame, values=["Austria", "Germany", "France", "USA"])
        entry.set(default)
    else:
        entry = ttk.Entry(form_frame)
        entry.insert(0, default)
    entry.grid(row=i, column=1, sticky="ew", padx=5, pady=2)
    entries[label] = entry


ttk.Label(form_frame, text="Description").grid(row=len(fields), column=0, sticky="nw", pady=5)
desc_text = tk.Text(form_frame, height=4)
desc_text.insert("1.0", "desc")
desc_text.grid(row=len(fields), column=1, sticky="ew", padx=5, pady=2)

# Кнопочка
ttk.Button(root, text="Submit Form", command=submit_form).pack(pady=10)

form_frame.columnconfigure(1, weight=1)
root.mainloop()
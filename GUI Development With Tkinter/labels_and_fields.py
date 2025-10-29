import tkinter as tk
from tkinter import ttk

def greet():
    print(f"Hello, {your_name.get() or 'World' }")

root = tk.Tk()
root.title('Greeter')

your_name = tk.StringVar()

name_label = ttk.Label(root,text="Name: ")
name_label.pack(side="left",padx=(0,10)) #adding spacing into right side of item

name_entry = ttk.Entry(root,width=15,textvariable=your_name)
name_entry.pack(side="left")
name_entry.focus()

greet_button = ttk.Button(root,text="Greet",command=greet)
greet_button.pack(side="left",fill="x",expand=True)

root.mainloop()
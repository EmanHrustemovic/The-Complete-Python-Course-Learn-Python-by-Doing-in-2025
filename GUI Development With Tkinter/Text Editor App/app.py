import tkinter as tk
from tkinter import ttk


def create_file():
    text_area = tk.Text(notebook)
    text_area.pack(fill="both", expand=True)
    notebook.add(text_area, text="Untitled")
    notebook.select(text_area)

root = tk.Tk()

main = tk.Frame(root)
main.pack(fill="both", expand=True, padx=1, pady=(4,0) )


notebook = ttk.Notebook()
notebook.pack(fill="both", expand=True)
create_file()

root.mainloop()
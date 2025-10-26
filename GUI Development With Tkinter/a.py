"""
import tkinter
tkinter.test()
"""
import tkinter as tk

root = tk.Tk()
root.title("Moj prvi Tkinter prozor")
root.geometry("300x200")

label = tk.Label(root, text="Tkinter radi!")
label.pack(pady=20)

root.mainloop()

"""
import tkinter
tkinter.test()
"""
import tkinter as tk
from tkinter import ttk

def greet():
    print('Hello world in Tkinter !!')

root = tk.Tk()
root.title('Hello')

greet_buton = ttk.Button(root,text="Greet",command=greet)
greet_buton.pack(side="left",fill="x",expand=True)

quit_button = ttk.Button(root,text="Quit",command=root.destroy)
quit_button.pack(side="left",fill="x",expand=True)

root.mainloop()

greet()

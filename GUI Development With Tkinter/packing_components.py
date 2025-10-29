import tkinter as tk

root = tk.Tk()

tk.Label(root,text="Label 1",background="green").pack(side="left",fill="both",expand=True)
tk.Label(root,text="Label 2",background="red").pack(side="top",fill="both")


root.mainloop()
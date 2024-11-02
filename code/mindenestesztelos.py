'''from subprocess import call

def open_py_file():
    call(["python","./code/bejelentkezes.py"])

open_py_file()

import tkinter as tk
from tkinter import ttk

def on_select(event):
    selected_item = combo_box.get()
    label.config(text="Selected Item: " + selected_item)

root = tk.Tk()
root.title("Combobox Example")

# Create a label
label = tk.Label(root, text="Selected Item: ")
label.pack(pady=10)

# Create a Combobox widget
combo_box = ttk.Combobox(root, values=["Option 1", "Option 2", "Option 3"])
combo_box.pack(pady=5)

# Set default value
combo_box.set("Option 1")

# Bind event to selection
combo_box.bind("<<ComboboxSelected>>", on_select)

root.mainloop()'''
#from tkinter import *

"""m1 = PanedWindow()
m1.pack(fill=BOTH, expand=1)
left = Entry(m1, bd=5)
m1.add(left)
m2 = PanedWindow(m1, orient=VERTICAL)
m1.add(m2)
top = Scale(m2, orient=HORIZONTAL)
m2.add(top)
mainloop()"""
import tkinter as tk
from tkinter import ttk

def display_range(a, b):
    label["text"] = f"Range: {a}-{b}"

root = tk.Tk()
root.geometry("400x300")
listbox = tk.Listbox(yscrollcommand=display_range)
listbox.insert(tk.END, *(f"Element {i}" for i in range(100)))
listbox.pack()
label = ttk.Label()
label.pack()
root.mainloop()


from tkinter import *
import os
from subprocess import call

root = Tk()
root.title("CsoPort")
root.minsize(500, 250)
root.maxsize(500,250)
root.configure(background="cadetblue")

def reg():
    root.destroy()
    call(["python","./code/regisztracio.py"])
    

def open_py_file():
    root.destroy()
    call(["python","./code/bejelentkezes.py"])
    

btn = Button(root, text="Regisztráció", command=reg)
btn.place(rely=0.4, relx=0.5,anchor=N)

Tk.btn2 = Button(root, text="Bejelentkezés", command = open_py_file)
Tk.btn2.place(rely=0.2, relx=0.5, anchor=N)

bezaras = Button(root, text="X",padx=5,pady=5,fg="red",bg="white" ,command=root.destroy)
bezaras.place(relx=0.5,rely=0.8, anchor=N)

root.mainloop()



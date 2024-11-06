from tkinter import *
import os
from subprocess import call

root = Tk()
root.title("miniapp")
root.minsize(500, 250)
root.maxsize(500,250)
root.configure(background="cadetblue")

def reg():
    root.destroy()
    call(["python","./code/regisztracio.py"])
    

def open_py_file():
    root.destroy()
    call(["python","./code/bejelentkezes.py"])
    

appnev=Label(root, text="Miniapp")
appnev.place(rely=0.1, relx=0.5,anchor=N)
btn = Button(root, text="Regisztráció", command=reg)
btn.place(rely=0.6, relx=0.5,anchor=N)

Tk.btn2 = Button(root, text="Bejelentkezés", command = open_py_file)
Tk.btn2.place(rely=0.5, relx=0.6)

bezaras = Button(root, text="X",padx=10,pady=10,fg="red",bg="white" ,command=root.destroy)
bezaras.place(relx=0.5,rely=0.7, anchor=N)

root.mainloop()



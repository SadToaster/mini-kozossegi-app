from tkinter import *
import os
from subprocess import call


# Mindent widgetként adunk hozzá

# Root -> a fő widget (a fő ablak)
root = Tk()
root.title("miniapp")
root.minsize(500, 250)

def reg():
    root.destroy()
    call(["python","./code/regisztracio.py"])

def open_py_file():
    root.destroy()
    call(["python","./code/bejelentkezes.py"])
    

appnev=Label(root, text="Miniapp")
appnev.place(rely=0.2, relx=0.4)
btn = Button(root, text="Regisztráció", command=reg)
btn.place(rely=0.5, relx=0.2)

Tk.btn2 = Button(root, text="Bejelentkezés", command = open_py_file)
Tk.btn2.place(rely=0.5, relx=0.6)

bezaras = Button(root, text="X",padx=10,pady=10,fg="red",bg="white" ,command=root.destroy)
bezaras.place(relx=0.5,rely=0.7, anchor=N)

root.mainloop()



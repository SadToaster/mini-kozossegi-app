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

btn2 = Button(root, text="Bejelentkezés", command = open_py_file)
btn2.place(rely=0.4, relx=0.5,anchor=N)

root.mainloop()
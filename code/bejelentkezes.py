from tkinter import*
from tkinter import Tk, BOTH
from tkinter.ttk import Frame, Label, Style
import os
from subprocess import call

root = Tk()
root.title("Mini-közösségi app")
root.maxsize(800,400)
root.minsize(800,400)
root.configure(background="cadetblue")

felhasznalo = Entry(root, width=50, bg="white", fg="black", borderwidth=10)
felhasznalo.insert(0, "Felhasználónév")
felhasznalo.place(relx=0.5,rely=0.1,anchor=N)

jelszo= Entry(root, width=50, bg="white",fg="black", borderwidth=10)
jelszo.insert(0, "Jelszó")
jelszo.place(relx=0.5,rely=0.25,anchor=N)

bejeadatok = []
with open("./code/bejelentkezes.txt",'r', encoding='utf-8') as file:
    for i in file:
        adat = i.strip().split(';')
        bejeadatok.append({
            'felnev' : str(adat[0]),
            'jelszo' : str(adat[1]),
            'azonosito' : int(adat[2])
        })

def bejelent():
    ent = felhasznalo.get()
    jeent = jelszo.get()
    global bejeadatok
    x = 0
    for i in bejeadatok:
        if ent == i['felnev'] and jeent == i['jelszo']:
            jo_e.config(text="Sikeres bejelentkezés")
            with open("./code/aktualisfelhasznalo.txt","w",encoding="utf-8") as akfel:
                print(f"{i['felnev']};{i['azonosito']}", file=akfel)
            x += 1
            root.destroy()
            call(["python","./code/fal.py"])
    
    if x == 0:
        jo_e.config(text="Sikertelen bejelentkezés!")
            

bejelentkezobt = Button(root, text="Bejelentkezés", padx=10, pady=10, command=bejelent, fg="black", bg="white")
bejelentkezobt.place(relx=0.5, rely=0.5, anchor=N)
bezaras = Button(root, text="X",padx=10,pady=10,fg="red",bg="white" ,command=root.destroy)
bezaras.place(relx=0.5,rely=0.7, anchor=N)
jo_e = Label(root, text="")
jo_e.place(relx=0.5,rely=0.85, anchor=N)

root.mainloop()
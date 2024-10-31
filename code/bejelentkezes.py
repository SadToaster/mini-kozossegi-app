from tkinter import*
from tkinter import Tk, BOTH
from tkinter.ttk import Frame, Label, Style
import fal

root = Tk()
root.title("Mini-közösségi app")
root.geometry("800x400")
root.configure(background="cadetblue")

felhasznalo = Entry(root, width=50, bg="white", fg="black", borderwidth=10)
felhasznalo.insert(0, "Felhasználónév")
felhasznalo.place(relx=0.5,rely=0.1,anchor=N)


jelszo= Entry(root, width=50, bg="white",fg="black", borderwidth=10)
jelszo.insert(0, "Jelszó")
jelszo.place(relx=0.5,rely=0.25,anchor=N)


bejeadatok = []
with open("./mini-kozossegi-app/code/bejelentkezes.txt",'r', encoding='utf-8') as file:
    for i in file:
        adat = i.strip().split(';')
        bejeadatok.append({
            'felnev' : str(adat[0]),
            'jelszo' : str(adat[1])
        })


def bejelent():
    ent = felhasznalo.get()
    jeent = jelszo.get()
    global bejeadatok
    x = 0
    for i in bejeadatok:
        if ent == i['felnev'] and jeent == i['jelszo']:
            fal.open_window(ent)
            léböl.config(text="Sikeres bejelentkezés")
            x += 1
    
    if x == 0:
        léböl.config(text="Sikertelen bejelentkezés!")
            
    



button = Button(root, text="Bejelentkezés", padx=10, pady=10, command=bejelent, fg="black", bg="white")
button.place(relx=0.5, rely=0.5, anchor=N)
btn2 = Button(root, text="X",padx=10,pady=10,fg="red",bg="white" ,command=root.destroy)
btn2.place(relx=0.5,rely=0.7, anchor=N)
léböl = Label(root, text="")
léböl.place(relx=0.5,rely=0.85, anchor=N)




root.mainloop()
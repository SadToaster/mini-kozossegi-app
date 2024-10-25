from tkinter import *
import os

# Mindent widgetként adunk hozzá

# Root -> a fő widget (a fő ablak)
root = Tk()
root.title("miniapp")
root.minsize(500, 250)

def reg():
    regiszt = Toplevel()
    

    regiszt.minsize(500,500)
    regiszt.maxsize(500,500)
    regiszt.title("Regisztráció")
    felhasznev = Entry(regiszt, width=50, bg="orange", borderwidth=10)
    felhasznev.place(rely=0.3,relx=0.5, anchor=N)
    jelsz = Entry(regiszt, width=50, bg="orange", borderwidth=10)
    jelsz.place(rely=0.5,relx=0.5, anchor=N)
    jelszbiztos = Entry(regiszt, width=50, bg="orange", borderwidth=10)
    jelszbiztos.place(rely=0.7,relx=0.5, anchor=N)
    lbl = Label(regiszt, text="Regisztráció")
    lbl.place(rely=0.1,relx=0.5, anchor=N)
    lbl1 = Label(regiszt, text="Felhasználónév")
    lbl1.place(rely=0.2,relx=0.2, anchor=N)
    lbl2 = Label(regiszt, text="Jelszó")
    lbl2.place(rely=0.4,relx=0.2, anchor=N)
    lbl3 = Label(regiszt, text="Ismételje meg a jelszót:")
    lbl3.place(rely=0.6,relx=0.2, anchor=N)
    btn2 = Button(regiszt, text="Bezárás", command=regiszt.destroy)
    btn2.place(rely=0.9, relx=0.5, anchor=N)
    
    
    

    def regisztralas():
        felhasznalonev=felhasznev.get()
        jelszo=jelsz.get()
        jelszobiztos=jelszbiztos.get()
        if jelszo==jelszobiztos:
            with open("./Mr.Dalma/bejelentkezes.txt", "a", encoding="utf-8") as file:
                print(f"\n{felhasznalonev};{jelszo}", file=file)
                
        else:
            print("Ide majd egy messagebox, hogy nem jó")



    btn3 = Button(regiszt, text="Regisztrálok", command=regisztralas)
    btn3.place(rely=0.8, relx=0.5, anchor=N)
    btn3 = Button(regiszt, text="Regisztrálok", command=regisztralas)
    btn3.place(rely=0.8, relx=0.5, anchor=N)

def masikfilenyitas():
    print("gatya")


appnev=Label(root, text="Miniapp")
appnev.place(rely=0.2, relx=0.4)
btn = Button(root, text="Regisztráció", command=reg)
btn.place(rely=0.5, relx=0.2)
btn2 = Button(root, text="Bejelentkezés", command=masikfilenyitas)
btn2.place(rely=0.5, relx=0.6)

# Event loop létrehozása
root.mainloop()
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
    """regiszt = Toplevel()
    

    regiszt.minsize(500,500)
    regiszt.maxsize(500,500)
    regiszt.title("Regisztráció")
    felhasznev = Entry(regiszt, width=50, bg="orange", borderwidth=10)
    felhasznev.place(rely=0.3,relx=0.2, anchor=W)
    jelsz = Entry(regiszt, width=50, bg="orange", borderwidth=10)
    jelsz.place(rely=0.5,relx=0.2, anchor=W)
    jelszbiztos = Entry(regiszt, width=50, bg="orange", borderwidth=10)
    jelszbiztos.place(rely=0.7,relx=0.2, anchor=W)
    lbl = Label(regiszt, text="Regisztráció")
    lbl.place(rely=0.1,relx=0.2, anchor=W)
    lbl1 = Label(regiszt, text="Felhasználónév")
    lbl1.place(rely=0.2,relx=0.2, anchor=W)
    lbl2 = Label(regiszt, text="Jelszó")
    lbl2.place(rely=0.4,relx=0.2, anchor=W)
    lbl3 = Label(regiszt, text="Ismételje meg a jelszót:")
    lbl3.place(rely=0.6,relx=0.2, anchor=W)
    btn2 = Button(regiszt, text="Bezárás", command=regiszt.destroy)
    btn2.place(rely=0.9, relx=0.5, anchor=N)
    
    
    

    def regisztralas():
        felhasznalonev=felhasznev.get()
        jelszo=jelsz.get()
        jelszobiztos=jelszbiztos.get()
        adatok=[]
        with open("./code/bejelentkezes.txt", "r", encoding="utf-8") as file:
            for sor in file:
                adat = sor.strip().split(';')
                adatok.append({
                    'felhasznev' : adat[0],
                    'jelszo' : adat[1],
                    'azonosito' : int(adat[2])
                })
        
        vanvagynincs=False

        for i in adatok:
            if felhasznalonev==i['felhasznev']:
                vanvagynincs=True
                break
            else:
                pass
        
        x=adatok[-1]['azonosito']+1

        if jelszo==jelszobiztos and vanvagynincs==False:
            with open("./code/bejelentkezes.txt", "a", encoding="utf-8") as file:
                print(f"\n{felhasznalonev};{jelszo};{x}", file=file)
            
        else:
            print("Ide majd egy messagebox, hogy nem jó")



    btn3 = Button(regiszt, text="Regisztrálok", command=regisztralas)
    btn3.place(rely=0.8, relx=0.5, anchor=N)
    ez már új pythonba van"""

def open_py_file():
    root.destroy()
    call(["python","./code/bejelentkezes.py"])
    

appnev=Label(root, text="Miniapp")
appnev.place(rely=0.2, relx=0.4)
btn = Button(root, text="Regisztráció", command=reg)
btn.place(rely=0.5, relx=0.2)

Tk.btn2 = Button(root, text="Bejelentkezés", command = open_py_file)
Tk.btn2.place(rely=0.5, relx=0.6)

root.mainloop()

"""ezek együtt fontosak
from subprocess import call
def open_py_file():
    call(["python","./code/bejelentkezes.py"])"""

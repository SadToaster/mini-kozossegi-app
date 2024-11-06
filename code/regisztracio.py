from tkinter import *
from subprocess import call

regiszt = Tk()
regiszt.configure(background="cadetblue")
    
def regisztbezar():
    regiszt.destroy()
    call(["python","./code/alap.py"])
    
    
    
sikornemsik=Label(regiszt, text="")
sikornemsik.place(rely=0.75,relx=0.5,anchor=N)

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
                    'azonosito' : int(adat[2])
                })
        
    vanvagynincs=True

    for i in adatok:
        if felhasznalonev==i['felhasznev']:
            vanvagynincs=False
            sikornemsik.config(text="Márlétezik ilyen nevű felhasználó")
            break
        else:
            pass
        
    x=adatok[-1]['azonosito']+1

    if jelszo==jelszobiztos and vanvagynincs:
        with open("./code/bejelentkezes.txt", "a", encoding="utf-8") as file:
            print(f"\n{felhasznalonev};{jelszo};{x}", file=file)
        sikornemsik.config(text="Sikeres regisztráció!")
            
    else:
        sikornemsik.config(text="Nem egyezik a jelszó a két mezőben.")


regiszt.minsize(500,500)
regiszt.maxsize(500,500)
regiszt.title("Regisztráció")
felhasznev = Entry(regiszt, width=50, bg="white", borderwidth=10)
felhasznev.place(rely=0.3,relx=0.2, anchor=W)
jelsz = Entry(regiszt, width=50, bg="white", borderwidth=10)
jelsz.place(rely=0.5,relx=0.2, anchor=W)
jelszbiztos = Entry(regiszt, width=50, bg="white", borderwidth=10)
jelszbiztos.place(rely=0.7,relx=0.2, anchor=W)
lbl = Label(regiszt, text="Regisztráció")
lbl.place(rely=0.1,relx=0.2, anchor=W)
lbl1 = Label(regiszt, text="Felhasználónév")
lbl1.place(rely=0.2,relx=0.2, anchor=W)
lbl2 = Label(regiszt, text="Jelszó")
lbl2.place(rely=0.4,relx=0.2, anchor=W)
lbl3 = Label(regiszt, text="Ismételje meg a jelszót:")
lbl3.place(rely=0.6,relx=0.2, anchor=W)
btn2 = Button(regiszt, text="Bezárás", command=regisztbezar)
btn2.place(rely=0.91, relx=0.5, anchor=N)
btn3 = Button(regiszt, text="Regisztrálok", command=regisztralas)
btn3.place(rely=0.83, relx=0.5, anchor=N)


regiszt.mainloop()
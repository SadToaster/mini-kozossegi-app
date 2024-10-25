from tkinter import*
from tkinter import Tk, BOTH
from tkinter.ttk import Frame, Label, Style

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
with open('./bejelentkezes.txt','r', encoding='utf-8')as file:
    for i in file:
        adat = i.strip().split(';')
        bejeadatok.append({
            'felnev' : str(adat[0]),
            'jelszo' : str(adat[1])
        })

   
def bejelentkezes():
    global felhasznalo
    global jelszo
    global bejeadatok
<<<<<<< HEAD:code/dalma.py
    global funkciok
    x=False
    for i in bejeadatok:
        if felhasznalo == i['felnev'] and jelszo == i['jelszo']:
            funkciok = Tk() 
            funkciok=Toplevel(root)
            funkciok.title("Funkciok")
            funkciok.config(width=300, height=200)
            funkciok.mainloop()
            x=True
            break
        else:
            continue
    
    if x:
        root.destroy()
    
            
        
=======
    index = 0
    for i in bejeadatok:
        if felhasznalo == i['felnev'] and jelszo == i['jelszo']:
            print("asd")
            index = i
            asd=Tk()
            asd.title("új")
            asd.geometry("400x400")
            asd.mainloop()
    
    

>>>>>>> 9113b231e711a1b0f818804574635c0dc808e3ab:Mr.Dalma/dalma.py


button = Button(root, text="Bejelentkezés", padx=10, pady=10, command=bejelentkezes(), fg="black", bg="white")
button.place(relx=0.5, rely=0.5, anchor=N)
btn2 = Button(root, text="X",padx=10,pady=10,fg="red",bg="white" ,command=root.destroy)
btn2.place(relx=0.5,rely=0.7, anchor=N)



root.mainloop()
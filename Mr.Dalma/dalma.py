from tkinter import*
from tkinter import Tk, BOTH
from tkinter.ttk import Frame, Label, Style

root = Tk()
root.title("Mini-közösségi app")
root.geometry("800x400")

felhasznalo = Entry(root, width=50, bg="cadet blue", fg="white", borderwidth=10)
felhasznalo.insert(0, "")
felhasznalo.place(relx=0.25,rely=0.1,anchor=N)

jelszo= Entry(root, width=50, bg="cadet blue",fg="white", borderwidth=10)
jelszo.insert(0, "")
jelszo.place(relx=0.7,rely=0.1,anchor=N)

def bejelentkezes():
    global felhasznalo
    global jelszo
    if felhasznalo == "Levi69420" and jelszo == "BoldogtalanvagyokLOL10":
        print("asd")
    elif felhasznalo == "Máté69421" and jelszo == "BoldogtalanvagyokLOL11":
        print("asd")

bejelentkezes()

button = Button(root, text="Bejelentkezés", padx=10, pady=10, command=bejelentkezes, fg="white", bg="cadetblue")
button.place(relx=0.5, rely=0.25, anchor=N)
btn2 = Button(root, text="Bezárás",padx=10,pady=10, command=root.destroy)
btn2.place(relx=0.5,rely=0.75, anchor=N)






root.mainloop()
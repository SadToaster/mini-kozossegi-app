from tkinter import*
from tkinter import Tk, BOTH
from tkinter.ttk import Frame, Label, Style
import profil


def open_window(felnev):
    global entri
    global posz
    root = Tk()
    root.title("Közösségi fal")
    root.geometry("800x600")
    root.configure(background="cadetblue")
    posz = Label(root,text="")
    posz.place(relx=0.1,rely=0.1,anchor=N)
    entri = Entry(root, width=50, bg="white", fg="black", borderwidth=10)
    entri.insert(0,"Mi jár a fejedben?")
    def posztolas():
        global entri
        global posz
        getter = entri.get()
        post = []
        with open("./mini-kozossegi-app/code/fal.txt","a",encoding="utf-8")as file:
            print(f"{felnev}\n{getter}",file=file)
        with open("./mini-kozossegi-app/code/fal.txt","r",encoding="utf-8")as fajl:
            for i in fajl:
                post.append(
                    i
                )
        print(post)
        kiiratas=str(post)
        kiiratas=kiiratas.replace("[","")
        kiiratas=kiiratas.replace("]","")
        posz.config(text='\n'.join(map(str, post)))
    entri.place(relx=0.25,rely=0.7,anchor=N)
    validalo = Button(root,text="Posztolás",padx=10, pady=10,command=posztolas)
    validalo.place(relx=0.1,rely=0.8,anchor=N)
    def prgab():
        profil.profil_galeria()
    gab = Button(root,text="Profil/galéria",command=prgab,padx=10,pady=10,fg="black", bg="white")
    gab.place(relx=0.8,rely=0.1,anchor=N)


open_window("asd")
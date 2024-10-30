from tkinter import*
from tkinter import Tk, BOTH
from tkinter.ttk import Frame, Label, Style


def open_window(felnev):
    global entri
    global posz
    root = Tk()
    root.title("Közösségi fal")
    root.geometry("800x600")
    root.configure(background="cadetblue")
    posz = Label(root,text="")
    posz.place(relx=0.5,rely=0.1,anchor=N)
    entri = Entry(root, width=50, bg="white", fg="black", borderwidth=10)
    entri.insert(0,"Mi jár a fejedben?")
    def posztolas():
        global entri
        global posz
        getter = entri.get()
        post = []
        with open("./mini-kozossegi-app/code/fal.txt","a",encoding="utf-8")as file:
            print(felnev,getter,sep=';',file=file)
        with open("./mini-kozossegi-app/code/fal.txt","r",encoding="utf-8")as fajl:
            for i in fajl:
                adat = i.strip().split(';')
                post.append({
                    'felnev' : str(adat[0]),
                    'po' : str(adat[1])
                })
        for a in range(post.lenght()):
            posz.config(text=f"{post[a]["felnev"]} 99{post[a]["po"]}")
    entri.place(relx=0.25,rely=0.7,anchor=N)
    validalo = Button(root,text="Posztolás",padx=10, pady=10,command=posztolas)
    validalo.place(relx=0.1,rely=0.8,anchor=N)


open_window("asd")
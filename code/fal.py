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
    posz.place(relx=0.1,rely=0.1,anchor=N)
    entri = Entry(root, width=50, bg="white", fg="black", borderwidth=10)
    entri.insert(0,"Mi jár a fejedben?")
    entri.place(relx=0.25,rely=0.7,anchor=N)
    validalo = Button(root,text="Posztolás",padx=10, pady=10,command=posztolas)
    validalo.place(relx=0.1,rely=0.8,anchor=N)
def posztolas():
    global entri
    global posz
    getter = entri.get()
    posz = Label(text=getter)

open_window("asd")
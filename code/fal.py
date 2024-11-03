from tkinter import*
from tkinter import Tk, BOTH
from tkinter.ttk import Frame, Label, Style
import profil
import tkinter as tk
from tkinter import ttk


def open_window(felnev):
    global entri
    global posz
    root = Tk()
    root.title("Közösségi fal")
    root.geometry("800x600")
    root.configure(background="cadetblue")
    entri = Entry(root, width=50, bg="white", fg="black", borderwidth=10)
    entri.insert(0,"Mi jár a fejedben?")
    entri.place(relx=0.25,rely=0.7,anchor=N)
    def posztolas():
        global entri
        global posz
        getter = entri.get()
        post = []
        posz = tk.Label(root, text="Posztolás:")
        posz.place(relx=0.1,rely=10000,anchor=N)
        with open("./code/fal.txt","a",encoding="utf-8")as file:
            print(f"{felnev}\n{getter}",file=file)
        with open("./code/fal.txt","r",encoding="utf-8")as fajl:
            for i in fajl:
                post.append(
                    i
                )
        kiiratas=str(post)
        kiiratas=kiiratas.replace("[","")
        kiiratas=kiiratas.replace("]","")
        def display_range(a, b):
            posz["text"] = f"Range: {a}-{b}"
        listbox = tk.Listbox(yscrollcommand=display_range, width=80)
        listbox.insert(tk.END, *(post[i] for i in range(len(post))))
        listbox.place(rely=0.4, relx=0.05, anchor=W, height=250)
    validalo = Button(root,text="Posztolás",padx=10, pady=10,command=posztolas)
    validalo.place(relx=0.1,rely=0.8,anchor=N)
    def prgab():
        profil.profil_galeria()
    gab = Button(root,text="Profil/galéria",command=prgab,padx=10,pady=10,fg="black", bg="white")
    gab.place(relx=0.8,rely=0.1,anchor=N)
    


open_window("asd")
from tkinter import*
from tkinter import Tk, BOTH
from tkinter.ttk import Frame, Label, Style

root = Tk()
root.title("Közösségi fal")
root.geometry("800x600")
root.configure(background="cadetblue")
posz = Label(root,text="")
posz.place(relx=0.1,rely=0.1,anchor=N)
entri = Entry(root, width=50, bg="white", fg="black", borderwidth=10)
entri.insert(2,"Mi jár a fejedben?")
entri.place(relx=0.25,rely=0.7,anchor=N)
validalo = Button(root,text="Posztolás")
validalo.place(relx=0.1,rely=0.8,anchor=N)


root.mainloop()
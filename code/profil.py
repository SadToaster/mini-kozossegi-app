from tkinter import*
from PIL import Image, ImageTk
from subprocess import call


root = Tk()
root.title("CsoPort")
root.maxsize(1100,750)
root.minsize(1100,750)
root.configure(background="cadetblue")

tunnerlabel = Label(root,text="Tunner Máté Albert")
tunnerlabel.place(relx=0.32,rely=0.02,anchor=N)
tunnerbemutatkozas = Label(root, text="Tunner Máté (alias Mr. szomorú)\n-a Veszprém SZC Ipari Technikumba jár informatika szakra\n-Hobbija az aktív sportolás és az olvasás.\n-Szereti: a könnyed, de nem üres beszédet\n-Nem szereti: a hivalkodó embereket",justify=LEFT)
tunnerbemutatkozas.place(relx=0.8,rely=0.21,anchor=N)

tunner1 = ImageTk.PhotoImage(Image.open("./code/img/tunner8.jpg").resize((290, 290)))
tunner2 = ImageTk.PhotoImage(Image.open("./code/img/tunner2.jpg").resize((290, 290)))
tunner3 = ImageTk.PhotoImage(Image.open("./code/img/tunner6.jpg").resize((290, 290)))
tunner4 = ImageTk.PhotoImage(Image.open("./code/img/tunner3.jpg").resize((290, 290)))
tunner5 = ImageTk.PhotoImage(Image.open("./code/img/tunner4.jpg").resize((290, 290)))

image_list = [tunner1, tunner2, tunner3, tunner4, tunner5]

global counter

counter = 0

def forwChangeImage():
    global counter
    if abs(counter) < len(image_list) - 1:
        counter += 1
    else:
        counter = 0
    imageLabel.config(image=image_list[counter])
    
def backChangeImage():
    global counter
    if abs(counter) < len(image_list) - 1:
        counter -= 1
    else:
        counter = 0
    imageLabel.config(image=image_list[counter])
    

imageLabel = Label(root, image=tunner1)
imageLabel.place(relx=0.32,rely=0.06,anchor=N)
next1 = Button(root, text="következő", width=20, height=2, bg="white", fg="black", command=forwChangeImage)
previous1 = Button(root, text="előző", width=20, height=2, bg="white", fg="black", command=backChangeImage)
next1.place(relx=0.55,rely=0.25,anchor=N)
previous1.place(relx=0.09,rely=0.25,anchor=N)

levilabel = Label(root,text="Nagy Levente")
levilabel.place(relx=0.32,rely=0.5,anchor=N)
levibemutatkozás = Label(root,text="Nagy Levente (alias Mr. Dalma)\n-a Veszprém SZC Ipari Technikumba jár informatika szakra\n-Hobbija a biciklizés, futás, túrázás\n-Szereti: sporttal töltött időt\n-Nem szereti:káposzta\n-Dzsáber the biggest, lelőlek szeretettel.(4.kép)" ,justify=LEFT)
levibemutatkozás.place(relx=0.8,rely=0.67,anchor=N)

levi1 = ImageTk.PhotoImage(Image.open("./code/img/levi2.jpg").resize((290, 290)))
levi2 = ImageTk.PhotoImage(Image.open("./code/img/levi1.jpg").resize((290, 290)))
levi3 = ImageTk.PhotoImage(Image.open("./code/img/levi3.jpg").resize((290, 290)))
levi4 = ImageTk.PhotoImage(Image.open("./code/img/levi4.jpg").resize((290, 290)))
levi5 = ImageTk.PhotoImage(Image.open("./code/img/levi5.jpg").resize((290, 290)))

image_listlevi = [levi1, levi2, levi3, levi4, levi5]

global counterlevi

counterlevi = 0

def forwChangeImagelevi():
    global counterlevi
    if abs(counterlevi) < len(image_listlevi) - 1:
        counterlevi += 1
    else:
        counterlevi = 0
    imageLabellevi.config(image=image_listlevi[counterlevi])
    
def backChangeImagelevi():
    global counterlevi
    if abs(counterlevi) < len(image_listlevi) - 1:
        counterlevi -= 1
    else:
        counterlevi = 0
    imageLabellevi.config(image=image_listlevi[counterlevi])
    

imageLabellevi = Label(root, image=levi2)
imageLabellevi.place(relx=0.32,rely=0.54,anchor=N)
next2 = Button(root, text="következő", width=20, height=2, bg="white", fg="black", command=forwChangeImagelevi)
previous2 = Button(root, text="előző", width=20, height=2, bg="white", fg="black", command=backChangeImagelevi)
next2.place(relx=0.55,rely=0.7,anchor=N)
previous2.place(relx=0.09,rely=0.7,anchor=N)
def visszafal():
    root.destroy()
    call(["python","./code/fal.py"])

viszfalb= Button(root,text="Vissza a falra",command=visszafal,padx=10,pady=10,fg="black", bg="white")
viszfalb.place(relx=0.1,rely=0.01,anchor=N)
root.mainloop()
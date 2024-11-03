from tkinter import*
from tkinter import Tk, BOTH
from tkinter.ttk import Frame, Label, Style
from PIL import Image, ImageTk

def profil_galeria():
    root = Tk()
    root.title("Profil/galéria")
    root.geometry("1000x700")
    root.configure(background="cadetblue")
    nev1 = Label(root,text="Nagy Levente")
    nev1.place(relx=0.5,rely=0.05,anchor=N)
    nev2 = Label(root,text="Tunner Máté")
    nev2.place(relx=0.5,rely=0.55,anchor=N)
    image1 = ImageTk.PhotoImage(Image.open("images/01.jpg").resize((600, 350)))
    image2 = ImageTk.PhotoImage(Image.open("images/02.jpg").resize((600, 350)))
    image3 = ImageTk.PhotoImage(Image.open("images/03.jpg").resize((600, 350)))
    image4 = ImageTk.PhotoImage(Image.open("images/04.jpg").resize((600, 350)))
    image5 = ImageTk.PhotoImage(Image.open("images/05.jpg").resize((600, 350)))
    # add them to the list
    image_list = [image1, image2, image3, image4, image5]
    # counter integer
    counter = 0
    # change image function
    def ChangeImage():
        global counter
        if counter < len(image_list) - 1:
            counter += 1
        else:
            counter = 0
        imageLabel.config(image=image_list[counter])
        infoLabel.config(text="Image " + str(counter + 1) + " of " + str(len(image_list)))
    # set up the components
    imageLabel = Label(root, image=image1)
    infoLabel = Label(root, text="Image 1 of 5", font="Helvetica, 20")
    button = Button(root, text="Change", width=20, height=2, bg="purple", fg="white", command=ChangeImage)
    # display the components
    imageLabel.pack()
    infoLabel.pack()
    button.pack(side="bottom", pady=3)
    # run the main loop
    root.mainloop()
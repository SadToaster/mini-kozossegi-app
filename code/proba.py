from tkinter import*
from tkinter import Tk, BOTH
from tkinter.ttk import Frame, Label, Style
from PIL import Image, ImageTk

root = Tk()
root.title("Profil/galéria")
root.geometry("1000x700")


image1 = ImageTk.PhotoImage(Image.open("./mini-kozossegi-app/code/img/levi1.jpg").resize((600, 350)))
image2 = ImageTk.PhotoImage(Image.open("./mini-kozossegi-app/code/img/tunner1.jpg").resize((600, 350)))
image3 = ImageTk.PhotoImage(Image.open("./mini-kozossegi-app/code/img/tunner2.jpg").resize((600, 350)))
#image4 = ImageTk.PhotoImage(Image.open("images/04.jpg").resize((600, 350)))
#image5 = ImageTk.PhotoImage(Image.open("images/05.jpg").resize((600, 350)))

image_list = [image1, image2, image3]

counter = 0

def ChangeImage():
    global counter
    if counter < len(image_list) - 1:
        counter += 1
    else:
        counter = 0
    imageLabel.config(image=image_list[counter])
    infoLabel.config(text="Kép " + str(counter + 1) + " / " + str(len(image_list)))
# set up the components
imageLabel = Label(root, image=image1)
infoLabel = Label(root, text="kép 1 / 3", font="Helvetica, 20")
button = Button(root, text="Váltás", width=20, height=2, bg="black", fg="white", command=ChangeImage)
# display the components
imageLabel.pack()
infoLabel.pack()
button.pack(side="bottom", pady=3)

root.mainloop()
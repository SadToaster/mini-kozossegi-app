from tkinter import *
from PIL import ImageTk, Image
# set up the tkinter window
root = Tk()
root.title("Profil/Galéria")
root.geometry("1000x800")

# set up the images
image1 = ImageTk.PhotoImage(Image.open("./code/img/levi1.jpg").resize((600, 350)))
image2 = ImageTk.PhotoImage(Image.open("./code/img/tunner1.jpg").resize((600, 350)))
image3 = ImageTk.PhotoImage(Image.open("./code/img/tunner2.jpg").resize((600, 350)))
#image4 = ImageTk.PhotoImage(Image.open("images/04.jpg").resize((600, 350)))
#image5 = ImageTk.PhotoImage(Image.open("images/05.jpg").resize((600, 350)))
# add them to the list
image_list = [image1, image2, image3]
# counter integer
counter = 0
# change image function
def forwChangeImage():
    global counter
    if abs(counter) < len(image_list) - 1:
        counter += 1
    else:
        counter = 0
    imageLabel.config(image=image_list[counter])
    #infoLabel.config(text="Image " + str(counter + 1) + " of " + str(len(image_list)))
def backChangeImage():
    global counter
    if abs(counter) < len(image_list) - 1:
        counter -= 1
    else:
        counter = 0
    imageLabel.config(image=image_list[counter])
    #infoLabel.config(text="Image " + str(counter + 1) + " of " + str(len(image_list)))

# set up the components
imageLabel = Label(root, image=image1)
#infoLabel = Label(root, text="Image 1 of 3", font="Helvetica, 20")
button1 = Button(root, text="next", width=20, height=2, bg="purple", fg="white", command=forwChangeImage)
button2 = Button(root, text="previous", width=20, height=2, bg="purple", fg="white", command=backChangeImage)
# display the components
imageLabel.pack()
#infoLabel.pack()
button1.pack(side=RIGHT, pady=3)
button2.pack(side=LEFT, pady=3)
# run the main loop
root.mainloop()
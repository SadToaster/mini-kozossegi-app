from tkinter import Tk
from PIL import ImageTk, Image
from tkinter import Tk, BOTH
from tkinter.ttk import Frame, Label, Style

# Create a Tkinter root window
root = Tk()
root.geometry('1000x900')
root.title("Slider")

# List of image file paths
pics_list = ["./code/img/levi1.jpg",
             "./code/img/tunner1.jpg",
             "./code/img/tunner2.jpg",
             ]

levinev = Label(root,text="Nagy Levente")
levinev.place(relx=0.5,rely=0.5,anchor=N)

# Create labels for displaying image and navigation buttons
lbl_next = Label(text=">", font=("Verdana",25))
lbl_previous = Label(text="<", font=("Verdana",25))
lbl_picture = Label()
lbl_picture.place(relx=0.5,rely=0.5,anchor=N)

# Grid layout for labels
lbl_previous.grid(row=0, column=0)
lbl_picture.grid(row=0, column=1)
lbl_next.grid(row=0, column=2)

# Initialize the index to track the current image
index = 0

def nextImage():
    global index, img

    # Increment the index to show the next image in the list
    index += 1
 
    # If the index goes beyond the last image, loop back to the first image
    if index > len(pics_list) - 1:
        index = 0

    # Load and display the image at the current index
    img = Image.open(pics_list[index])
    img = img.resize((300,370))
    img = ImageTk.PhotoImage(img)
    lbl_picture['image'] = img



def previousImage():
    global index, img

    # Decrement the index to show the previous image in the list
    index -= 1

    # If the index goes below 0, loop back to the last image
    if index < 0:
        index =  len(pics_list) - 1

    # Load and display the image at the current index
    img = Image.open(pics_list[index])
    img = img.resize((330,400))
    img = ImageTk.PhotoImage(img)
    lbl_picture['image'] = img


# Bind the navigation buttons to their respective functions
lbl_next.bind("<Button-1>", lambda abc : nextImage())
lbl_previous.bind("<Button-1>", lambda abc : previousImage())


# Show the first image in the list when the program starts
nextImage()

# Start the Tkinter event loop
root.mainloop()
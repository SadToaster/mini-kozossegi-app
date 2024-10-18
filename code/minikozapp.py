from email import message
import tkinter as tk
from tkinter import ttk


def posztolas():

    post = tk.Toplevel()
    post.title("Posztolás")
    post.config(width=300, height=200)

    button_close = ttk.Button(
        post,
        text="Close window",
        command=post.destroy
    )
    button_close.place(x=75, y=75)

def uzi():

    message = tk.Toplevel()
    message.title("Üzenetváltás")
    message.config(width=400, height=600)

    uzenet_var=tk.StringVar()

    uzenet_entry = tk.Entry(message,textvariable = uzenet_var, font=('calibre',10,'normal'))

    x= uzenet_var

    button_close = ttk.Button(
        message,
        text="Close window",
        command=message.destroy
    )
    button_close.place(x=75, y=75)

def tarplat():

    tartalom = tk.Toplevel()
    tartalom.title("Fórum")
    tartalom.config(width=300, height=200)

    button_close = ttk.Button(
        tartalom,
        text="Close window",
        command=tartalom.destroy
    )
    button_close.place(x=75, y=75)


# Create the main window.
felhasznalasi_lehetosegek = tk.Tk()
felhasznalasi_lehetosegek.config(width=500, height=500)
felhasznalasi_lehetosegek.title("Felhasználási lehetőségek")
# Create a button inside the main window that
# invokes the posztolas() function
# when pressed.
poszt = ttk.Button(
    felhasznalasi_lehetosegek,
    text="Posztolás",
    command=posztolas
)
poszt.place(x=100, y=100)
uzengetes = ttk.Button(
    felhasznalasi_lehetosegek,
    text="Üzengetés",
    command=uzi
)
uzengetes.place(x=100, y=200)

tartalom_platform = ttk.Button(
    felhasznalasi_lehetosegek,
    text="Fórum",
    command=tarplat
)
tartalom_platform.place(x=100, y=300)
felhasznalasi_lehetosegek.mainloop()
from tkinter import*
from tkinter import Tk, BOTH
from tkinter.ttk import Frame, Label, Style
import tkinter as tk
from tkinter import ttk
from subprocess import call



root = Tk()
root.title("CsoPort")
root.geometry("800x400")
root.configure(background="cadetblue")
uzenet= Entry(root, textvariable="uzenet",width=100)
uzenet.place(rely=0.95, relx=0.2, anchor=W)

#felhasználó információi áthozva
with open("./code/aktualisfelhasznalo.txt","r",encoding="utf-8") as felhasz:
    for i in felhasz:
         adat = i.strip().split(';')
         felhasznalo=adat[0]
         azonosito=int(adat[1])
mindenkineve=[]
mindenkiazonositoja=[]
with open("./code/bejelentkezes.txt","r",encoding="utf-8") as osszfelhasz1:
    for i in osszfelhasz1:
            adat = i.strip().split(';')
            if adat[0]!=felhasznalo:
                mindenkineve.append(adat[0])
with open("./code/bejelentkezes.txt","r",encoding="utf-8") as osszfelhasz2:
    for i in osszfelhasz2:
            adat = i.strip().split(';')
            if int(adat[2])!=azonosito:
                mindenkiazonositoja.append(int(adat[2]))
chatazononosito=0
def on_select(event):
    kuldesbtn.config(state=ACTIVE)
    global selected_item
    selected_item = combo_box.get()
    label.config(text="Selected Item: " + selected_item)
    global chatazononosito
    chatazononosito=azonosito**azonosito+mindenkiazonositoja[mindenkineve.index(selected_item)]**mindenkiazonositoja[mindenkineve.index(selected_item)]
    uzenetek=[]
    with open("./code/uzenetek.txt","r",encoding="utf-8") as kiiras:
        for x in kiiras:
            adat = x.split(';')
            if int(adat[1])==chatazononosito:
                uzenetek.append(adat[0])
            else:
                 pass
    #chatpanel.config(text='\n'.join(map(str, uzenetek)))
    def display_range(a, b):
        label["text"] = f"Range: {a}-{b}"
    listbox = tk.Listbox(yscrollcommand=display_range, width=100)
    listbox.insert(tk.END, *(uzenetek[i] for i in range(len(uzenetek))))
    listbox.yview(END)
    listbox.place(rely=0.55, relx=0.2, anchor=W, height=280)   
    

label = tk.Label(root, text="Selected Item: ")
combo_box = ttk.Combobox(root, values=mindenkineve)
combo_box.place(rely=0.07, relx=0.57, anchor=N)
combo_box.set("Partner választó")
combo_box.bind("<<ComboboxSelected>>", on_select)


global uzenetek
uzenetek=[]
with open("./code/uzenetek.txt","r",encoding="utf-8") as kiiras:
        for x in kiiras:
            adat = x.split(';')
            if int(adat[1])==chatazononosito:
                uzenetek.append(adat[0])


def kuld():
    global uzenetek
    uzenetek=[]
    global chatazononosito
    with open("./code/uzenetek.txt","a",encoding="utf-8") as file:
        print (f"{felhasznalo}: {uzenet.get()};{chatazononosito}", file=file)
    uzenet.delete(0, END)
    with open("./code/uzenetek.txt","r",encoding="utf-8") as kiiras:
        for x in kiiras:
            adat = x.split(';')
            if int(adat[1])==chatazononosito:
                uzenetek.append(adat[0])
            else:
                 pass
    def display_range(a, b):
        label["text"] = f"Range: {a}-{b}"
    listbox = tk.Listbox(yscrollcommand=display_range, width=100)
    listbox.insert(tk.END, *(uzenetek[i] for i in range(len(uzenetek))))
    listbox.yview(END)
    listbox.place(rely=0.55, relx=0.2, anchor=W, height=280) 

def display_range(a, b):
    label["text"] = f"Range: {a}-{b}"
listbox = tk.Listbox(yscrollcommand=display_range, width=100)
listbox.insert(tk.END, *(uzenetek[i] for i in range(len(uzenetek))))
listbox.yview(END)
listbox.place(rely=0.55, relx=0.2, anchor=W, height=280) 

kuldesbtn=Button(root, text="🚀",width=3, command=kuld, bg="white")
kuldesbtn.place(rely=0.95, relx=0.96,anchor=W)
if chatazononosito==0:
     kuldesbtn.config(state=DISABLED)


def visszafal():
    root.destroy()
    call(["python","./code/fal.py"])

viszfalb= tk.Button(root,text="Vissza a falra",command=visszafal,padx=10,pady=10,fg="black", bg="white")
viszfalb.place(relx=0.1,rely=0.05,anchor=N)

root.mainloop()
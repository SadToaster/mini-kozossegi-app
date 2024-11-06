from tkinter import*
from tkinter import Tk, BOTH
from tkinter.ttk import Frame, Label, Style
import tkinter as tk
from tkinter import ttk
from subprocess import call



root = Tk()
root.title("Mini-közösségi app")
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
    listbox.place(rely=0.5, relx=0.2, anchor=W, height=250)   
    

label = tk.Label(root, text="Selected Item: ")
combo_box = ttk.Combobox(root, values=mindenkineve)
combo_box.pack(pady=5)
combo_box.set("mindegy, csak válassz")
combo_box.bind("<<ComboboxSelected>>", on_select)

"""chatpanel=Label(text="", width=100)
chatpanel.place(rely=0.6, relx=0.2, height=250 ,anchor=W)"""

def kuld():
    uzenetek=[]
    global chatazononosito
    with open("./code/uzenetek.txt","a",encoding="utf-8") as file:
        print (f"{felhasznalo}: {uzenet.get()};{chatazononosito}", file=file)
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
    listbox.place(rely=0.5, relx=0.2, anchor=W, height=250) 
      

kuldesbtn=Button(root, textvariable="📡",width=3, command=kuld)
kuldesbtn.place(rely=0.95, relx=0.96,anchor=W)

def visszafal():
    root.destroy()
    call(["python","./code/fal.py"])

viszfalb= tk.Button(root,text="Vissza a falra",command=visszafal,padx=10,pady=10,fg="black", bg="white")
viszfalb.place(relx=0.1,rely=0.01,anchor=N)

"""
x=-1
with open("./code/bejelentkezes.txt","r", encoding="utf-8") as fil:
    for i in fil:
        x+=1
w = Scale(root, from_=0, to=x)
w.place(rely=0, relx=0.007, height=400, anchor=N)"""
root.mainloop()
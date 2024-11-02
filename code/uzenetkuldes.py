from tkinter import*
from tkinter import Tk, BOTH
from tkinter.ttk import Frame, Label, Style
import tkinter as tk
from tkinter import ttk



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






def on_select(event):
    selected_item = combo_box.get()
    label.config(text="Selected Item: " + selected_item)
    global chatazononosito
    chatazononosito=azonosito**2+mindenkiazonositoja[mindenkineve.index(selected_item)]**2

              



# Create a label
label = tk.Label(root, text="Selected Item: ")
label.pack(pady=10)
combo_box = ttk.Combobox(root, values=mindenkineve)
combo_box.pack(pady=5)
# Set default value
combo_box.set("Válassz partnert")
# Bind event to selection
combo_box.bind("<<ComboboxSelected>>", on_select)


uzenetek=[]
def kuld():
    global chatazononosito
    with open("./code/uzenetek.txt","a",encoding="utf-8") as file:
        print (f"{uzenet.get()};{felhasznalo};{chatazononosito}", file=file)
    with open("./code/uzenetek.txt","r",encoding="utf-8") as kiiras:
        for i in kiiras:
            adat = i.strip().split(';')
            uzenetek.append({
                'uzenet' : adat[0],
                'felhasznev' : adat[1],
                'chatazonosito' : adat[2]
            })
kuldesbtn=Button(root, textvariable="📡",width=3, command=kuld)
kuldesbtn.place(rely=0.95, relx=0.96,anchor=W)









"""
x=-1
with open("./code/bejelentkezes.txt","r", encoding="utf-8") as fil:
    for i in fil:
        x+=1
w = Scale(root, from_=0, to=x)
w.place(rely=0, relx=0.007, height=400, anchor=N)"""
root.mainloop()

    
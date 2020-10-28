from tkinter import *
from tkinter.messagebox import *

fenetre = Tk()
fenetre.title("TxtPr")
fenetre.configure(bg="grey1")
fenetre.geometry("600x600")

def open():
    print("Open")

def save():
    print("Save")

MenuBar = Menu(fenetre)

Files = Menu(MenuBar, tearoff=0)
Files.add_command(label="Ouvrir", command=open)
Files.add_command(label="Sauvegarder", command=save)
Files.add_command(label="Quitter", command=fenetre.quit)

About = Menu(MenuBar, tearoff=1)
About.add_command(label="GitHub : Program")

MenuBar.add_cascade(label="Fichier", menu=Files)
MenuBar.add_cascade(label="A propos", menu=About)

L1 = Label(fenetre, text="<-! Write your text !->")
L1.pack(side = TOP)
E1 = Text(fenetre,bd=2, bg="thistle3", width=80, height=80)
E1.pack() 

fenetre.config(menu=MenuBar)
fenetre.mainloop()
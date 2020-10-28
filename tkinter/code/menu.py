from tkinter import *
from tkinter.messagebox import *

fenetre = Tk()

def alert():
    showinfo("alerte", "Bravo!")

menubar = Menu(fenetre)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Créer", command=alert)
menu1.add_command(label="Editer", command=alert)
menu1.add_separator()
menu1.add_command(label="Quitter", command=fenetre.quit)

menubar.add_cascade(label="Fichier", menu=menu1)

fenetre.config(menu=menubar)
fenetre.mainloop()
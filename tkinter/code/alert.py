from tkinter import *
from tkinter.messagebox import * 

fenetre = Tk()

def callback():
    if askyesno('Quitter l\'application', 'Êtes-vous sûr de vouloir faire ça?'):
        showerror("Oof", "...")
    else:
        showerror("Annulé", "Vous avez annulé votre demande.")

btn = Button(fenetre, text="Fermer", command=callback)
btn.pack()

fenetre.mainloop()
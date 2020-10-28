from tkinter import *

fenetre = Tk()

btn = Button(fenetre, text="Fermer", command=fenetre.quit)
btn.pack()

fenetre.mainloop()
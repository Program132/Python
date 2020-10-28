from tkinter import *

fenetre = Tk()

L1 = Label(fenetre, text="User Name")
L1.pack(side = LEFT)
E1 = Entry(fenetre, bd =5)
E1.pack(side = RIGHT)

fenetre.mainloop()
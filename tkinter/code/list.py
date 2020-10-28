from tkinter import *

fenetre = Tk()

liste = Listbox(fenetre)
liste.insert(1, "Python")
liste.insert(2, "PHP")
liste.insert(3, "jQuery")
liste.insert(4, "CSS")
liste.insert(5, "Javascript")
liste.insert(6, "C++")
liste.insert(7, "C#")
liste.insert(8, "C")
liste.insert(9, "Lua")


liste.pack()

fenetre.mainloop()
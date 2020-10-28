from tkinter import *

fenetre = Tk()

canvas = Canvas(fenetre, width=150, height=120, background='yellow')
ligne1 = canvas.create_line(75, 0, 75, 120)
ligne2 = canvas.create_line(0, 60, 150, 60)
txt = canvas.create_text(75, 60, text="Cible", font="Arial 16 italic", fill="blue")
##create_arc()        :  arc de cercle
##create_bitmap()     :  bitmap
##create_image()      :  image
##create_line()       :  ligne
##create_oval()       :  ovale
##create_polygon()    :  polygone
##create_rectangle()  :  rectangle 
##create_text()       :  texte
##create_window()     :  fenetre
canvas.pack()

fenetre.mainloop()
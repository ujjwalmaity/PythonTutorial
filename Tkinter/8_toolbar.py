from tkinter import *

root = Tk()

toolbar = Frame(root, bg='Pink')
toolbar.pack(side=TOP, fill=X)

button_1 = Button(toolbar, text='Insert Files')
button_2 = Button(toolbar, text='Print')
button_1.pack(side=LEFT, padx=2, pady=3)
button_2.pack(side=LEFT, padx=2, pady=3)

root.mainloop()

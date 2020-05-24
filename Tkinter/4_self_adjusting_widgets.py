from tkinter import *

root = Tk()

label_1 = Label(root, text='First', bg='Red', fg='White')
label_2 = Label(root, text='Second', bg='Blue', fg='White')

label_1.pack(fill=X)
label_2.pack(side=LEFT, fill=Y)

root.mainloop()

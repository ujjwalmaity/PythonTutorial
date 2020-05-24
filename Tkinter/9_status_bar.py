from tkinter import *

root = Tk()

status = Label(root, text='This is status', bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

root.mainloop()

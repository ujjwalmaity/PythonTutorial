from tkinter import *

root = Tk()


def do_something():
    print('Button clicked.')


button_1 = Button(root, text='Click Here', command=do_something)
button_1.pack()

root.mainloop()

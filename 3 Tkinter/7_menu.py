from tkinter import *


def func():
    print('Menu clicked.')


root = Tk()

myMenu = Menu(root)
root.config(menu=myMenu)

# Menu 1
subMenu = Menu(myMenu)

myMenu.add_cascade(label='File', menu=subMenu)

subMenu.add_command(label='Project', command=func)
subMenu.add_command(label='Save', command=func)
subMenu.add_separator()
subMenu.add_command(label='Exit', command=func)

# Menu 2
subMenu2 = Menu(myMenu)
myMenu.add_cascade(label='Edit', menu=subMenu2)
subMenu2.add_command(label='Undo', command=func)

root.mainloop()

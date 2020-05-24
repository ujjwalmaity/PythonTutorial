from tkinter import *

root = Tk()

canvas = Canvas(root)
canvas.pack()

line_1 = canvas.create_line(0, 0, 50, 100)
line_2 = canvas.create_line(10, 10, 100, 100, fill='Green')

root.mainloop()

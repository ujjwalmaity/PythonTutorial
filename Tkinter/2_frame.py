from tkinter import *

root = Tk()

frame_1 = Frame(root)
frame_1.pack()

frame_2 = Frame(root)
frame_2.pack(side=BOTTOM)

button_1 = Button(frame_1, text='Click Here', fg='Red')
button_2 = Button(frame_2, text='Click Here', fg='Blue')
button_1.pack()
button_2.pack()

root.mainloop()

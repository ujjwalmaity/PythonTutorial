from tkinter import *


class MyButton:
    def __init__(self, __root):
        frame = Frame(__root)
        frame.pack()

        self.printButton = Button(frame, text='Click Here', command=self.print_message)
        self.exitButton = Button(frame, text='Exit', command=frame.quit)

        self.printButton.pack()
        self.exitButton.pack()

    def print_message(self):
        print('Button clicked.')


root = Tk()
MyButton(root)

root.mainloop()

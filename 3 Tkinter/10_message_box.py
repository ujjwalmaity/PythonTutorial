from tkinter import *
import tkinter.messagebox as message_box

root = Tk()

message_box.showinfo('Title', 'This is awesome')

response = message_box.askquestion('Question 1', 'Do you like coffee?')
if response == 'yes':
    print('Here is a coffee for you.')

root.mainloop()

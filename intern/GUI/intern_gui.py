from tkinter import *
from tkinter import messagebox

WIDTH = 1280
HEIGHT = 720

# Base
root = Tk()
# Canvas
canvas = Canvas(root, width=WIDTH, height=HEIGHT, relief='raised', bg='grey')
canvas.pack()

top_frame = Frame(root, bg='green')
top_frame.place(relwidth=1, relheight=0.1, relx=0, rely=0)

left_frame = Frame(root, bg='brown')
left_frame.place(relwidth=0.2, relheight=0.9, relx=0, rely=0.1)


root.title('Intern System - Plots & Stats')
root.geometry('{}x{}'.format(WIDTH,HEIGHT))
root.mainloop()
from tkinter import *
from tkinter import messagebox

WIDTH = 1280
HEIGHT = 720

PLOTS_LABELS = ['Activity', 'Countries', 'Knowledge', 'Learning', 'Ratings', 'Sessions', 'Tags', 'Users']

TOP_FRAME_COLOR = '#00aaff'
TOP_FRAME_FONT = ("Helvetica", "36")
LEFT_FRAME_COLOR = '#66ccff'
LEFT_FRAME_FONT = ("Helvetica", "26")
RIGHT_FRAME_COLOR = '#e6f7ff'

# Base
root = Tk()
root.title('Intern System - Plots & Stats')
root.geometry('{}x{}'.format(WIDTH,HEIGHT))

# Canvas
canvas = Canvas(root, width=WIDTH, height=HEIGHT, relief='raised')
canvas.pack()

# Frames
top_frame = Frame(root, bg=TOP_FRAME_COLOR)
top_frame.place(relwidth=1, relheight=0.1, relx=0, rely=0)

left_frame = Frame(root, bg=LEFT_FRAME_COLOR)
left_frame.place(relwidth=0.2, relheight=0.9, relx=0, rely=0.1)

right_frame = Frame(root, bg=RIGHT_FRAME_COLOR)
right_frame.place(relwidth=0.8, relheight=0.9, relx=0.2, rely=0.1)

# Top Frame
top_frame_label = Label(top_frame, text='Intern System - Plots & Stats', bg=TOP_FRAME_COLOR, font=TOP_FRAME_FONT)
top_frame_label.pack(expand=True, fill='both')

# Right Frame
image_label = Label(right_frame)
image_label.pack()

def showImage(label):
    image = PhotoImage(file='Figure_{}.png'.format(label))
    image_label.configure(image=image)
    image_label.image = image

# Left Frame
label = Label(left_frame, text='Plots & stats', bg=LEFT_FRAME_COLOR, font=LEFT_FRAME_FONT)
label.grid(row=0, column=0)

counter = 1
for temp_label in PLOTS_LABELS:
    button = Button(left_frame, text=temp_label, bg=LEFT_FRAME_COLOR, relief='flat', underline=0, command=lambda label=temp_label: showImage(label))
    button.grid(row=counter, column=0)
    counter += 1

# Start GUI
root.mainloop()
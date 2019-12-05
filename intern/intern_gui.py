from tkinter import *
from datetime import datetime
from stats import generate_plots as gd

WIDTH = 1536
HEIGHT = 864

PLOTS_LABELS = ['Activity', 'Countries', 'Knowledge',
                'Learning', 'Ratings', 'Sessions', 'Tags', 'Users']

TOP_FRAME_COLOR = '#00aaff'
TOP_FRAME_FONT = ("Helvetica", "36")
LEFT_FRAME_COLOR = '#66ccff'
LEFT_FRAME_FONT = ("Helvetica", "26")
RIGHT_FRAME_COLOR = '#e6f7ff'

# Base
root = Tk()
root.title('Intern System - Plots & Stats')
root.geometry('{}x{}'.format(WIDTH, HEIGHT))

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
top_frame_label = Label(top_frame, text='Intern System - Plots & Stats',
                        bg=TOP_FRAME_COLOR, font=TOP_FRAME_FONT)
top_frame_label.pack(expand=True, fill='both')

# Right Frame
upper_frame = Frame(right_frame, bg=RIGHT_FRAME_COLOR)
upper_frame.place(relwidth=1, relheight=0.1, relx=0, rely=0)

lower_frame = Frame(right_frame, bg=RIGHT_FRAME_COLOR)
lower_frame.place(relwidth=1, relheight=0.9, relx=0, rely=0.1)

year_input_data = StringVar(root)
year_input_data.set(datetime.now().year)
year_input_options = ['2017', '2018', '2019']
year_input = OptionMenu(upper_frame, year_input_data, *year_input_options)
year_input.grid(row=0, column=0, padx=10, pady=40)

month_input_data = StringVar(root)
month_input_data.set(datetime.now().month)
month_input_options = ['01', '02', '03', '04',
                       '05', '06', '07', '08', '09', '10', '11', '12']
month_input = OptionMenu(upper_frame, month_input_data, *month_input_options)
month_input.grid(row=0, column=1, padx=10, pady=40)

def generate_plots():
    year = int(year_input_data.get())
    month = int(month_input_data.get())
    gd(year, month)

generate_plots_button = Button(upper_frame, text='Generate new Plots', bg=RIGHT_FRAME_COLOR, relief='flat', underline=0, command=lambda : generate_plots())
generate_plots_button.grid(row=0, column=2, padx=10, pady=40)


image_label = Label(lower_frame)
image_label.pack(expand=True)


def showImage(label):
    image = PhotoImage(file='Figure_{}.png'.format(label))
    image_label.configure(image=image)
    image_label.image = image


# Left Frame
label = Label(left_frame, text='Plots & Stats',
              bg=LEFT_FRAME_COLOR, font=LEFT_FRAME_FONT, anchor="center")
label.grid(row=0, column=0)

counter = 1
for temp_label in PLOTS_LABELS:
    button = Button(left_frame, text=temp_label, bg=LEFT_FRAME_COLOR, relief='flat',
                    underline=0, command=lambda label=temp_label: showImage(label))
    button.grid(row=counter, column=0)
    counter += 1

# Keybinds
root.bind('<a>', lambda event: showImage(PLOTS_LABELS[0]))
root.bind('<c>', lambda event: showImage(PLOTS_LABELS[1]))
root.bind('<k>', lambda event: showImage(PLOTS_LABELS[2]))
root.bind('<l>', lambda event: showImage(PLOTS_LABELS[3]))
root.bind('<r>', lambda event: showImage(PLOTS_LABELS[4]))
root.bind('<s>', lambda event: showImage(PLOTS_LABELS[5]))
root.bind('<t>', lambda event: showImage(PLOTS_LABELS[6]))
root.bind('<u>', lambda event: showImage(PLOTS_LABELS[7]))

root.bind('<g>', lambda event: generate_plots())

# Start GUI
# print('Image size: {}x{}'.format(WIDTH * 0.8, HEIGHT * 0.8))
root.mainloop()

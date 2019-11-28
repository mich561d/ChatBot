# Purpose of this file is to get all functions to work. Will be moved to demo.py once its done. There the proper architecture will be done.
from tkinter import *
from tkinter import messagebox
from random import randint as r

string_to_display = []

def show_message(self):
    # Handling user input
    user_message = input_field.get()
    show_user_message = 'You: {}'.format(user_message)
    string_to_display.append(show_user_message)

    # Handling bot message
    bot_message = input_field.get()
    show_bot_message = 'CVBot: {}'.format(bot_message)
    string_to_display.append(show_bot_message)

    # Showing messages
    text_area = Text(root, height=33, width=41)
    text_area.tag_config('bot', foreground='red')
    text_area.tag_config('user', foreground='blue')

    tag = ''
    for msg in string_to_display:
        if msg.startswith('CVBot', 0, 4):
            tag = 'bot'
        else:
            tag = 'user'

    text_area.insert(END, '\n'.join(string_to_display), tag)

    # Resets the entry widget to be ready for a new message.
    input_field.delete(0, END)

    text_area.grid(row=3, column=3)
    label = Label(root, fg='green')
    label.grid(row=0, column=0)


def on_close():
    result = messagebox.askyesno('Rating', 'Were you happy with the conversation?')
    rating = 0
    if result == True:
        rating = r(3,5)
    else:
        rating = r(1,3)
    # Uncomment for no bad reviews :D
    # if result == True:
    #     root.destroy()
    print(rating)
    root.destroy()

root = Tk()

input_field = Entry(root, width='45')
button = Button(root, text='Send', command=show_message, width='5')

# Binds the enter key to the button.
root.bind('<Return>', show_message)

# input_field.grid(row=1, column=2)
# button.grid(row=2, column=2)
button.place(x=292, y=570)
input_field.place(x=5, y=575)

root.geometry('345x600')
root.protocol('WM_DELETE_WINDOW', on_close)
root.mainloop()
from tkinter import *
from tkinter import simpledialog
#import client_chatBot as client

string_to_display = []


def show_message(self):
    # Handling user input
    user_message = input_field.get()
    show_user_message = 'You: {}'.format(user_message)
    string_to_display.append(show_user_message)
    #client.add_question(user_message)

    # Handling bot message
    bot_message = input_field.get()
    show_bot_message = 'CVBot: {}'.format(bot_message)
    string_to_display.append(show_bot_message)

    # Showing messages
    text_area = Text(root, height=33, width=41)
    text_area.insert(END, '\n\n'.join(string_to_display))

    # Resets the entry widget to be ready for a new message.
    input_field.delete(0, END)

    text_area.grid(row=3, column=3)
    label = Label(root, fg='green')
    label.grid(row=0, column=0)


def on_close(self):
    result = simpledialog.askinteger(
        "Rating",
        "How happy were you with the conversation? (Scale: Bad 1-5 Great)",
        minvalue=1,
        maxvalue=5
    )
    if result != None:
        #client.add_question('Rating: {}'.format(result))
        #client.status = 0
        root.destroy()


#client.setup()

root = Tk()

input_field = Entry(root, width='45')
button = Button(root, text='Send', command=show_message, width='5')

# Binds the enter key to the button.
root.bind('<Return>', show_message)

button.place(x=292, y=570)
input_field.place(x=5, y=575)

root.geometry('345x600')
root.protocol('WM_DELETE_WINDOW', on_close)
root.mainloop()

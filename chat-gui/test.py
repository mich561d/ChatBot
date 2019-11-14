from tkinter import *

string_to_display = []

def show_message():
    # Handling user input
    user_message = input_field.get()
    show_user_message = "You: {}".format(user_message)
    string_to_display.append(show_user_message)

    # Handling bot message
    bot_message = input_field.get()
    show_bot_message = "CVBot: {}".format(bot_message)
    string_to_display.append(show_bot_message)

    # Showing messages
    text_area = Text(root, height=20, width=40)
    text_area.tag_config('bot', foreground='red')
    text_area.tag_config('user', foreground='blue')

    tag = ''
    for msg in string_to_display:
        if msg.startswith('CVBot', 0, 5):
            tag = 'bot'
        else:
            tag = 'user'


    text_area.insert(END, "\n".join(string_to_display), tag)

    text_area.grid(row=3, column=3)
    # label = Label(root, fg='green')
    # label["text"] = string_to_display
    # label.grid(row=3, column=3)

root = Tk()

input_field = Entry(root, height=20, width=40)
button = Button(root, text="Send", command=show_message)

#input_field.grid(row=1, column=2)
#button.grid(row=2, column=2)

input_field.place(x=2, y=20)
button.place(x=30, y=30)

root.geometry("1000x600")
root.mainloop()
from tkinter import *

#TODO: Get this to work.. 

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def show_message(self):
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
            if msg.startswith('CVBot', 0, 4):
                tag = 'bot'
            else:
                tag = 'user'

        text_area.insert(END, "\n".join(string_to_display), tag)

        text_area.grid(row=3, column=3)
        label = Label(root, fg='green')
        label.grid(row=1, column=1)

    # Creation of init_window
    def init_window(self):

            # changing the title of our master widget
        self.master.title("Chatbot")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a button instance
        sendButton = Button(self, text="Send", command=self.show_message)
        sendButton.grid(row=0, column=1)


root = Tk()

string_to_display = []
input_field = Entry(root)
input_field.grid(row=0, column=0)
# size of the window
root.geometry("1000x600")


app = Window(root)
root.mainloop()

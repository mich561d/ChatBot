from tkinter import *

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def show_message(self):
        user_message = inputField.get()
        string_to_display = "You: {}".format(user_message)
        label = Label(self)
        label["text"] = string_to_display
        label.grid(row=1, column=1)

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget      
        self.master.title("Chatbot")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a button instance
        sendButton = Button(self, text="Send", command=self.show_message)

        inputField.grid(row=0, column=0)
        sendButton.grid(row=0, column=1)

root = Tk()

inputField = Entry(root)

#size of the window
root.geometry("1000x600")


app = Window(root) 
root.mainloop()

from tkinter import *

def show_message():
    user_message = input_field.get()
    string_to_display = "You: {}".format(user_message)
    label = Label(root)
    label["text"] = string_to_display
    label.grid(row=2, column=2)

root = Tk()

input_field = Entry(root)
button = Button(root, text="Send", command=show_message)

input_field.grid(row=1, column=0)
button.grid(row=1, column=1)


root.geometry("1000x600")
root.mainloop()
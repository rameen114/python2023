from tkinter import *

top = Tk()
top.geometry("400x200")
top.configure(background="gray")

user_name = Label(top, text="Name").place(x=40, y=60)
user_password = Label(top, text="Password").place(x=40, y=100)
submit_button = Button(top, text="Submit").place(x=40, y=140)

user_name_input_area = Entry(top).place(x=120 ,y=60)
user_password_input_area = Entry(top).place(x=120, y=100)

top.mainloop()
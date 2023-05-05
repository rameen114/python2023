from tkinter import *
from tkinter.ttk import *

from time import strftime

window = Tk()
window .title("My first TKinter windows")

def showTime():
    string = strftime('%H:%M:%S: %p')
    clock.config(text=string)
    clock.after(1000, showTime)

clock = Label(window, font=("ds-digital", 200), background="white", foreground="green")
clock.pack()

showTime()
mainloop()
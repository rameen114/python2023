import requests
import tkinter as tk
from tkinter import Text, END
from tkinter.ttk import Button

root = tk.Tk()
root.title('Elders speech') # pip3 install requests

def get_qoute():
    r       = requests.get('https://api.quotable.io/random')
    data    = r.json()
    qoute   = data['content']
    author  = data['author']

    qa      = qoute + author

    text_box.delete(1.0, END)
    text_box.insert(END, qa)


text_box    = Text(root, width=50, height=10)
get_button  = Button(root, text="Get New Qoute", command=get_qoute)

text_box.pack()
get_button.pack()

root.mainloop()
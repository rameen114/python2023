from tkinter import *

root = Tk()
root.geometry('400x500')

datas = []

def add():
    global datas
    datas.append([Name.get(), Number.get(), Address.get(1.0, "end-1c")])
    update_book()

def view():
    Name.set(datas[int(select.curselection()[0])][0])
    Number.set(datas[int(select.curselection()[0])][1])
    Address.delete(1.0,"end")
    Address.insert(1.0, datas[int(select.curselection()[0])][2])

def delete():
    del datas[int(select.curselection()[0])]
    update_book()

def reset():
    Name.set('')
    Number.set('')
    Address.delete(1.0, "end")

def update_book():
    select.delete(0, END)
    for n,p,a in datas:
        select.insert(END, n)

Name    = StringVar()
Number  = StringVar()

frame = Frame()
frame.pack(pady=10)

frame1 = Frame()
frame1.pack()

frame2  = Frame()
frame2.pack(pady=10)

Label(frame, text='Name').pack(side=LEFT)
Entry(frame, textvariable=Name, width=50).pack()

Label(frame1, text='Number').pack(side=LEFT)
Entry(frame1, textvariable=Number, width=50).pack()

Label(frame2, text='Address').pack(side=LEFT)
Address = Text(frame2, width=40, height=10)
Address.pack()

Button(root, text='Add', command=add).place(x=100, y=270)
Button(root, text='View', command=view).place(x=100, y=310)
Button(root, text='Delete', command=delete).place(x=100, y=350)
Button(root, text='Reset', command=reset).place(x=100, y=390)

select = Listbox(root, height=12)
select.place(x=200, y=260)
select.pack()

root.mainloop()
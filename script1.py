from tkinter import *

window=Tk()

def print_entry():
    print(e1_value.get())
    t1.insert(END,e1_value.get())

b1=Button(window, text="Execute", command=print_entry)
b1.grid(row=0,column=0)

e1_value=StringVar()
e1=Entry(window, textvariable=e1_value)
e1.grid(row=0,column=1)

t1=Text(window, heigh=25, width=25)
t1.grid(row=0,column=2)

window.mainloop()

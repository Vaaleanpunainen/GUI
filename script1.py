from tkinter import *

window=Tk()

def km_to_miles():
    miles=float(e1_value.get())*1.609
    t1.insert(END, miles)

b1=Button(window, text="Execute", command=km_to_miles)
b1.grid(row=0,column=0)

e1_value=StringVar()
e1=Entry(window, textvariable=e1_value)
e1.grid(row=0,column=1)

t1=Text(window, heigh=25, width=25)
t1.grid(row=0,column=2)

window.mainloop()

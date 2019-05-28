from tkinter import *

window=Tk()

b1=Button(window, text="Button")
b1.grid(row=0,column=0)

e1=Entry(window)
e1.grid(row=0,column=1)

t1=Text(window, heigh=1, width=25)
t1.grid(row=0,column=2)

window.mainloop()

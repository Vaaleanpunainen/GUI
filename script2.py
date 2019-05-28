from tkinter import *

window=Tk()

def convert_kg():
    grams=(float(e1_value.get())*1000, "grams")
    t1.insert(END, grams)
    pounds=(float(e1_value.get())*2.20462, "pounds")
    t2.insert(END, pounds)
    ounces=(float(e1_value.get())*35.274, "ounces")
    t3.insert(END, ounces)

l1=Label(text="Enter value (kg):", fg="black")
l1.grid(row=0,column=0)

b1=Button(window, text="Convert", command=convert_kg)
b1.grid(row=0,column=2)

e1_value=StringVar()
e1=Entry(window, textvariable=e1_value)
e1.grid(row=0,column=1)


t1=Text(window, heigh=1, width=25)
t1.grid(row=1,column=0)

t2=Text(window, heigh=1, width=25)
t2.grid(row=1,column=1)

t3=Text(window, heigh=1, width=25)
t3.grid(row=1,column=2)

window.mainloop()

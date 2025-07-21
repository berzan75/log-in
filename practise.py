from tkinter import *

top=Tk()
top.geometry("300x300")

hello=Label(top,
            text="hello").place(x= 100,
                                y=130)
world=Label(top,
            text="world").place(x=100,
                                y=150)
top.mainloop()
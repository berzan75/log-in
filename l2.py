from tkinter import *

top=Tk()
top.title("loged in")
top.geometry("600x450")
top.config(background="red")

user_name = Label(top,
                text="User_name").place(x=40,
                                        y=100)
user_password= Label(top,
                     text="Password").place(x=40,
                                            y=140)
user_entry= Entry(top,
                  width=40).place(x=120,
                                  y=100)

password= Entry(top,
                width=40).place(x=120,
                                y=140)
submit=Button(top,
              text="submit").place(x=40,
                                   y=200)
top.mainloop()
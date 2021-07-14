from tkinter import *
import os
from PIL import ImageTk, Image

root = Tk()
root.title("Login")
root.iconbitmap("photo/login.ico")
root.geometry("500x600+450+100")
root.minsize(500, 600)
root.maxsize(500, 600)

photo = ImageTk.PhotoImage(file="photo/login.png")
mycanvas = Canvas(root, width=800, height=500)
mycanvas.pack(fill="both", expand=True)
mycanvas.create_image(0, 0, image=photo, anchor="nw")


def resizer(e):
    global bg, resized_bg, new_bg
    # open image
    bg = Image.open("photo/login.png")
    # resize image
    resized_bg = bg.resize((e.width, e.height), Image.ANTIALIAS)
    # define Image again
    new_bg = ImageTk.PhotoImage(resized_bg)
    mycanvas.create_image(0, 0, image=new_bg, anchor="nw")
    mycanvas.create_text(250, 90, text="Login", font=("Helvetica", 35), fill="white")


root.bind('<Configure>', resizer)

photologin = PhotoImage(file="photo/Login_.png")
labellogin = Label(root, image=photologin, bg="#074e72")
labellogin.place(x=220, y=140)

user = PhotoImage(file="photo/user_.png")
labellogi = Label(root, image=user, bg="#085b7f")
labellogi.place(x=105, y=237)

username = Entry(root, width=18)
username.config(font=("Courier", 16))
username.insert(0, "UserName")
username.place(x=150, y=240)

password = PhotoImage(file="photo/passw.png")
userpass = Label(root, image=password, bg="#085276")
userpass.place(x=105, y=297)


def showpass():
    if var.get() == 1:
        userpassw.config(show='')
    if var.get() == 0:
        userpassw.config(show='*')


userpassw = Entry(root, width=18, show='*')
userpassw.config(font=("Courier", 16))
userpassw.insert(0, "Password")
userpassw.place(x=150, y=300)

var = IntVar()
var.set('0')
c = Checkbutton(root, text="show password", variable=var, onvalue=1, offvalue=0,
                command=showpass, bg="#07496f", fg="white")
c.config(font=("Courier", 13))
c.place(x=150, y=340)

name = "admin"
passwod = "admin"


def login():
    if username.get() == name and userpassw.get() == passwod:
        root.destroy()
        os.popen('python Shop_GUI.py').readlines()
    else:
        mycanvas.create_text(350, 500, text="Incorrect Password\nTry again!",
                             font=("Helvetica", 20), fill="red")


logbutton = Button(root, text="Login", command=login)
logbutton.config(font=("Courier", 15))
logbutton.place(x=220, y=400)

root.mainloop()

import tkinter
import os
from tkinter import *
import sqlite3
import tkinter.messagebox


root=None
userbox=None
passbox=None
topframe=None
bottomframe=None
frame3=None
login=None

def GET():
    global userbox,passbox,error
    S1=userbox.get()
    S2=passbox.get()
    if(S1=='Shrine' and S2=='hospital'):
        os.system('py menu.py')
    else:
        error=tkinter.Label(bottomframe,text="Wrong Id / Password \n TRY AGAIN",fg="red",font="bold")
        error.pack()


def Entry():
    global userbox,passbox,login,topframe,bottomframe,image_1
    root = tkinter.Tk()

    root.geometry("280x250")
    topframe = tkinter.Frame(root)
    topframe.pack()
    bottomframe=tkinter.Frame(root)
    bottomframe.pack()
    heading = tkinter.Label(topframe, text="HOSPITAL MANAGEMENT",bg='white',fg='steelblue',font='Times 16 bold italic')
    username=tkinter.Label(topframe,text="USERNAME",fg="steelblue")
    userbox = tkinter.Entry(topframe)
    password=tkinter.Label(bottomframe,text="PASSWORD",fg='steelblue')
    passbox = tkinter.Entry(bottomframe,show="*")
    login = tkinter.Button(bottomframe, text="LOGIN", command=GET,font="arial 8 bold",fg='steelblue')
    heading.pack()
    username.pack()
    userbox.pack()
    password.pack()
    passbox.pack()
    login.pack()
    root.title("DATABASE LOGIN")
    root.mainloop()

Entry()

import os
import sqlite3
import tkinter.messagebox
from tkinter import *


conn=sqlite3.connect("Hospital.db")
print("DATABASE CONNECTION SUCCESSFUL")


def ap():
    os.system('py appointment.py')

def pa():
    os.system('py patient.py')

def do():
    os.system('py doctor.py')

def sp():
    os.system('py specialization.py')


def menu():
    global root1,button1,button2,button3,button4,button5,m,button6
    root1=Tk()


    root1.geometry("350x500")
    root1.title("MAIN MENU")
    m=tkinter.Label(root1,text="MENU",font='Times 16 bold italic',fg='blue4')
    button1=Button(root1,text="1.PATIENT LOG",width=20,height=2,fg='blue4',bg='SkyBlue1',font=('Verdana',15),command=pa)
    button2 = Button(root1, text="2.DOCTOR LOG",width=20,height=2,fg='blue4',bg='SkyBlue1',font=('Verdana',15),command=do)
    button3 = Button(root1, text="3.APPOINTMNET LOG",width=20,height=2,fg='blue4',bg='SkyBlue1',font=('Verdana',15),command=ap)
    button4 = Button(root1, text="4.SPECIALIZATION LOG",width=20,height=2,fg='blue4',bg='SkyBlue1',font=('Verdana',15),command=sp)

    m.place(x=75,y=5)

    button1.pack(side=tkinter.TOP)
    button1.place(x=50,y=50)
    button2.pack(side=tkinter.TOP)
    button2.place(x=50,y=150)
    button3.pack(side=tkinter.TOP)
    button3.place(x=50,y=250)
    button4.pack(side=tkinter.TOP)
    button4.place(x=50, y=350)
    root1.mainloop()





menu()

from tkinter import *
import sqlite3
import tkinter.messagebox
import mysql.connector
from mysql.connector import Error
import PIL.Image
import PIL.ImageTk


conn = mysql.connector.connect(host='localhost',
                                            database='hospital' ,
                                            user='root',
                                            password='root')
cursor = conn.cursor()

class Application:
 def __init__(self,master):
    self.master=master

    #creating frames in the master
    self.up=Frame(master,width=800,height=600,bg='RoyalBlue2')
    self.up.pack(side=TOP)

    im = PIL.Image.open("hp14.jpg")
    photo = PIL.ImageTk.PhotoImage(im)

    label = Label(self.up, image=photo)
    label.image = photo  # keep a reference!
    label.pack()


    self.heading=Label(self.up,text="SPECIALIZATION REGISTRATION",font="Helvetica 30 italic",fg='blue4',bg='SkyBlue1')
    self.heading.place(x=30,y=10)

    self.Sc=Label(self.up,text="Specialization code",font='arial 30 italic',fg='blue4',bg='SkyBlue1')
    self.Sc.place(x=15, y=150)
    self.Sname=Label(self.up,text="Specialization name",font='arial 30 italic',fg='blue4',bg='SkyBlue1')
    self.Sname.place(x=15, y=250)

    self.Spec_code_ent = Entry(self.up, width=20, font=('Verdana', 25))
    self.Spec_code_ent.place(x=380, y=155)
    self.Sname_ent = Entry(self.up, width=20, font=('Verdana', 25))
    self.Sname_ent.place(x=380, y=255)

    self.add=Button(self.up,text="Add Specialization",width=20,height=2,fg='blue4',bg='SkyBlue1',font=('Verdana',15),command=self.add_spec)
    self.add.place(x=150,y=380)
    self.dele=Button(self.up,text="Remove specialization",width=20,height=2,fg='blue4',bg='SkyBlue1',font=('Verdana',15),command=self.dele)
    self.dele.place(x=450,y=380)

 def add_spec(self):
    self.val1=self.Spec_code_ent.get()
    self.val2=self.Sname_ent.get()

    if self.val1=='' or self.val2=='':
        tkinter.messagebox.showinfo("Warning","Please Fill all the boxes")

    else:
        values=(str(self.val1),str(self.val2))
        cursor.execute('INSERT INTO doc_specialization(spec_code,spec_desc)VALUES(%s,%s);',values)
        conn.commit()
        tkinter.messagebox.showinfo("Success","Specialization "+str(self.val2)+" has been created")
 def remove(self):
    id=str(e7.get())

    cursor.execute("select * from doc_specialization where spec_code = %s",(id,))
    v=cursor.fetchall()

    if (len(v)==0):
        tkinter.messagebox.showinfo("Warning","No such Specialization")
    else:
        cursor.execute('DELETE FROM doc_specialization where spec_code = %s',(id,))
        conn.commit()
        tkinter.messagebox.showinfo("Success","Specialization has been deleted")



 def dele(self):
    self.d=Toplevel(root,bg="steelblue")
    global e7


    self.id=Label(self.d,text="Enter specialization code to delete",font='arial 30 italic',fg='blue4',bg='SkyBlue1')
    self.id.place(x=30, y=150)
    self.d.geometry("1100x400+0+0")
    e7 =Entry(self.d,width=20,font=('Verdana',25))
    e7.place(x=650, y=155)
    self.dbutton=Button(self.d,text="Delete",width=20,height=2,fg='blue4',bg='SkyBlue1',font=('Verdana',15),command=self.remove)
    self.dbutton.place(x=450, y=250)


root =Tk()
b=Application(root)

#resolution of the window

root.geometry("828x466+0+0")

#preventing the resize feature
root.resizable(False,False)
root.mainloop()

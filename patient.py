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
        self.up=Frame(master,width=1280,height=880,bg='pink')
        self.up.pack(side=TOP)

        im = PIL.Image.open("hp10.png")
        photo = PIL.ImageTk.PhotoImage(im)

        label = Label(self.up, image=photo)
        label.image = photo  # keep a reference!
        label.pack()



        self.heading=Label(self.up,text="HOSPITAL-PATIENT REGISTRATION",font="Helvetica 40 italic",fg='blue4',bg='DeepSkyBlue1')
        self.heading.place(x=30,y=10)
        self.Pid=Label(self.up,text="Patient ID",font='arial 30 italic',fg='blue4',bg='DeepSkyBlue1')
        self.Pid.place(x=30, y=150)
        self.Pname=Label(self.up,text="Patient name",font='arial 30 italic',fg='blue4',bg='DeepSkyBlue1')
        self.Pname.place(x=30, y=250)

        self.Gender = Label(self.up, text="Gender", font='arial 30 italic',fg='blue4',bg='DeepSkyBlue1')
        self.Gender.place(x=30, y=350)
        self.Age = Label(self.up, text="Age", font='arial 30 italic', fg='blue4',bg='DeepSkyBlue1')
        self.Age.place(x=30, y=450)
        self.Phone = Label(self.up, text="Phone numer", font='arial 30 italic', fg='blue4',bg='DeepSkyBlue1')
        self.Phone.place(x=30, y=550)
        self.Address = Label(self.up, text="Address", font='arial 30 italic', fg='blue4',bg='DeepSkyBlue1')
        self.Address.place(x=30, y=650)

        #creating entry boxes
        self.Pid_ent = Entry(self.up, width=20, font=('Verdana', 25))
        self.Pid_ent.place(x=460, y=155)
        self.Pname_ent = Entry(self.up, width=20, font=('Verdana', 25))
        self.Pname_ent.place(x=460, y=255)
        self.Gender_ent = Entry(self.up, width=20, font=('Verdana', 25))
        self.Gender_ent.place(x=460, y=355)
        self.Age_ent = Entry(self.up, width=20, font=('Verdana', 25))
        self.Age_ent.place(x=460, y=455)
        self.Phone_ent = Entry(self.up, width=20, font=('Verdana', 25))
        self.Phone_ent.place(x=460, y=555)
        self.Address_ent = Entry(self.up, width=20, font=('Verdana', 25))
        self.Address_ent.place(x=460, y=655)




        #button to perfor a command
        self.add=Button(self.up,text="Add Patient",width=20,height=2,fg='blue4',bg='SkyBlue1',font=('Verdana',15),command=self.add_patient)
        self.add.place(x=160,y=750)

        self.dele=Button(self.up,text="Delete Patient",width=20,height=2,fg='blue4',bg='SkyBlue1',font=('Verdana',15),command=self.dele)

        self.dele.place(x=460,y=750)
        self.view=Button(self.up,text="View Patient",width=20,height=2,fg='blue4',bg='SkyBlue1',font=('Verdana',15),command=self.va)
        self.view.place(x=760,y=750)

     def add_patient(self):
        self.val1=self.Pid_ent.get()
        self.val2=self.Pname_ent.get()
        self.val3=self.Gender_ent.get()
        self.val4=self.Age_ent.get()
        self.val5=self.Phone_ent.get()
        self.val6=self.Address_ent.get()

        #checking if the user input is empty
        if self.val1=='' or self.val2=='' or self.val3==''or self.val4==''or self.val5==''or self.val6=='':
            tkinter.messagebox.showinfo("Warning","Please Fill all the boxes")
        else:
           values=(str(self.val1),str(self.val2),str(self.val3),str(self.val4),str(self.val5),str(self.val6))
           cursor.execute('INSERT INTO patient(patid,pname,gender,age,phone,address)VALUES(%s,%s,%s,%s,%s,%s)',values)

           #cursor.execute(sql,values)
           conn.commit()
           tkinter.messagebox.showinfo("Success","Patient Details for "+str(self.val2)+" has been added")

     def remove(self):
         id=str(e7.get())

         cursor.execute("select * from patient where patid = %s",(id,))
         v=cursor.fetchall()

         if (len(v)==0):
            tkinter.messagebox.showinfo("Warning","No such Patient")
         else:
            cursor.execute('DELETE FROM patient where patid = %s',(id,))
            conn.commit()
            tkinter.messagebox.showinfo("Success","Patient has been deleted")



     def dele(self):
        self.d=Toplevel(root,bg="steelblue")
        global e7


        self.id=Label(self.d,text="Enter Patient id to delete",font='arial 30 italic',fg='blue4',bg='DeepSkyBlue1')
        self.id.place(x=30, y=150)
        self.d.geometry("1080x400+0+0")
        e7 =Entry(self.d,width=20,font=('Verdana',25))
        e7.place(x=500, y=155)
        self.dbutton=Button(self.d,text="Delete",width=20,height=2,fg='blue4',bg='SkyBlue1',font=('Verdana',15),command=self.remove)
        self.dbutton.place(x=450, y=250)

     def viewappointment(self):
        global e8
        ap=str(e8.get())
        cursor.execute("select * from patient where patid=%s", (ap,))
        v=cursor.fetchall()
        if (len(v) == 0):
            errorD = Label(rootAP, text="NO SUCH PATIENT", fg="red")
            errorD.place(x=20, y=120)
        else:
            cursor.execute("Select patid,pname,gender,age,phone,address from patient where patid=%s",(ap,))
            s=cursor.fetchall()

            for i in s:
                l1=tkinter.Label(rootAP,text="PATIENT ID",fg='blue')
                dis1=tkinter.Label(rootAP,text=i[0])
                l2=tkinter.Label(rootAP,text="PATIENT NAME",fg='blue')
                dis2=tkinter.Label(rootAP,text=i[1])
                l3=tkinter.Label(rootAP,text="PATIENT SEX",fg='blue')
                dis3=tkinter.Label(rootAP,text=i[2])
                l4=tkinter.Label(rootAP,text="PATIENT AGE",fg='blue')
                dis4=tkinter.Label(rootAP,text=i[3])
                l5=tkinter.Label(rootAP,text="PATIENT PHONE NUMBER",fg='blue')
                dis5=tkinter.Label(rootAP,text=i[4])
                l6=tkinter.Label(rootAP,text="PATIENT ADDRESS",fg='blue')
                dis6=tkinter.Label(rootAP,text=i[5])

                l1.pack()
                dis1.pack()
                l2.pack()
                dis2.pack()
                l3.pack()
                dis3.pack()
                l4.pack()
                dis4.pack()
                l5.pack()
                dis5.pack()
                l6.pack()
                dis6.pack()

                conn.commit()


     def va(self):
        global rootAP,e8
        rootAP=tkinter.Tk()
        rootAP.geometry("500x550")
        rootAP.title("PATIENT LIST")
        h1=tkinter.Label(rootAP,text="ENTER PATIENT ID TO VIEW DETAILS")
        h1.place(x=20,y=20)
        e8=Entry(rootAP)
        e8.place(x=20,y=40)
        b5=Button(rootAP,text="SEARCH",command=self.viewappointment)
        b5.place(x=30,y=65)
        rootAP.mainloop()

#Creating the object
root =Tk()
b=Application(root)

#resolution of the window

root.geometry("1280x880+0+0")

#preventing the resize feature
root.resizable(False,False)
root.mainloop()

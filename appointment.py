from tkinter import *
import sqlite3
import tkinter.messagebox
import mysql.connector
from mysql.connector import Error
import PIL.Image
import PIL.ImageTk

try:
 conn = mysql.connector.connect(host='localhost',
                                         database='hospital',
                                         user='root',
                                         password='root')
 if conn.is_connected():
        db_Info = conn.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)


 class Application:
    def __init__(self,master):
        self.master=master

        #creating frames in the master
        self.up=Frame(master,width=1280,height=880,bg='pink')
        self.up.pack(side=TOP)

        im = PIL.Image.open("hp.png")
        photo = PIL.ImageTk.PhotoImage(im)

        label = Label(self.up, image=photo)
        label.image = photo  # keep a reference!
        label.pack()



        #Label for the window
        self.heading=Label(self.up,text="Hospital Appointments",font="Helvetica 40 italic",fg='blue4',bg='DeepSkyBlue1')
        self.heading.place(x=30,y=10)
        self.Pid=Label(self.up,text="Patient ID",font='arial 30 italic',fg='blue4',bg='DeepSkyBlue1')
        self.Pid.place(x=30, y=150)


        self.Did = Label(self.up, text="Doctor ID", font='arial 30 italic',fg='blue4',bg='DeepSkyBlue1')
        self.Did.place(x=30, y=250)
        self.At = Label(self.up, text="Appointment time(HH:MM:SS)", font='arial 30 italic', fg='blue4',bg='DeepSkyBlue1')
        self.At.place(x=30, y=350)
        self.Ad = Label(self.up, text="Appointment Date(YYYY-MM-DD)", font='arial 30 italic', fg='blue4',bg='DeepSkyBlue1')
        self.Ad.place(x=30, y=450)
        self.Descp = Label(self.up, text="Description", font='arial 30 italic', fg='blue4',bg='DeepSkyBlue1')
        self.Descp.place(x=30, y=550)

        #creating entry boxes
        self.PatID_ent = Entry(self.up, width=20, font=('Verdana', 25))
        self.PatID_ent.place(x=660, y=155)
        self.DocID_ent = Entry(self.up, width=20, font=('Verdana', 25))
        self.DocID_ent.place(x=660, y=255)
        self.AppT_ent = Entry(self.up, width=20, font=('Verdana', 25))
        self.AppT_ent.place(x=660, y=355)
        self.AppD_ent = Entry(self.up, width=20, font=('Verdana', 25))
        self.AppD_ent.place(x=660, y=455)
        self.Descp_ent = Entry(self.up, width=20, font=('Verdana', 25))
        self.Descp_ent.place(x=660, y=555)




        #button to perfor a command
        self.add=Button(self.up,text="Add Appointment",width=20,height=2,fg='blue4',bg='DeepSkyBlue1',font=('Verdana',15),command=self.add_appointment)
        self.add.place(x=160,y=750)

        self.dele=Button(self.up,text="Delete Appointment",width=20,height=2,fg='blue4',bg='DeepSkyBlue1',font=('Verdana',15),command=self.dele)

        self.dele.place(x=460,y=750)
        self.view=Button(self.up,text="View Appointment",width=20,height=2,fg='blue4',bg='DeepSkyBlue1',font=('Verdana',15),command=self.va)
        self.view.place(x=760,y=750)

    def add_appointment(self):
        self.val1=self.PatID_ent.get()
        self.val2=self.DocID_ent.get()
        self.val3=self.AppT_ent.get()
        self.val4=self.AppD_ent.get()
        self.val5=self.Descp_ent.get()

        #checking if the user input is empty
        if self.val1=='' or self.val2=='' or self.val3==''or self.val4==''or self.val5=='':
            tkinter.messagebox.showinfo("Warning","Please Fill all the boxes")
        else:
            values=(str(self.val1),str(self.val2),str(self.val3),str(self.val4),str(self.val5))
            cursor.execute('INSERT INTO appointment (patid,did,appt,appd,descp)VALUES(%s,%s,%s,%s,%s)',values)

            #(sql, values)
            conn.commit()
            tkinter.messagebox.showinfo("Success","Appointment for "+str(self.val1)+" has been created")

    def remove(self):
         id=str(e7.get())

         cursor.execute("select * from appointment where patid = %s",(id,))
         v=cursor.fetchall()

         if (len(v)==0):
            tkinter.messagebox.showinfo("Warning","No such Appointment")
         else:
            cursor.execute('DELETE FROM appointment where patid = %s',(id,))
            conn.commit()
            tkinter.messagebox.showinfo("Success","Appointment has been deleted")



    def dele(self):
        self.d=Toplevel(root,bg="steelblue")
        global e7
        self.id=Label(self.d,text="Enter Patient id to delete",font='arial 30 italic',fg='blue4',bg='DeepSkyBlue1')
        self.id.place(x=30, y=150)
        self.d.geometry("1080x400+0+0")
        e7 =Entry(self.d,width=20,font=('Verdana',25))
        e7.place(x=500, y=155)
        self.dbutton=Button(self.d,text="Delete",width=20,height=2,fg='blue4',bg='DeepSkyBlue1',font=('Verdana',15),command=self.remove)
        self.dbutton.place(x=450, y=250)


    def viewappointment(self):
        global e8,e9
        ap=str(e8.get())
        d=str(e9.get())
        cursor.execute("select * from appointment where patid=%s AND did=%s", (ap,d,))
        v=cursor.fetchall()
        if (len(v) == 0):
            errorD = Label(rootAP, text="NO APPOINTMENT FOR TODAY", fg="red")
            errorD.place(x=20, y=120)
        else:
            cursor.execute("Select patid,did,appt,appd,descp from appointment where patid=%s AND did=%s",(ap,d,))
            s=cursor.fetchall()
            s0=Label(rootAP,text="| Patient id | Doctor id | Appointment time | Appointment Date | Description |")
            for i in s:
                s1=Label(rootAP,text=i,fg='green',font='arial 20 italic')
                s1.place(x=10,y=140)


    def va(self):
        global rootAP,e8,e9
        rootAP=tkinter.Tk()
        rootAP.geometry("500x550")
        rootAP.title("TODAYS APPOINTMENTS")
        h1=tkinter.Label(rootAP,text="ENTER PATIENT ID TO VIEW APPOINTMENTS")
        h1.place(x=20,y=20)

        e8=Entry(rootAP)
        e8.place(x=20,y=40)
        h1=tkinter.Label(rootAP,text="ENTER DOCTOR ID TO VIEW APPOINTMENTS")
        h1.place(x=20,y=60)
        e9=Entry(rootAP)
        e9.place(x=20,y=80)
        b5=Button(rootAP,text="SEARCH",command=self.viewappointment)
        b5.place(x=30,y=105)
        rootAP.mainloop()

 #Creating the object
 root =Tk()
 b=Application(root)

 #resolution of the window

 root.geometry("1280x880+0+0")

 #preventing the resize feature
 root.resizable(False,False)

 root.mainloop()

except Error as e:
   print("Error while connecting to MySQL", e)

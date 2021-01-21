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

        self.up=Frame(master,width=1280,height=980)
        self.up.pack(side=TOP)

        im = PIL.Image.open("hp2.jpg")
        photo = PIL.ImageTk.PhotoImage(im)

        label = Label(self.up, image=photo)
        label.image = photo  # keep a reference!
        label.pack()







        #Label for the window
        self.heading=Label(self.up,text="DOCTOR REGISTRATION",font="Helvetica 40 italic",fg='blue4',bg='RoyalBlue2')
        self.heading.place(x=30,y=10)
        self.Did=Label(self.up,text="Doctor ID",font='arial 30 italic',fg='blue4',bg='RoyalBlue2')
        self.Did.place(x=30, y=150)
        self.Dname=Label(self.up,text="Doctor name",font='arial 30 italic',fg='blue4',bg='RoyalBlue2')
        self.Dname.place(x=30, y=250)
        self.Gender = Label(self.up, text="Gender", font='arial 30 italic',fg='blue4',bg='RoyalBlue2')
        self.Gender.place(x=30, y=350)
        self.Age = Label(self.up, text="Age", font='arial 30 italic', fg='blue4',bg='RoyalBlue2')
        self.Age.place(x=30, y=450)
        self.Spec_code = Label(self.up, text="Specialization Code", font='arial 30 italic', fg='blue4',bg='RoyalBlue2')
        self.Spec_code.place(x=30, y=550)
        self.Salary = Label(self.up, text="Salary", font='arial 30 italic', fg='blue4',bg='RoyalBlue2')
        self.Salary.place(x=30, y=650)
        self.Phone = Label(self.up, text="Phone", font='arial 30 italic', fg='blue4',bg='RoyalBlue2')
        self.Phone.place(x=30, y=750)

        #creating entry boxes
        self.Did_ent = Entry(self.up, width=20, font=('Verdana', 25))
        self.Did_ent.place(x=460, y=155)
        self.Dname_ent = Entry(self.up, width=20, font=('Verdana', 25))
        self.Dname_ent.place(x=460, y=255)
        self.Gender_ent = Entry(self.up, width=20, font=('Verdana', 25))
        self.Gender_ent.place(x=460, y=355)
        self.Age_ent = Entry(self.up, width=20, font=('Verdana', 25))
        self.Age_ent.place(x=460, y=455)
        self.Spec_ent = Entry(self.up, width=20, font=('Verdana', 25))
        self.Spec_ent.place(x=460, y=555)
        self.Salary_ent = Entry(self.up, width=20, font=('Verdana', 25))
        self.Salary_ent.place(x=460, y=655)
        self.Phone_ent = Entry(self.up, width=20, font=('Verdana', 25))
        self.Phone_ent.place(x=460, y=755)




        #button to perfor a command
        self.add=Button(self.up,text="Add Doctor",width=20,height=2,fg='blue4',bg='SkyBlue1',font=('Verdana',15),command=self.add_doctor)
        self.add.place(x=160,y=850)

        self.dele=Button(self.up,text="Delete Doctor",width=20,height=2,fg='blue4',bg='SkyBlue1',font=('Verdana',15),command=self.dele)
        self.dele.place(x=460,y=850)
        #self.view=Button(self.up,text="View Doctors",width=20,height=2,fg='blue4',bg='SkyBlue1',font=('Verdana',15),command=self.va)
        #self.view.place(x=460,y=850)
        self.view=Button(self.up,text="View Highest salary cardiologist",width=30,height=2,fg='blue4',bg='SkyBlue1',font=('Verdana',15),command=self.ha)
        self.view.place(x=760,y=850)

    def add_doctor(self):
        self.val1=self.Did_ent.get()
        self.val2=self.Dname_ent.get()
        self.val3=self.Gender_ent.get()
        self.val4=self.Age_ent.get()
        self.val5=self.Spec_ent.get()
        self.val6=self.Salary_ent.get()
        self.val7=self.Phone_ent.get()

        #checking if the user input is empty
        if self.val1=='' or self.val2=='' or self.val3==''or self.val4==''or self.val5==''or self.val6==''or self.val7=='':
            tkinter.messagebox.showinfo("Warning","Please Fill all the boxes")
        else:
           values=(str(self.val1),str(self.val2),str(self.val3),str(self.val4),str(self.val5),str(self.val6),str(self.val7))
           cursor.execute('INSERT INTO doctor(did,dname,gender,age,spec_code,sal,phone)VALUES(%s,%s,%s,%s,%s,%s,%s);',values)

           #cursor.execute(sql,values)
           conn.commit()
           tkinter.messagebox.showinfo("Success","Doctor Details for "+str(self.val2)+" has been added")

    def remove(self):
        id=str(e7.get())

        cursor.execute("select * from doctor where did = %s",(id,))
        v=cursor.fetchall()

        if (len(v)==0):
            tkinter.messagebox.showinfo("Warning","No such Doctor")
        else:
            cursor.execute('DELETE FROM doctor where did = %s',(id,))
            conn.commit()
            tkinter.messagebox.showinfo("Success","Doctor has been deleted")



    def dele(self):
        self.d=Toplevel(root,bg="steelblue")
        global e7


        self.id=Label(self.d,text="Enter Doctor Id to delete",font='arial 30 italic',fg='blue4',bg='RoyalBlue2')
        self.id.place(x=30, y=150)
        self.d.geometry("1080x400+0+0")
        e7 =Entry(self.d,width=20,font=('Verdana',25))
        e7.place(x=500, y=155)
        self.dbutton=Button(self.d,text="Delete",width=20,height=2,fg='blue4',bg='SkyBlue1',font=('Verdana',15),command=self.remove)
        self.dbutton.place(x=450, y=250)

    def viewappointment(self):
       global e8
       ap=str(e8.get())
       cursor.execute("select * from doctor where did=%s", (ap,))
       v=cursor.fetchall()
       if (len(v) == 0):
           errorD = Label(rootAP, text="NO SUCH DOCTOR", fg="red")
           errorD.place(x=20, y=120)
       else:
           cursor.execute("Select did,dname,gender,age,spec_code,sal,phone from doctor where did=%s",(ap,))
           s=cursor.fetchall()

           for i in s:
               s1=Label(rootAP,text=i,fg='green',font='arial 15 italic')
               s1.place(x=10,y=85)


    def va(self):
       global rootAP,e8
       rootAP=tkinter.Tk()
       rootAP.geometry("500x550")
       rootAP.title("DOCTOR LIST")
       h1=tkinter.Label(rootAP,text="ENTER DOCTOR ID TO VIEW DETAILS")
       h1.place(x=20,y=20)
       e8=Entry(rootAP)
       e8.place(x=20,y=40)
       b5=Button(rootAP,text="SEARCH",command=self.viewappointment)
       b5.place(x=30,y=65)
       rootAP.mainloop()

    def high(self):
        cursor.execute("select * from doctor ")
        v=cursor.fetchall()
        if (len(v) == 0):
            errorD = Label(rootAP, text="NO SUCH DOCTOR", fg="red")
            errorD.place(x=20, y=120)
        else:
            cursor.execute("Select MAX(sal) from doctor where spec_code in (select spec_code from doc_specialization where spec_desc='cardiologist')")
            max=cursor.fetchall()
            for i in max:
                v=i

            cursor.execute("Select did,dname,gender,age,spec_code,sal,phone from doctor where spec_code in (select spec_code from doc_specialization where spec_desc='cardiologist') AND sal=%s",(v[0],))
            s=cursor.fetchall()
            for i in s:
                s1=Label(rootAP,text=i,fg='green',font='arial 15 italic')
                s1.place(x=10,y=85)


    def ha(self):
          global rootAP,e8
          rootAP=tkinter.Tk()
          rootAP.geometry("500x550")
          rootAP.title("DOCTOR LIST")
          b5=Button(rootAP,text="SEARCH",command=self.high)
          b5.place(x=30,y=65)
          rootAP.mainloop()







#Creating the object
root =Tk()
b=Application(root)

#resolution of the window

root.geometry("1280x980+0+0")



#preventing the resize feature
root.resizable(False,False)
root.mainloop()

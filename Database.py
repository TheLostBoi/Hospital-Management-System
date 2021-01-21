import mysql.connector
from mysql.connector import Error



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





  cursor.execute("DROP TABLE if EXISTS appointment")
  cursor.execute("Drop table if EXISTS patient")
  cursor.execute("Drop table if EXISTS doctor")
  cursor.execute("Drop table if EXISTS doc_specialization")



  cursor.execute("""Create table patient
            (patid int(20),
             pname varchar(20) not null,
             gender varchar(10) not null,
             age int(5) not null,
             phone varchar(1c0) not null,
             address varchar(100) not null,
             PRIMARY KEY(patid))""")
  print("Patient table created")

  cursor.execute("""CREATE TABLE doc_specialization
           (spec_code int(50)PRIMARY KEY,
           spec_desc varchar(30))
             """)
  print("Specialization table created")

  cursor.execute("""create table doctor
            (did varchar(10) primary key,
             dname varchar(20)not null,
             gender varchar(10) not null,
             age int(5) not null,
             spec_code int(20) not null,
             sal float(10) not null,
             phone varchar(10),
             foreign key(spec_code)references doc_specialization(spec_code)
             )""")

  print("Doctor table created")


  cursor.execute("""create table appointment
            (patid int(20) not NULL ,
             did varchar(10) not NULL ,
             appt TIME not NULL ,
             appd DATE not NULL,
             descp varchar(100) NOT NULL,
             FOREIGN KEY(patid) references patient(patid) ON DELETE CASCADE,
             FOREIGN KEY(did) references doctor(did) ON DELETE CASCADE)
            """)

  print("Appointment table created")
  cursor.execute("SHOW tables")
  for tables in cursor:
	   print(tables)




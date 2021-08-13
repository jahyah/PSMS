import tkinter as tk
from tkinter import font as tkfont
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#from PIL import ImageTk,Image
import tkinter.messagebox
import csv
import os
import sqlite3


breed_list = ["","GERMAN SHEPHERD", "POODLE","LABRADOR RETRIEVERS","GOLDEN RETRIEVERS","FRENCH BULLDOG","SIBERIAN HUSKY","BEAGLES","ROTTWIELERS","GERMAN SHORTHAIRED POINTERS","PEMBROKE WELSH CORGIS"
            
            ,"RAGDOLL","EXOTIC","MAINE COON","PERSIAN","BRITISH SHORTHAIR","DEVON REX","ABYSSINIAN","AMERICAN SHORTHAIR","SCOTTISH FOLD","SPHYNX"
            
            ,"HOLLAND LOP","MINI LOP","DUTCH","LION HEAD","FRENCH LOP","CALIFORNIAN","DWARF PAPILION","NETHERLAND DWARF","MINI REX","FLEMISH GIANT"
            
            ,"PARAKET","COCKATIEL","FINCH","LOVEBIRD","MONK PARAKET","DOVE","PARROTLET","AFRICAN GRAY PARROT"

            ,"SYRIAN HAMSTER","CHINISE HAMSTER","DWARF CAMPBELL RUSSIAN HAMSTER","DWARF WINTER WHITE RUSSIAN HAMSTER","DWARF ROBOROVSKI HAMSTER"

            ,"AMRECICAN GUINEA PIG","CRESTED GUINEA PIG","CORONET GUINEA PIG","PERUVIAN GUINEA PIG","HIMALAYAN GUINEA PIG","SILKIE GUINEA PIG","TEDDY GUINEA PIG","TEXEL GUINEA PIG","REX GUINEA PIG","SHEBA GUINEA PIG","ALPACA GUINEA PIG"
         
            ,"BETTA","GOLD FISH","ANGEL FISH","CATFISH","GUPPIES","MOLLIES","NEON TETRAS","PLATIES","SWORD TAILS","ZEBRA DANIOS" ]

type_list = ["","DOG","CAT","RABBIT","BIRDS","HAMSTER","GUINEA PIG","FISH"]

date_list = ["", "07/01/2021","07/02/2021","07/03/2021","07/04/2021","07/05/2021","07/06/2021","07/07/2021","07/08/2021","07/09/2021","07/10/2021",
             "07/11/2021","07/12/2021","07/13/2021","07/14/2021","07/15/2021","07/16/2021","07/17/2021","07/18/2021","07/19/2021","07/20/2021",
             "07/21/2021","07/22/2021","07/23/2021","07/24/2021","07/25/2021","07/26/2021","07/27/2021","07/28/2021","07/29/2021","07/30/2021",
             "07/31/2021",

             "08/01/2021","08/02/2021","08/03/2021","08/04/2021","08/05/2021","08/06/2021","08/07/2021","08/08/2021","08/09/2021","08/10/2021",
             "08/11/2021","08/12/2021","08/13/2021","08/14/2021","08/15/2021","08/16/2021","08/17/2021","08/18/2021","08/19/2021","08/20/2021",
             "08/21/2021","08/22/2021","08/23/2021","08/24/2021","08/25/2021","08/26/2021","08/27/2021","08/28/2021","08/29/2021","08/30/2021",
             "08/31/2021",

             "09/01/2021","09/02/2021","09/03/2021","09/04/2021","09/05/2021","09/06/2021","09/07/2021","09/08/2021","09/09/2021","09/10/2021",
             "09/11/2021","09/12/2021","09/13/2021","09/14/2021","09/15/2021","09/16/2021","09/17/2021","09/18/2021","09/19/2021","09/20/2021",
             "09/21/2021","09/22/2021","09/23/2021","09/24/2021","09/25/2021","09/26/2021","09/27/2021","09/28/2021","09/29/2021","09/30/2021",

             "10/01/2021","10/02/2021","10/03/2021","10/04/2021","10/05/2021","10/06/2021","10/07/2021","10/08/2021","10/09/2021","10/10/2021",
             "10/11/2021","10/12/2021","10/13/2021","10/14/2021","10/15/2021","10/16/2021","10/17/2021","10/18/2021","10/19/2021","10/20/2021",
             "10/21/2021","10/22/2021","10/23/2021","10/24/2021","10/25/2021","10/26/2021","10/27/2021","10/28/2021","10/29/2021","10/30/2021",
             "10/31/2021",

             "11/01/2021","11/02/2021","11/03/2021","11/04/2021","11/05/2021","11/06/2021","11/07/2021","11/08/2021","11/09/2021","11/10/2021",
             "11/11/2021","11/12/2021","11/13/2021","11/14/2021","11/15/2021","11/16/2021","11/17/2021","11/18/2021","11/19/2021","11/20/2021",
             "11/21/2021","11/22/2021","11/23/2021","11/24/2021","11/25/2021","11/26/2021","11/27/2021","11/28/2021","11/29/2021","11/30/2021",

             "12/01/2021","12/02/2021","12/03/2021","12/04/2021","12/05/2021","12/06/2021","12/07/2021","12/08/2021","12/09/2021","12/10/2021",
             "12/11/2021","12/12/2021","12/13/2021","12/14/2021","12/15/2021","12/16/2021","12/17/2021","12/18/2021","12/19/2021","12/20/2021",
             "12/21/2021","12/22/2021","12/23/2021","12/24/2021","12/25/2021","12/26/2021","12/27/2021","12/28/2021","12/29/2021","12/30/2021",
             "12/31/2021"]

def PSMS_UserDatabase():
    conn = sqlite3.connect("PSMS.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS user (username VARCHAR PRIMARY KEY, password VARCHAR NOT NULL, role VARCHAR NOT NULL,login VARCHAR NOT NULL)")
    cur.execute("CREATE TABLE IF NOT EXISTS online_users (username VARCHAR PRIMARY KEY, password VARCHAR NOT NULL, role VARCHAR NOT NULL)")
    conn.commit() 
    conn.close()
PSMS_UserDatabase()
def connectCustomer():
    conn=sqlite3.connect("PSMS.db")
    cur=conn.cursor()
    cur.execute("PRAGMA foreign_keys = ON")
    cur.execute("""CREATE TABLE IF NOT EXISTS Customer(
        Customer_id VARCHAR(7) PRIMARY KEY,
        Customer_name VARCHAR(30),
        Mobile_no VARCHAR(11)
        )""")
    conn.commit()
connectCustomer()

def connectPET():
    conn=sqlite3.connect("PSMS.db")
    cur=conn.cursor()
    cur.execute("PRAGMA foreign_keys = ON")
    cur.execute("""CREATE TABLE IF NOT EXISTS PET(
        Pet_id VARCHAR(5) PRIMARY KEY,
        Breed VARCHAR,
        type VARCHAR,
        Customer_id VARCHAR(7),
        FOREIGN KEY(Customer_id) 
            REFERENCES Customer(Customer_id)
                ON DELETE CASCADE
            )""")
    conn.commit()
connectPET()

def connectAppointment():
    conn=sqlite3.connect("PSMS.db")
    cur=conn.cursor()
    cur.execute("PRAGMA foreign_keys = ON")
    cur.execute("""CREATE TABLE IF NOT EXISTS Appointment(
        Appointment_ID VARCHAR(5) PRIMARY KEY,
        Appointment_details VARCHAR,
        Appointment_date DATE,
        Appointment_Time VARCHAR,
        Status VARCHAR(10),
        Customer_id VARCHAR (7),
        FOREIGN KEY(Customer_id) 
            REFERENCES Customer(Customer_id)
                ON DELETE CASCADE
            )""")
    conn.commit()
connectAppointment()
def connectHistory():
    conn=sqlite3.connect('PSMS.db')
    cur=conn.cursor()
    cur.execute("""CREATE TABLE  IF NOT EXISTS History(
        Appointment_id    VARCHAR(5) PRIMARY KEY,
        Appointment_details   VARCHAR,
        Status    VARCHAR(10),
        appointment_date  DATE,
        Customer_id   VARCHAR(7),
        Pet_id    VARCHAR(5),
        FOREIGN KEY(Pet_id) 
            REFERENCES PET(Pet_id)
                ON DELETE CASCADE
                )""")
connectHistory()


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        #create window
        window = tk.Frame(self)
        window.pack()
        
        window.grid_rowconfigure(0, minsize=1000)
        window.grid_columnconfigure(0, minsize=1850)
        
        self.frames = {}
        for F in (LoginPage,HomePage,AddPage,history,customerPage,PetPage):
            frame = F(window,self)
            self.frames[F] = frame
            frame.grid(row=0,column=0, sticky="nsew")
    
        self.show_frame(LoginPage)
        
    def show_frame(self,page):
        frame = self.frames[page]
        frame.configure(background="white")
        frame.tkraise()
        
        
class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller.title("Pet Shop Management System")
        
        
        ##Variables
        
        Username = StringVar()
        Password= StringVar()
        
        ##Pics       
        self.first = PhotoImage(file="p16.png", master=self) 
        self.sec = PhotoImage(file="bg3.png", master=self) 
        self.third = PhotoImage(file="L23.png", master=self)
        #elf.fourth = PhotoImage(file="pro.png", master=self)
        
        appfirst = tk.Label(self, image = self.first, bd=0)
        appfirst.place(x=50,y=400)

        appsec = tk.Label(self, image = self.sec, bd=0)
        appsec.place(x=400,y=140)
        
        appthird = tk.Label(self, image = self.third, bd=0)
        appthird.place(x=850,y=0)
        
        #appfourth = tk.Label(self, image = self.fourth, bd=0)
        #appfourth.place(x=650,y=300)
        
            
        def onlineuser():
            conn=sqlite3.connect("PSMS.db")
            cur=conn.cursor()           
            cur.execute("UPDATE user SET login = 'Online' WHERE username = ?",(Username.get(),))
            cur.execute("UPDATE user SET login = '***' WHERE username != ?",(Username.get(),))
            conn.commit()
        
     
#                    
        def Login():
            #cur_user()
            #PSMS_UserDatabase()
            conn = sqlite3.connect("PSMS.db")
            cur = conn.cursor()
            if Username.get() == "" or Password.get() == "":
                tkinter.messagebox.showerror("Pet Shop Management System", "Please require the completed field")
            else:
                cur.execute("SELECT * FROM user WHERE username = ? and password = ?", (Username.get(), Password.get()))
                if cur.fetchone() is not None:
                    tkinter.messagebox.showinfo("Pet Shop Management System", "Login Successfully")
                    onlineuser()
                    controller.show_frame(HomePage)
                    Username.set('')
                    Password.set('')
                else:
                    tkinter.messagebox.showerror("Pet Shop Management System", "Invalid password or username")  
            conn.commit()
            conn.close()
        #def Loginevent(event):
            #login()            

            #########################################


##################################################################################


        
        ##Labels&Buttons
        welcome = tk.Label(self, text= "Log in to your account", font=("Arial Bold", 30), bg="white", bd=0, fg="grey23")
        welcome.place(x=405,y=220)
        
        
        user_name = tk.Label(self, font=("Poppins", 12), text="Username:", padx=5, pady=5, bg="white")
        user_name.place(x=600,y=300)
        user_name1 = tk.Entry(self, font=("Poppins", 13), textvariable=Username, width=30, bg="white")
        user_name1.place(x=600,y=340)
        
        password = tk.Label(self, font=("Poppins", 12), text="Password:", padx=5, pady=5, bg="white")
        password.place(x=600,y=390)
        password = tk.Entry(self, font=("Poppins", 13), textvariable=Password, width=30, bg="white",show="*")
        password.place(x=600,y=430)
        
        
        Button = tk.Button(self, bg="gray50", fg="white", text="Log in", width=20, font=("Arial Bold", 16), command=Login)
        Button.place(x=600,y=490)

        

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller.title("Pet Shop Management System")
        
        tapps = StringVar()
        c_user = StringVar()
        company = StringVar()
        capps = StringVar()
        
        leftbar = tk.Label(self,height = 100,width=35, bg= "grey13")
        leftbar.place(x=0,y=0)
        
        ##Pics
        self.picgo = PhotoImage(file="go2.png", master=self) 
        self.prof = PhotoImage(file="gg.png", master=self)
        self.uppic = PhotoImage(file="p14a.png", master=self) 
        self.picps = PhotoImage(file="pettt.png", master=self) 
        self.home = PhotoImage(file="home.png", master=self) 
        self.histo = PhotoImage(file="histo.png", master=self) 
        self.cust = PhotoImage(file="borrow.png", master=self) 
        self.out = PhotoImage(file="logout.png", master=self) 
        self.whiapp = PhotoImage(file="whiapp.png", master=self) 
        self.whipet = PhotoImage(file="whipet.png", master=self)
        self.whiexit = PhotoImage(file="whiexit.png", master=self)
        
        app_picgo = tk.Label(self, image = self.picgo, bd=0)
        app_picgo.place(x=800,y=340)
        
        app_picgo1 = tk.Label(self, image = self.uppic, bd=0)
        app_picgo1.place(x=300,y=0)
        
        app_ps = tk.Label(leftbar, image = self.picps, bd=0, bg="grey13")
        app_ps.place(x=20,y=50)
        
        app_home = tk.Label(leftbar, image = self.home, bd=0, bg="grey13")
        app_home.place(x=6,y=410)
        
        app_histo = tk.Label(leftbar, image = self.histo, bd=0, bg="grey13")
        app_histo.place(x=6,y=610)
        
        app_cust = tk.Label(leftbar, image = self.cust, bd=0, bg="grey13")
        app_cust.place(x=6,y=510)
        
        app_out = tk.Label(leftbar, image = self.out, bd=0, bg="grey13")
        app_out.place(x=6,y=660)
        
        app_whiapp = tk.Label(leftbar, image = self.whiapp, bd=0, bg="grey13")
        app_whiapp.place(x=6,y=460)
        
        app_whipet = tk.Label(leftbar, image = self.whipet, bd=0, bg="grey13")
        app_whipet.place(x=6,y=560)
        
        app_whiexit = tk.Label(leftbar, image = self.whiexit, bd=0, bg="grey13")
        app_whiexit.place(x=6,y=710)
        
        app_prof = tk.Label(leftbar, image = self.prof, bd=0, bg= "grey13")
        app_prof.place(x=45,y=190)
        
    
        
        ##Functions
        def setoffline():
            conn=sqlite3.connect("PSMS.db")
            cur=conn.cursor()
            cur.execute("SELECT username FROM user WHERE login ='Online'")
            username = cur.fetchone()
            cur.execute("UPDATE user SET login = '***' WHERE username = ?",(username,))
            conn.commit()
            
        def logout():
            iExit = tkinter.messagebox.askyesno("Pet Shop Management Sysytem","Do you want to log-out?")
            if iExit > 0:
                
                controller.show_frame(LoginPage)
                #setoffline()
                conn.commit()
                conn.close()
                
        def ExitApplication():
            MsgBox = tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
            if MsgBox == 'yes':
                #logout()
                app.destroy()
            else:
                tk.messagebox.showinfo('Return','You will now return to the application screen')


        def Current_User():
            conn = sqlite3.connect("PSMS.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM user WHERE login = 'Online'")
            row = cur.fetchall()
            for i in row:
                #print(i)
                c_user.set(i[0])
            self.user = Label(self, font=("Helvetica", 60),textvariable = c_user, bg ="white", fg = "black")
            self.user.place(x=1080,y=100)
            self.after(1000,Current_User)
            self.usera = Label(self, font=("Helvetica", 20),textvariable = c_user, bg ="grey13", fg = "white")
            self.usera.place(x=75,y=350)
            conn.commit()            
            conn.close()
         
        
         
            
        ##buttons
        
        Button1 = tk.Button(leftbar, text="HOME", font=("Courier", 18), bd=0, bg="grey13", fg="white", command= lambda: controller.show_frame(HomePage))
        Button1.place(x=40,y=410)
        
        Button2 = tk.Button(leftbar, text="APPOINTMENTS", font=("Courier", 18), bd=0, bg="grey13", fg="white", command= lambda: controller.show_frame(AddPage))
        Button2.place(x=40,y=460)
        
        Button3 = tk.Button(leftbar, text="CUSTOMER", font=("Courier", 18), bd=0, bg="grey13", fg="white", command= lambda: controller.show_frame(customerPage))
        Button3.place(x=40,y=510)
        
        Button4 = tk.Button(leftbar, text="PETS", font=("Courier", 18), bd=0, bg="grey13", fg="white", command= lambda: controller.show_frame(PetPage))
        Button4.place(x=40,y=560)
        
        Button5 = tk.Button(leftbar, text="HISTORY", font=("Courier", 18), bd=0, bg="grey13", fg="white", command= lambda: controller.show_frame(history))
        Button5.place(x=40,y=610)
        
        Button6 = tk.Button(leftbar, text="LOG-OUT", font=("Courier", 18), bd=0, bg="grey13", fg="white", command= logout)
        Button6.place(x=40,y=660)
        
        Button7 = tk.Button(leftbar, text="EXIT", font=("Courier", 18), bd=0, bg="grey13", fg="white", command=ExitApplication)
        Button7.place(x=40,y=710)
        
        
        ##Labels
        homelabel1 = tk.Label(self, text= "Hey there! ", font=("Helvetica", 60), bg="white", fg="grey23", anchor=CENTER)
        homelabel1.place(x=700,y=100)
        
        homelabel2 = tk.Label(self, text= "Got treats? We do.", font=("Courier", 40), bg="white", fg="grey23")
        homelabel2.place(x=700,y=230)
        
        homelabel4 = tk.Label(self, text= "Get a few more barks for your bucks!", font=("Courier", 20,"bold"), bg="white", fg="grey23")
        homelabel4.place(x=300,y=500)
        
        
        
        Current_User()
        

        

class AddPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller.title("Pet Shop Management System")
        
        CustomerID= StringVar()
        Customer_name = StringVar()
        Customer_mno = StringVar()
        Pet_name = StringVar()
        PetID= StringVar()
        Breed = StringVar()
        Pet_type = StringVar()
        Pet_name = StringVar()
        AppointmentID = StringVar()
        Appointment_details = StringVar()
        Schedule = StringVar()
        Status = StringVar()
        Appointment_Date = StringVar()
        Appointment_Time = StringVar()
        SearchBar_Var = StringVar()
        c_user = StringVar()
        role = []

        
        leftbar = tk.Label(self,height = 100,width=35, bg= "grey13")
        leftbar.place(x=0,y=0)
        
        topbar = tk.Label(self,height = 2,width=200, bg= "gray60")
        topbar.place(x=250,y=80)
        
        ##topbar label
        
        pagelabel = tk.Label(topbar, text= "APPOINTMENTS", font=("Helvetica", 15,"bold"), bg="gray60", fg="white")
        pagelabel.place(x=85,y=5)
        
        ##Pics
        
        self.prof1 = PhotoImage(file="bg3a.png", master=self)
        self.prof2 = PhotoImage(file="bg3b.png", master=self)
        self.prof3 = PhotoImage(file="bg3c.png", master=self)
        self.prof4 = PhotoImage(file="bg6a.png", master=self)
        self.prof5 = PhotoImage(file="bg6b.png", master=self)
        self.prof6 = PhotoImage(file="bg6c.png", master=self)
        self.prof7 = PhotoImage(file="bg6d.png", master=self)
        self.prof = PhotoImage(file="gg.png", master=self)
        self.picps = PhotoImage(file="pettt.png", master=self) 
        self.home = PhotoImage(file="home.png", master=self) 
        self.histo = PhotoImage(file="histo.png", master=self) 
        self.cust = PhotoImage(file="borrow.png", master=self) 
        self.out = PhotoImage(file="logout.png", master=self) 
        self.whiapp = PhotoImage(file="whiapp.png", master=self) 
        self.whipet = PhotoImage(file="whipet.png", master=self)
        self.whiexit = PhotoImage(file="whiexit.png", master=self)
        
        
        app_pl1 = tk.Label(self, image = self.prof1, bd=0, bg="gray60")
        app_pl1.place(x=340,y=5)
        
        app_pl2 = tk.Label(self, image = self.prof2, bd=0, bg="gray60")
        app_pl2.place(x=470,y=1)
        
        app_pl3 = tk.Label(self, image = self.prof3, bd=0, bg="gray60")
        app_pl3.place(x=590,y=1)
        
        app_pl4 = tk.Label(self, image = self.prof4, bd=0, bg="gray60")
        app_pl4.place(x=270,y=760)
        
        app_pl5 = tk.Label(self, image = self.prof5, bd=0, bg="gray60")
        app_pl5.place(x=520,y=750)
        
        app_pl6 = tk.Label(self, image = self.prof6, bd=0, bg="gray60")
        app_pl6.place(x=800,y=750)
        
        app_pl7 = tk.Label(self, image = self.prof7, bd=0, bg="gray60")
        app_pl7.place(x=1075,y=760)
        
        app_pl8 = tk.Label(self, image = self.prof4, bd=0, bg="gray60")
        app_pl8.place(x=1350,y=760)
        
        app_pl = tk.Label(topbar, image = self.whiapp, bd=0, bg="gray60")
        app_pl.place(x=50,y=0)
        
        app_ps = tk.Label(leftbar, image = self.picps, bd=0, bg="grey13")
        app_ps.place(x=20,y=50)
        
        app_home = tk.Label(leftbar, image = self.home, bd=0, bg="grey13")
        app_home.place(x=6,y=410)
        
        app_histo = tk.Label(leftbar, image = self.histo, bd=0, bg="grey13")
        app_histo.place(x=6,y=610)
        
        app_cust = tk.Label(leftbar, image = self.cust, bd=0, bg="grey13")
        app_cust.place(x=6,y=510)
        
        app_out = tk.Label(leftbar, image = self.out, bd=0, bg="grey13")
        app_out.place(x=6,y=660)
        
        app_whiapp = tk.Label(leftbar, image = self.whiapp, bd=0, bg="grey13")
        app_whiapp.place(x=6,y=460)
        
        app_whipet = tk.Label(leftbar, image = self.whipet, bd=0, bg="grey13")
        app_whipet.place(x=6,y=560)
        
        app_whiexit = tk.Label(leftbar, image = self.whiexit, bd=0, bg="grey13")
        app_whiexit.place(x=6,y=710)
        
        app_prof = tk.Label(leftbar, image = self.prof, bd=0, bg= "grey13")
        app_prof.place(x=45,y=190)
        
        ##Functions for logout and Exit
        
        def logout():
            iExit = tkinter.messagebox.askyesno("Pet Shop Management Sysytem","Do you want to log-out?")
            if iExit > 0:
                
                controller.show_frame(LoginPage)
                #setoffline()
                conn.commit()
                conn.close()
                
        def ExitApplication():
            MsgBox = tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
            if MsgBox == 'yes':
                #logout()
                app.destroy()
            else:
                tk.messagebox.showinfo('Return','You will now return to the application screen')
                
        def Current_User():
            conn = sqlite3.connect("PSMS.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM user WHERE login = 'Online'")
            row = cur.fetchall()
            for i in row:
                #print(i)
                c_user.set(i[0])
            self.usera = Label(self, font=("Helvetica", 20),textvariable = c_user, bg ="grey13", fg = "white")
            self.usera.place(x=75,y=350)
            self.after(1000,Current_User)
            conn.commit()            
            conn.close()

        
        
        ##leftbar buttons
        Button1 = tk.Button(leftbar, text="HOME", font=("Courier", 18), bd=0, bg="grey13", fg="white", command= lambda: controller.show_frame(HomePage))
        Button1.place(x=40,y=410)
        
        Button2 = tk.Button(leftbar, text="APPOINTMENTS", font=("Courier", 18), bd=0, bg="grey13", fg="white", command= lambda: controller.show_frame(AddPage))
        Button2.place(x=40,y=460)
        
        Button3 = tk.Button(leftbar, text="CUSTOMER", font=("Courier", 18), bd=0, bg="grey13", fg="white", command= lambda: controller.show_frame(customerPage))
        Button3.place(x=40,y=510)
        
        Button4 = tk.Button(leftbar, text="PETS", font=("Courier", 18), bd=0, bg="grey13", fg="white", command= lambda: controller.show_frame(PetPage))
        Button4.place(x=40,y=560)
        
        Button5 = tk.Button(leftbar, text="HISTORY", font=("Courier", 18), bd=0, bg="grey13", fg="white", command= lambda: controller.show_frame(history))
        Button5.place(x=40,y=610)
        
        Button6 = tk.Button(leftbar, text="LOG-OUT", font=("Courier", 18), bd=0, bg="grey13", fg="white", command= logout)
        Button6.place(x=40,y=660)
        
        Button7 = tk.Button(leftbar, text="EXIT", font=("Courier", 18), bd=0, bg="grey13", fg="white", command=ExitApplication)
        Button7.place(x=40,y=710)
        
        ##btnpic
        self.btna = PhotoImage(file="j.png", master=self) 
        self.btnb = PhotoImage(file="p2.png", master=self) 
        self.btnc = PhotoImage(file="p3.png", master=self)
        self.btnd = PhotoImage(file="ap5.png",master=self)
        self.btne = PhotoImage(file="house1.png",master=self)
        self.btnf = PhotoImage(file="histo.png",master=self)
        

        


        def ondoubleclick(event):

            x = self.tree.selection()
            values = self.tree.item(x,"values")
            CustomerID.set(values[0])
            AppointmentID.set(values[1])
            Appointment_details.set(values[2])
            Status.set(values[5])
            Appointment_Date.set(values[3])
            Appointment_Time.set(values[4])
            edit()

        def onleftclick1(event):
            x = self.tree.selection()
            values = self.tree.item(x,"values")
            CustomerID.set(values[0])
            AppointmentID.set(values[1])
            Appointment_details.set(values[2])
            Status.set(values[5])
            Appointment_Date.set(values[3])
            Appointment_Time.set(values[4])
            updatestat()

        def onrightclick(event):
            x = self.tree.selection()
            values = self.tree.item(x,"values")
            CustomerID.set(values[0])
            AppointmentID.set(values[1])
            Appointment_details.set(values[2])
            Status.set(values[5])
            Appointment_Date.set(values[4])
            Appointment_Time.set(values[5])
            showpet()

        def onclick(event):
            x = self.tree1.selection()
            values = self.tree1.item(x,"values")
            conn = sqlite3.connect("PSMS.db")
            cur= conn.cursor()
            cur.execute("SELECT * FROM Customer WHERE Customer_name = ?",(values[0],))
            c = cur.fetchall()
            Customer_name.set(values[0])
            for a in c:
                CustomerID.set(a[0])
                Customer_mno.set(a[2])                      
            custclick()

        def clear1():
            CustomerID.set('')
            Customer_name.set('')
            Customer_mno.set('')
            PetID.set('')
            Pet_name.set('')
            Breed.set('')
            Pet_type.set('')
            AppointmentID.set('')
            Appointment_details.set('')
            Status.set('')
            Appointment_Date.set('')
            SearchBar_Var.set('')
            Appointment_Time.set('')
        def clear():
            PetID.set('')
            Pet_name.set('')
            Breed.set('')
            Pet_type.set('')
            AppointmentID.set('')
            Appointment_details.set('')
            Appointment_Date.set('')
            SearchBar_Var.set('')
            Appointment_Time.set('')

        #Treeview
        style = ttk.Style(self)
        style.configure("Treeview",
            background = "silver",
            foreground = "black",
            fieldbackground = "silver"
            )
        style.map('Treeview',background=[('selected','deep sky blue')])
        scroll_y=Scrollbar(self, orient=VERTICAL)
        self.tree = ttk.Treeview(self, height=10, columns=("CustomerID","AppointmentID", \
                                                            "Appointment_details","Appointment_Date","Appointment_Time", "Status"), yscrollcommand=scroll_y.set)

        #scroll_y.pack(side=RIGHT, fill=Y)
        #scroll_y.place(x=600,y=600)
        
        self.tree.heading("CustomerID", text="Customer ID")
        self.tree.heading("AppointmentID", text="Appointment ID")
        self.tree.heading("Appointment_details", text="Details")
        self.tree.heading("Status", text="Status")
        self.tree.heading("Appointment_Date", text="Date")
        self.tree.heading("Appointment_Time", text="Time")        
        self.tree.heading("Status", text="Status")
        self.tree['show'] = 'headings'

        self.tree.column("CustomerID", width=50)
        self.tree.column("AppointmentID", width=60)
        self.tree.column("Appointment_details", width=150)
        self.tree.column("Appointment_Date", width=45)
        self.tree.column("Appointment_Time", width=45)
        self.tree.column("Status", width=45)


        self.tree.bind("<Double-Button-1>", ondoubleclick)
        self.tree.bind("<Return>",onleftclick1)
        self.tree.bind("<Double-Button-3>", onrightclick)        

        #self.tree.pack(fill=BOTH,expand=1)
        
        self.tree.place(x=400,y=205,width=950,height=560)

        scroll_y=Scrollbar(self, orient=VERTICAL)
        self.tree1 = ttk.Treeview(self, height=10, columns=("Customer_name"), yscrollcommand=scroll_y.set)

        #scroll_y.pack(side=RIGHT, fill=Y)
        #scroll_y.place(x=600,y=600)
        
        self.tree1.heading("Customer_name", text="Customer Name")

        self.tree1['show'] = 'headings'

        self.tree1.column("Customer_name", width=60)
        self.tree1.place(x=280,y=205,width=100,height=560)

        self.tree1.bind("<Double-Button-1>",onclick)


        def add():
            clear()


            global role
            conn=sqlite3.connect('PSMS.db')
            cur=conn.cursor()
            cur.execute("SELECT * FROM user WHERE login = 'Online'")
            #cur.execute("SELECT * FROM Appointment WHERE username != '-' AND company_name != '-' ")
            item=cur.fetchall()
            for m in item:
                n = m[0]#NAME
                role = m[2]
            if role == 'Admin':
                win = Toplevel()
                win.title("ADD APPOINTMENT")
                win.geometry("900x700")
                win.configure(background="white")

                def dates(data):
                    datelist.delete(0,END)
                    for item in data:
                        datelist.insert(END, item)
    
                def filloutdates(event):
                    App_date.delete(0, END)
                    App_date.insert(0,datelist.get(ACTIVE))
    
                def checkdates(event):
                    click = App_date.get()
    
                    if click =='':
                        data = date_list
                    else:
                        data = []
                        for i in date_list:
                            if click.lower() in i.lower():
                                data.append(i)
                        dates(data)
                
                #========================================# 
         

                def breeds(data):
                    breedlist.delete(0, END)
                    for item in data:
                        breedlist.insert(END, item)
    
                def fillout(event):
                    Etype.delete(0,END)
                    Etype.insert(0,breedlist.get(ACTIVE))
    
                def check(event):
                    click = Etype.get()
    
                    if click == '':
                        data = breed_list
                    else:
                        data = []
                        for i in breed_list:
                            if click.lower() in i.lower():
                                data.append(i)
                    breeds(data)
                #=========================================#
                def pettypes(data):
                    typelist.delete(0,END)
                    for item in data:
                        typelist.insert(END, item)
    
    
                def fillout1(event):
                    Ebreed.delete(0,END)
                    Ebreed.insert(0,typelist.get(ACTIVE))
    
    
                def check1(event):
                    click = Ebreed.get()
                    if click =="":
                        data = type_list
                    else:
                        data = []
                        for i in type_list:
                            if click.lower() in i.lower():
                                data.append(i)
                    pettypes(data)


                LCus_name = Label(win, width=50, bg="snow",fg="grey24", font=("Courier", 14),text="Customer Name:")
                LCus_name.place(x=20, y=10,width=151 )
                Cus_name = Entry(win, font=("Courier", 14),textvariable = Customer_name, width=28, bg="snow",fg="grey24",highlightthickness=2)
                Cus_name.place(x=200, y=10)

                LCus_ID = Label(win, width=50, bg="snow",fg="grey24", font=("Courier", 14),text="Customer ID:")
                LCus_ID.place(x=550, y=10,width=147 )
                Cus_ID = Entry(win, font=("Courier", 14),textvariable = CustomerID, width=15, bg="snow",fg="grey24",highlightthickness=2)
                Cus_ID.place(x=700, y=10)

                LCus_mno = Label(win, width=50, bg="snow",fg="grey24", font=("Courier", 14),text="Mobile No.:")
                LCus_mno.place(x=20, y=50,width=140 )
                Cus_mno = Entry(win, font=("Courier", 14),textvariable = Customer_mno, width=28, bg="snow",fg="grey24",highlightthickness=2)
                Cus_mno.place(x=200, y=50)

                LApp_date = Label(win, width=50, bg="snow",fg="grey24", font=("Courier", 14),text="Date:")
                LApp_date.place(x=550, y=50,width=70 )
                App_date = Entry(win, font=("Courier", 14),textvariable = Appointment_Date, width=15, bg="snow",fg="grey24",highlightthickness=2)
                App_date.place(x=700, y=50)
                #datelist = Listbox(win, width=61,height=1,bg="snow",bd=0)
                #datelist.place(x=700, y=75)

                LApp_det = Label(win, width=50, bg="snow",fg="grey24", font=("Courier", 14),text="Details:")
                LApp_det.place(x=20, y=100,width=90 )
                App_det = Entry(win, font=("Courier", 14),textvariable = Appointment_details, width=28, bg="snow",fg="grey24",highlightthickness=2)
                App_det.place(x=200, y=100)

                LApp_det = Label(win, width=50, bg="snow",fg="grey24", font=("Courier", 14),text="Time:")
                LApp_det.place(x=550, y=100,width=90 )
                App_time = ttk.Combobox(win, font=("Courier", 14),value=["08:00-09:00 AM","09:00-10:00 AM","10:00-11:00 AM","11:00-12:00 PM","01:00-02:00 PM","02:00-03:00 PM","03:00-04:00 PM","04:00-05:00 PM"], textvariable = Appointment_Time, width=14,state='readonly')
                # = Entry(win, font=("Courier", 14),textvariable = Appointment_Time, width=15, bg="snow",fg="grey24",highlightthickness=2)
                App_time.place(x=700, y=100)

                LApp_ID = Label(win, width=50, bg="snow",fg="grey24", font=("Courier", 14),text="Appointment ID:")
                LApp_ID.place(x=20, y=140,width=180 )
                App_ID = Entry(win, font=("Courier", 14),textvariable = AppointmentID, width=28, bg="snow",fg="grey24",highlightthickness=2)
                App_ID.place(x=200, y=140)


                LApp_Stat = Label(win, width=50, bg="snow",fg="grey24", font=("Courier", 14),text="Status:")
                LApp_Stat.place(x=550, y=140,width=90 )
                App_Stat = Entry(win, font=("Courier", 14),textvariable = Status, width=15, bg="snow",fg="grey24",highlightthickness=2)
                App_Stat.place(x=700, y=140)
                App_Stat.insert(0,"Processing")


                style = ttk.Style(win)
                style.configure("Treeview",
                    background = "silver",
                    foreground = "black",
                    fieldbackground = "silver"
                    )
                style.map('Treeview',background=[('selected','deep sky blue')])
                scroll_y=Scrollbar(win, orient=VERTICAL)
                treep = ttk.Treeview(win, height=10, columns=("PetID","Pet_name","Breed","Pet_type"), yscrollcommand=scroll_y.set)

                #scroll_y.pack(side=RIGHT, fill=Y)
                #scroll_y.place(x=600,y=600)
                

                treep.heading("PetID", text="Pet ID")
                treep.heading("Pet_name", text="Pet Name")
                treep.heading("Pet_type", text="Type")
                treep.heading("Breed", text="Breed")

                treep['show'] = 'headings'

                treep.column("PetID", width=50)
                treep.column("Pet_type", width=40)
                treep.column("Pet_type", width=40)
                treep.column("Breed", width=100)

                treep.place(x=20,y=310,width=850,height=300)

                Lpetid = Label(win, width=50, bg="snow",fg="grey24", font=("Courier", 14),text="Pet ID:")
                Lpetid.place(x=20, y=180,width=100 )
                Epetid = Entry(win, font=("Courier", 14),textvariable = PetID, width=28, bg="snow",fg="grey24",highlightthickness=2)
                Epetid.place(x=200, y=180)

                Lpetname = Label(win, width=50, bg="snow",fg="grey24", font=("Courier", 14),text="Pet NAME:")
                Lpetname.place(x=20, y=220,width=100 )
                Epetname = Entry(win, font=("Courier", 14),textvariable = Pet_name, width=28, bg="snow",fg="grey24",highlightthickness=2)
                Epetname.place(x=200, y=220)

                Lbreed = Label(win, width=50, bg="snow",fg="grey24", font=("Courier", 14),text="Type:")
                Lbreed.place(x=550, y=180,width=100 )
                Ebreed = Entry(win, font=("Courier", 14),textvariable = Pet_type, width=15, bg="snow",fg="grey24",highlightthickness=2)
                Ebreed.place(x=700, y=180)

                Ltype = Label(win, width=50, bg="snow",fg="grey24", font=("Courier", 14),text="Breed:")
                Ltype.place(x=550, y=220,width=100 )
                Etype = Entry(win, font=("Courier", 14),textvariable = Breed, width=15, bg="snow",fg="grey24",highlightthickness=2)
                Etype.place(x=700, y=220)


                datelist = Listbox(win, width=28,height=1,bg="snow",bd=0)
                datelist.place(x=700, y=75)

                typelist = Listbox(win, width=28,height=1,bg="snow",bd=0)
                typelist.place(x=700, y=205)

                breedlist = Listbox(win, width=28,height=1,bg="snow",bd=0)
                breedlist.place(x=700, y=245)


                dates(date_list)
                datelist.bind("<<ListboxSelect>>",filloutdates)
                App_date.bind("<KeyRelease>", checkdates)
                
                
                breeds(breed_list)
                breedlist.bind("<<ListboxSelect>>", fillout)
                Etype.bind("<KeyRelease>" ,check) 
    
                pettypes(type_list)
                typelist.bind("<<ListboxSelect>>",fillout1)
                Ebreed.bind("<KeyRelease>",check1)

                def displaycustpets():
                    treep.tag_configure('oddrow',background="white")
                    treep.tag_configure('evenrow',background="silver")                    
                    for i in treep.get_children():
                        treep.delete(i)
                    conn = sqlite3.connect("PSMS.db")
                    cur= conn.cursor()

                    cur.execute("PRAGMA foreign_keys = ON")
                    cur.execute("SELECT * FROM Pet WHERE Customer_id = ?",(CustomerID.get(),))
                    pet=cur.fetchall()
                    count = 0
                    for i in pet:
                        if count % 2 == 0:
                            treep.insert("", tk.END,iid=count,text=f'{count + 1}', values = (i),tags = ('evenrow',))
                        else:
                            treep.insert("", tk.END,iid=count,text=f'{count + 1}', values = (i),tags = ('oddrow',)) 
                        count += 1
                        conn.close()                           
                displaycustpets()



                def pet():
                    if PetID.get() == "" or Pet_name.get() == "" or Breed.get() == "" or Pet_type.get() == "":
                        tkinter.messagebox.showinfo("Pet Shop Management System","Fill all of the entries")
                    else:                       
                        conn=sqlite3.connect("PSMS.db")
                        cur=conn.cursor()
                        cur.execute("INSERT INTO PET(Pet_id,Pet_name,Breed,Type,Customer_id,Schedule) VALUES(?,?,?,?,?,?)",\
                            (PetID.get(),Pet_name.get(),Breed.get(),Pet_type.get(),CustomerID.get(),Schedule.get()))
                        conn.commit()
                        displaycustpets()
                        conn.close()
                        PetID.set('')
                        Pet_name.set('')
                        Breed.set('')
                        Pet_type.set('')
                        Schedule.set('')




                def selectpet():
                    x = treep.selection()
                    petid = treep.item(x)["values"][0]
                    conn=sqlite3.connect("PSMS.db")
                    cur=conn.cursor()
                    cur.execute("UPDATE PET SET Schedule = 'Scheduled' WHERE pet_id = ?",(petid,))
                    conn.commit()
                    conn.close()
                    #tkinter.messagebox.showinfo("Pet Shop Management System","Selected Succesfully")

                def deselectpet():
                    x = treep.selection()
                    petid = treep.item(x)["values"][0]
                    conn=sqlite3.connect("PSMS.db")
                    cur=conn.cursor()
                    cur.execute("UPDATE PET SET Schedule = 'Unscheduled' WHERE pet_id = ?",(petid,))
                    conn.commit()
                    conn.close()
                    #tkinter.messagebox.showinfo("Pet Shop Management System","deselected Succesfully")

                def addappointment():
                    displaycustpets()
                    conn=sqlite3.connect("PSMS.db")
                    cur=conn.cursor()
                    cur.execute("SELECT * FROM CUSTOMER WHERE customer_id = ?",(CustomerID.get(),))
                    row=cur.fetchall()
                    if row != []:
                        cur.execute("INSERT INTO Appointment(Appointment_id,Appointment_details,appointment_date,Status,Customer_id,Appointment_Time) VALUES ( ?,?,?,?,?,?)",\
                            (AppointmentID.get(),Appointment_details.get(),Appointment_Date.get(),Status.get(),CustomerID.get(),Appointment_Time.get()))
                    else:
                        cur.execute("INSERT INTO Customer(Customer_id,Customer_name,Mobile_no) VALUES(?,?,?)",\
                            (CustomerID.get(),Customer_name.get(),Customer_mno.get()))
                        cur.execute("INSERT INTO Appointment(Appointment_id,Appointment_details,appointment_date,Status,Customer_id,Appointment_Time) VALUES ( ?,?,?,?,?,?)",\
                            (AppointmentID.get(),Appointment_details.get(),Appointment_Date.get(),Status.get(),CustomerID.get(),Appointment_Time.get()))                        

                    conn.commit()
                    conn.close()
                    win.destroy()
                    displaycus()
                    display()
                    clear1()

                    tkinter.messagebox.showinfo("Pet Shop Management System","Appointment Added Succesfully")                    

                but1= tk.Button(win,font=("Courier", 14),width=15,text="Refresh",bg="gray50",fg="white",command=displaycustpets)
                but1.place(x=20,y=260,height=30)

                but2= tk.Button(win,font=("Courier", 14),width=15,text="Add PET",bg="gray50",fg="white",command=pet)
                but2.place(x=250,y=260,height=30)

                but4= tk.Button(win,font=("Courier", 14),width=15,text="SELECT PET",bg="gray50",fg="white",command=selectpet)
                but4.place(x=480,y=260,height=30)

                but5= tk.Button(win,font=("Courier", 14),width=15,text="DESELECT PET",bg="gray50",fg="white",command=deselectpet)
                but5.place(x=700,y=260,height=30)

                but6= tk.Button(win,font=("Courier", 14),width=15,text="Submit",bg="gray50",fg="white",command=addappointment)
                but6.place(x=350,y=630,height=30)

            else:
                 tkinter.messagebox.showinfo("Pet Shop Management System","only the ADMIN can ADD Appointment")

        def edit():
            def dates(data):
                datelist.delete(0,END)
                for item in data:
                    datelist.insert(END, item)

            def filloutdates(event):
                App_date.delete(0, END)
                App_date.insert(0,datelist.get(ACTIVE))

            def checkdates(event):
                click = App_date.get()

                if click =='':
                    data = date_list
                else:
                    data = []
                    for i in date_list:
                        if click.lower() in i.lower():
                            data.append(i)
                    dates(data)
            
            #========================================# 
     

            def breeds(data):
                breedlist.delete(0, END)
                for item in data:
                    breedlist.insert(END, item)

            def fillout(event):
                Etype.delete(0,END)
                Etype.insert(0,breedlist.get(ACTIVE))

            def check(event):
                click = Etype.get()

                if click == '':
                    data = breed_list
                else:
                    data = []
                    for i in breed_list:
                        if click.lower() in i.lower():
                            data.append(i)
                breeds(data)
            #=========================================#
            def pettypes(data):
                typelist.delete(0,END)
                for item in data:
                    typelist.insert(END, item)


            def fillout1(event):
                Ebreed.delete(0,END)
                Ebreed.insert(0,typelist.get(ACTIVE))


            def check1(event):
                click = Ebreed.get()
                if click =="":
                    data = type_list
                else:
                    data = []
                    for i in type_list:
                        if click.lower() in i.lower():
                            data.append(i)
                pettypes(data)


            win = Toplevel()
            win.title("EDIT APPOINTMENT")
            win.geometry("900x700")
            win.configure(background="white")


            LCus_ID = Label(win, width=50, bg="snow",fg="grey24", font=("Courier", 14),text="Customer ID:")
            LCus_ID.place(x=20, y=40,width=147 )
            Cus_ID = Entry(win, font=("Courier", 14),textvariable = CustomerID, width=28, bg="snow",fg="grey24",highlightthickness=2)
            Cus_ID.place(x=200, y=40)


            LApp_date = Label(win, width=50, bg="snow",fg="grey24", font=("Courier", 14),text="Date:")
            LApp_date.place(x=550, y=40,width=70 )
            App_date = Entry(win, font=("Courier", 14),textvariable = Appointment_Date, width=15, bg="snow",fg="grey24",highlightthickness=2)
            App_date.place(x=700, y=40)
            #datelist = Listbox(win, width=61,height=1,bg="snow",bd=0)
            #datelist.place(x=700, y=75)

            LApp_det = Label(win, width=50, bg="snow",fg="grey24", font=("Courier", 14),text="Details:")
            LApp_det.place(x=20, y=100,width=90 )
            App_det = Entry(win, font=("Courier", 14),textvariable = Appointment_details, width=28, bg="snow",fg="grey24",highlightthickness=2)
            App_det.place(x=200, y=100)

            LApp_time = Label(win, width=50, bg="snow",fg="grey24", font=("Courier", 14),text="Time:")
            LApp_time.place(x=550, y=100,width=90 )
            App_time = ttk.Combobox(win, font=("Courier", 14),value=["08:00-09:00 AM","09:00-10:00 AM","10:00-11:00 AM","11:00-12:00 PM","01:00-02:00 PM","02:00-03:00 PM","03:00-04:00 PM","04:00-05:00 PM"], textvariable = Appointment_Time, width=14,state='readonly')
            # = Entry(win, font=("Courier", 14),textvariable = Appointment_Time, width=15, bg="snow",fg="grey24",highlightthickness=2)
            App_time.place(x=700, y=100)

            LApp_ID = Label(win, width=50, bg="snow",fg="grey24", font=("Courier", 14),text="Appointment ID:")
            LApp_ID.place(x=20, y=140,width=180 )
            App_ID = Entry(win, font=("Courier", 14),textvariable = AppointmentID, width=28, bg="snow",fg="grey24",highlightthickness=2)
            App_ID.place(x=200, y=140)

            LApp_Stat = Label(win, width=50, bg="snow",fg="grey24", font=("Courier", 14),text="Status:")
            LApp_Stat.place(x=550, y=140,width=90 )
            App_Stat = Entry(win, font=("Courier", 14),textvariable = Status, width=15, bg="snow",fg="grey24",highlightthickness=2)
            App_Stat.place(x=700, y=140)



            Lpetid = Label(win, width=50, bg="snow",fg="grey24", font=("Courier", 14),text="Pet ID:")
            Lpetid.place(x=20, y=180,width=100 )
            Epetid = Entry(win, font=("Courier", 14),textvariable = PetID, width=28, bg="snow",fg="grey24",highlightthickness=2)
            Epetid.place(x=200, y=180)

            Lpetname = Label(win, width=50, bg="snow",fg="grey24", font=("Courier", 14),text="Pet NAME:")
            Lpetname.place(x=20, y=220,width=100 )
            Epetname = Entry(win, font=("Courier", 14),textvariable = Pet_name, width=28, bg="snow",fg="grey24",highlightthickness=2)
            Epetname.place(x=200, y=220)

            Lbreed = Label(win, width=50, bg="snow",fg="grey24", font=("Courier", 14),text="Type:")
            Lbreed.place(x=550, y=180,width=100 )
            Ebreed = Entry(win, font=("Courier", 14),textvariable = Pet_type, width=15, bg="snow",fg="grey24",highlightthickness=2)
            Ebreed.place(x=700, y=180)

            Ltype = Label(win, width=50, bg="snow",fg="grey24", font=("Courier", 14),text="Breed:")
            Ltype.place(x=550, y=220,width=100 )
            Etype = Entry(win, font=("Courier", 14),textvariable = Breed, width=15, bg="snow",fg="grey24",highlightthickness=2)
            Etype.place(x=700, y=220)


            datelist = Listbox(win, width=28,height=1,bg="snow",bd=0)
            datelist.place(x=700, y=75)

            typelist = Listbox(win, width=28,height=1,bg="snow",bd=0)
            typelist.place(x=700, y=205)

            breedlist = Listbox(win, width=28,height=1,bg="snow",bd=0)
            breedlist.place(x=700, y=245)


            dates(date_list)
            datelist.bind("<<ListboxSelect>>",filloutdates)
            App_date.bind("<KeyRelease>", checkdates)
            
            
            breeds(breed_list)
            breedlist.bind("<<ListboxSelect>>", fillout)
            Etype.bind("<KeyRelease>" ,check) 

            pettypes(type_list)
            typelist.bind("<<ListboxSelect>>",fillout1)
            Ebreed.bind("<KeyRelease>",check1)

            style = ttk.Style(win)
            style.configure("Treeview",
                background = "silver",
                foreground = "black",
                fieldbackground = "silver"
                )
            style.map('Treeview',background=[('selected','deep sky blue')])
            scroll_y=Scrollbar(win, orient=VERTICAL)
            treep = ttk.Treeview(win, height=10, columns=("PetID","Pet_name","Breed","Pet_type"), yscrollcommand=scroll_y.set)

            #scroll_y.pack(side=RIGHT, fill=Y)
            #scroll_y.place(x=600,y=600)
            

            treep.heading("PetID", text="Pet ID")
            treep.heading("Pet_name", text="Pet Name")
            treep.heading("Pet_type", text="Type")
            treep.heading("Breed", text="Breed")

            treep['show'] = 'headings'

            treep.column("PetID", width=50)
            treep.column("Pet_type", width=40)
            treep.column("Pet_type", width=40)
            treep.column("Breed", width=100)

            treep.place(x=20,y=310,width=850,height=300)
            
            def displaycustpets():
                treep.tag_configure('oddrow',background="white")
                treep.tag_configure('evenrow',background="silver")                    
                for i in treep.get_children():
                    treep.delete(i)
                conn = sqlite3.connect("PSMS.db")
                cur= conn.cursor()

                cur.execute("PRAGMA foreign_keys = ON")
                cur.execute("SELECT * FROM Pet WHERE Customer_id = ?",(CustomerID.get(),))
                pet=cur.fetchall()
                count = 0
                for i in pet:
                    if count % 2 == 0:
                        treep.insert("", tk.END,iid=count,text=f'{count + 1}', values = (i),tags = ('evenrow',))
                    else:
                        treep.insert("", tk.END,iid=count,text=f'{count + 1}', values = (i),tags = ('oddrow',)) 
                    count += 1
                    conn.close()                           





            def pet():
                if PetID.get() == "" or Pet_name.get() == "" or Breed.get() == "" or Pet_type.get() == "":
                    tkinter.messagebox.showinfo("Pet Shop Management System","Fill all of the entries")
                else:                       
                    conn=sqlite3.connect("PSMS.db")
                    cur=conn.cursor()
                    cur.execute("INSERT INTO PET(Pet_id,Pet_name,Breed,Type,Customer_id,Schedule) VALUES(?,?,?,?,?,?)",\
                        (PetID.get(),Pet_name.get(),Breed.get(),Pet_type.get(),CustomerID.get(),Schedule.get()))
                    conn.commit()
                    conn.close()
                    displaycustpets()


            def selectpet():
                x = treep.selection()
                petid = treep.item(x)["values"][0]
                conn=sqlite3.connect("PSMS.db")
                cur=conn.cursor()
                cur.execute("UPDATE PET SET Schedule = 'Scheduled' WHERE pet_id = ?",(petid,))
                conn.commit()
                conn.close()
                #tkinter.messagebox.showinfo("Pet Shop Management System","Selected Succesfully")

            def deselectpet():
                x = treep.selection()
                petid = treep.item(x)["values"][0]
                conn=sqlite3.connect("PSMS.db")
                cur=conn.cursor()
                cur.execute("UPDATE PET SET Schedule = 'Unscheduled' WHERE pet_id = ?",(petid,))
                conn.commit()
                conn.close()
                #tkinter.messagebox.showinfo("Pet Shop Management System","deselected Succesfully")

            def updateappointment():
                displaycustpets()
                slctd = self.tree.selection()

                for i in slctd:
                    conn=sqlite3.connect("PSMS.db")
                    cur=conn.cursor()
                    cur.execute("UPDATE Appointment SET Appointment_id = ?,Appointment_details =?, appointment_date=?,Status = ?,Appointment_Time=?,customer_id = ?\
                        WHERE customer_id = ? ",(AppointmentID.get(),Appointment_details.get(),Appointment_Date.get(),Status.get(),Appointment_Time.get(),CustomerID.get(),self.tree.set(i,"#1")))
                     

                    conn.commit()
                    conn.close()
                    win.destroy()
                    display()
                    displaycus()
                    clear1()
                    tkinter.messagebox.showinfo("Pet Shop Management System","Appointment Updated Succesfully")                    

            but1= tk.Button(win,font=("Courier", 14),width=15,text="Refresh",bg="gray50",fg="white",command=displaycustpets)
            but1.place(x=20,y=260,height=30)

            but2= tk.Button(win,font=("Courier", 14),width=15,text="Add PET",bg="gray50",fg="white",command=pet)
            but2.place(x=250,y=260,height=30)

            but4= tk.Button(win,font=("Courier", 14),width=15,text="SELECT PET",bg="gray50",fg="white",command=selectpet)
            but4.place(x=480,y=260,height=30)

            but5= tk.Button(win,font=("Courier", 14),width=15,text="DESELECT PET",bg="gray50",fg="white",command=deselectpet)
            but5.place(x=700,y=260,height=30)

            but6= tk.Button(win,font=("Courier", 14),width=15,text="Submit",bg="gray50",fg="white",command=updateappointment)
            but6.place(x=350,y=630,height=30)
            displaycustpets()

        def search():
            for i in self.tree.get_children():
                self.tree.delete(i)

            search = self.SearchBar.get()
            conn=sqlite3.connect("PSMS.db")
            cur=conn.cursor()
            cur.execute("SELECT * FROM Appointment ")
            rows=cur.fetchall()
            
            for row in rows:
                if row[0].startswith(search) or row[1].startswith(search) or row[2].startswith(search) or row[3].startswith(search) or row[4].startswith(search) or row[5].startswith(search):
                    self.tree.insert("", tk.END,text=row[0], values=(row[4],row[0],row[1],row[2],row[5],row[3]))

            conn.close()


        def deletedata():
            global role
            conn=sqlite3.connect('PSMS.db')
            cur=conn.cursor()
            cur.execute("SELECT * FROM user WHERE login = 'Online'")
            item = cur.fetchall()
            for m in item:
                role = m[2]#role
                response = messagebox.askyesno("Are you sure you want to delete this??")                              
                if response > 0:
                    if role == 'Admin':
                        click = self.tree.selection()[0]
                        app_id = self.tree.item(click)["values"][1]
                        conn = sqlite3.connect("PSMS.db")
                        cur=conn.cursor()
                        cur.execute("SELECT * FROM Appointment ")
                        rows = cur.fetchall()
                        for row in rows:
                            if app_id == row[1]:
                                app_id = row[1]
                        cur.execute("DELETE FROM Appointment WHERE Appointment_ID = ?", (app_id,))

                        conn.commit()
                        self.tree.delete(click)
                        display()
                    else:
                        tkinter.messagebox.showinfo("Pet Shop Management System","Only The Admin can DELETE Appointment")

        def display():
            clear1()
            self.tree.tag_configure('oddrow',background="white")
            self.tree.tag_configure('evenrow',background="silver")
            for i in self.tree.get_children():
                self.tree.delete(i)
            conn = sqlite3.connect("PSMS.db")
            cur= conn.cursor()
            cur.execute("PRAGMA foreign_keys = ON")
            cur.execute("SELECT * FROM Customer")
            Cus=cur.fetchall()
            cur.execute("SELECT * FROM Appointment WHERE Status = 'Processing'")
            App=cur.fetchall()
            count = 0
            for a in App:
                if count % 2 == 0:
                    self.tree.insert("", tk.END,iid=count,text=f'{count + 1}', values=(a[4],a[0],a[1],a[2],a[5],a[3]),tags=('evenrow',))
                else:
                    self.tree.insert("", tk.END,iid=count,text=f'{count + 1}', values=(a[4],a[0],a[1],a[2],a[5],a[3]),tags=('oddrow',))

                count += 1
            conn.commit()
            conn.close()
        display()

        def showpet():
            up=Toplevel()
            up.title("SHOW PETS")
            up.geometry("550x270")

            style = ttk.Style(up)
            style.configure("Treeview",
                background = "silver",
                foreground = "black",
                fieldbackground = "silver"
                )
            style.map('Treeview',background=[('selected','deep sky blue')])
            scroll_y=Scrollbar(up, orient=VERTICAL)
            treep = ttk.Treeview(up, height=10, columns=("PetID","Pet_name","Breed","Pet_type"), yscrollcommand=scroll_y.set)

            #scroll_y.pack(side=RIGHT, fill=Y)
            #scroll_y.place(x=600,y=600)
            

            treep.heading("PetID", text="Pet ID")
            treep.heading("Pet_name", text="Pet Name")
            treep.heading("Pet_type", text="Type")
            treep.heading("Breed", text="Breed")

            treep['show'] = 'headings'

            treep.column("PetID", width=70)
            treep.column("Pet_name", width=40)
            treep.column("Pet_type", width=40)
            treep.column("Breed", width=70)
            treep.place(x=20,y=20,width=500,height=200)

            def displaypets():
                treep.tag_configure('oddrow',background="white")
                treep.tag_configure('evenrow',background="silver")
                slctd = self.tree.selection()
                cus_id = self.tree.item(slctd)['values'][0]
                conn = sqlite3.connect("PSMS.db")
                cur= conn.cursor()
                cur.execute("SELECT * FROM PET WHERE Customer_id = ? AND Schedule = 'Scheduled'",(cus_id,))
                rows=cur.fetchall()
                count = 0
                for row in rows:
                    if count % 2 == 0:
                        treep.insert("", tk.END,iid=count,text=f'{count + 1}', values=(row),tags=('evenrow',))

                    else:
                        treep.insert("", tk.END,iid=count,text=f'{count + 1}', values=(row),tags=('oddrow',))
                    count += 1
                conn.commit()

                conn.close()

            displaypets()

        def displaycus():
            for i in self.tree1.get_children():
                self.tree1.delete(i)
            conn = sqlite3.connect("PSMS.db")
            cur= conn.cursor()
            cur.execute("PRAGMA foreign_keys = ON")
            cur.execute("SELECT customer_name FROM Customer")
            Cus=cur.fetchall()
            for c in Cus:
                self.tree1.insert("", tk.END, values=c[0:])
            conn.commit()
            conn.close()
            clear1()
        displaycus()

        def custclick():
            for i in self.tree.get_children():
                self.tree.delete(i)            
            self.tree.tag_configure('oddrow',background="white")
            self.tree.tag_configure('evenrow',background="silver")
            clicked = self.tree1.selection()[0]
            cus_name = self.tree1.item(clicked)["values"][0]
            conn = sqlite3.connect("PSMS.db")
            cur= conn.cursor()
            cur.execute("SELECT * FROM Customer WHERE Customer_name = ? ",(cus_name,))
            cus_id = cur.fetchall()
            for c in cus_id:
               cusid = c[0]
            cur.execute("SELECT * FROM Appointment WHERE Customer_id = ?",(cusid,))
            row = cur.fetchall()
            count = 0
            for a in row:
                if count % 2 == 0:
                    self.tree.insert("", tk.END,iid=count,text=f'{count + 1}', values=(a[4],a[0],a[1],a[2],a[5],a[3]),tags=('evenrow',))
                else:
                    self.tree.insert("", tk.END,iid=count,text=f'{count + 1}', values=(a[4],a[0],a[1],a[2],a[5],a[3]),tags=('oddrow',))

                count += 1
            conn.commit()
            conn.close()

        def updatestat():
            up1=Toplevel()
            up1.title("UPDATE STATUS")
            up1.geometry("230x150")
            Label(up1, text = "STATUS",fg="grey24", font=("Courier", 14)).place(x=80,y=10)

            stat1 = ttk.Combobox(up1, font=("Courier", 14),value=["Completed","Cancelled"], textvariable = Status, width=17,state='readonly')
            stat1.place(x=10, y=50)

            def Selectstat():
                slctd = self.tree.selection()
                app_id = self.tree.item(slctd)['values'][1]
                conn = sqlite3.connect("PSMS.db")
                cur= conn.cursor()
                cur.execute("UPDATE APPOINTMENT SET STATUS = ? WHERE Appointment_ID = ?",(Status.get(),app_id))
                cur.execute("INSERT INTO History(Appointment_ID,Appointment_details,appointment_date,Status,Customer_id,Appointment_Time)VALUES(?,?,?,?,?,?)",\
                    (AppointmentID.get(),Appointment_details.get(),Appointment_Date.get(),Status.get(),CustomerID.get(),Appointment_Time.get()))               
                up1.destroy()
                conn.commit()
                tkinter.messagebox.showinfo("Pet Shop Management System","Status Updated Successfully")
                display()
                clear1()

            but3= tk.Button(up1,font=("Courier", 14),width=10,text="ENTER",bg="gray50",fg="white",command = Selectstat)
            but3.place(x=50,y=90,height=30)



        title = tk.Label(self, text= "Pet Shop Management System", font=("Courier", 25), bg="white", bd=0, fg="grey23")
        title.place(x=250,y=80)

        pagetitle = tk.Label(self, text= "APPOINTMENTS", font=("Courier", 10, "bold"), bg="white", bd=0, fg="grey23")
        pagetitle.place(x=85,y=780)
        
        #self.ref = tk.Button(self, bd=0, bg="white",command=resfresh)#add
        #self.ref.place(x=830,y=165)
        #self.btnadd.config(cursor= "hand2")


        self.SearchBar = Entry(self, font=("Courier", 14), textvariable=SearchBar_Var, width=47,bg="snow",fg="grey23")
        self.SearchBar.place(x=460,y=170)
        self.SearchBar.insert(0,'Search here')

        self.btnsearch = tk.Button(self, image=self.btna, bd=0, bg="white",command=search)
        self.btnsearch.place(x=990,y=170)
        self.btnsearch.config(cursor= "hand2")

        self.btnrefresh = tk.Button(self, image=self.btnd, bd=0, bg="white",command=display)
        self.btnrefresh.place(x=390,y=165)
        self.btnrefresh.config(cursor= "hand2")

        self.btnrefresh = tk.Button(self, text="Refresh",font=("Courier", 14), bd=0,command=displaycus,bg="gray50",fg="white",width = 8)
        self.btnrefresh.place(x=280,y=165)
        self.btnrefresh.config(cursor= "hand2")


        self.btnadd = tk.Button(self, image=self.btnb, bd=0, bg="white",command=add)#add
        self.btnadd.place(x=1060,y=165)
        self.btnadd.config(cursor= "hand2")

        self.btndel = tk.Button(self, image=self.btnc, bd=0, bg="white",command=deletedata)#delete
        self.btndel.place(x=1140,y=162)
        self.btndel.config(cursor= "hand2")

        Current_User()
        
        #Button = tk.Button(self, text="Home", font=("Courier", 12, "bold"), bd=0, bg="white", fg="grey23", command= lambda: controller.show_frame(HomePage))
        #Button.place(x=450,y=90)
        #Button.bind("<Button-1>",clickevent)

class PetPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller.title("Pet Shop Management System")
        
        CustomerID= StringVar()
        Customer_name = StringVar()
        Customer_mno = StringVar()
        PetID= StringVar()
        Breed = StringVar()
        Pet_type = StringVar()
        Pet_name = StringVar()
        AppointmentID = StringVar()
        Appointment_details = StringVar()
        Status = StringVar()
        Appointment_Date = StringVar()
        SearchBar_Var = StringVar()
        c_user = StringVar()
        role = []
        
        
        ##Labels
        leftbar = tk.Label(self,height = 100,width=35, bg= "grey13")
        leftbar.place(x=0,y=0)
        
        topbar = tk.Label(self,height = 2,width=200, bg= "gray60")
        topbar.place(x=250,y=80)
        
        ##topbar label
        
        pagelabel = tk.Label(topbar, text= "LIST OF PETS", font=("Helvetica", 15,"bold"), bg="gray60", fg="white")
        pagelabel.place(x=85,y=5)
        
        ##Pics
        
        self.prof1 = PhotoImage(file="bg3a.png", master=self)
        self.prof2 = PhotoImage(file="bg3b.png", master=self)
        self.prof3 = PhotoImage(file="bg3c.png", master=self)
        self.prof4 = PhotoImage(file="bg6a.png", master=self)
        self.prof5 = PhotoImage(file="bg6b.png", master=self)
        self.prof6 = PhotoImage(file="bg6c.png", master=self)
        self.prof7 = PhotoImage(file="bg6d.png", master=self)
        self.prof = PhotoImage(file="gg.png", master=self)
        self.picps = PhotoImage(file="pettt.png", master=self) 
        self.home = PhotoImage(file="home.png", master=self) 
        self.histo = PhotoImage(file="histo.png", master=self) 
        self.cust = PhotoImage(file="borrow.png", master=self) 
        self.out = PhotoImage(file="logout.png", master=self) 
        self.whiapp = PhotoImage(file="whiapp.png", master=self) 
        self.whipet = PhotoImage(file="whipet.png", master=self)
        self.whiexit = PhotoImage(file="whiexit.png", master=self)
        self.btna = PhotoImage(file="j.png", master=self) 
        
        
        app_pl1 = tk.Label(self, image = self.prof1, bd=0, bg="gray60")
        app_pl1.place(x=340,y=5)
        
        app_pl2 = tk.Label(self, image = self.prof2, bd=0, bg="gray60")
        app_pl2.place(x=470,y=1)
        
        app_pl3 = tk.Label(self, image = self.prof3, bd=0, bg="gray60")
        app_pl3.place(x=590,y=1)
        
        app_pl4 = tk.Label(self, image = self.prof4, bd=0, bg="gray60")
        app_pl4.place(x=270,y=760)
        
        app_pl5 = tk.Label(self, image = self.prof5, bd=0, bg="gray60")
        app_pl5.place(x=520,y=750)
        
        app_pl6 = tk.Label(self, image = self.prof6, bd=0, bg="gray60")
        app_pl6.place(x=800,y=750)
        
        app_pl7 = tk.Label(self, image = self.prof7, bd=0, bg="gray60")
        app_pl7.place(x=1075,y=760)
        
        app_pl8 = tk.Label(self, image = self.prof4, bd=0, bg="gray60")
        app_pl8.place(x=1350,y=760)
        
        app_pl = tk.Label(topbar, image = self.whipet, bd=0, bg="gray60")
        app_pl.place(x=50,y=0)
        
        app_ps = tk.Label(leftbar, image = self.picps, bd=0, bg="grey13")
        app_ps.place(x=20,y=50)
        
        app_home = tk.Label(leftbar, image = self.home, bd=0, bg="grey13")
        app_home.place(x=6,y=410)
        
        app_histo = tk.Label(leftbar, image = self.histo, bd=0, bg="grey13")
        app_histo.place(x=6,y=610)
        
        app_cust = tk.Label(leftbar, image = self.cust, bd=0, bg="grey13")
        app_cust.place(x=6,y=510)
        
        app_out = tk.Label(leftbar, image = self.out, bd=0, bg="grey13")
        app_out.place(x=6,y=660)
        
        app_whiapp = tk.Label(leftbar, image = self.whiapp, bd=0, bg="grey13")
        app_whiapp.place(x=6,y=460)
        
        app_whipet = tk.Label(leftbar, image = self.whipet, bd=0, bg="grey13")
        app_whipet.place(x=6,y=560)
        
        app_whiexit = tk.Label(leftbar, image = self.whiexit, bd=0, bg="grey13")
        app_whiexit.place(x=6,y=710)
        
        app_prof = tk.Label(leftbar, image = self.prof, bd=0, bg= "grey13")
        app_prof.place(x=45,y=190)
        
        ##Functions for logout and Exit
        
        def logout():
            iExit = tkinter.messagebox.askyesno("Pet Shop Management Sysytem","Do you want to log-out?")
            if iExit > 0:
                
                controller.show_frame(LoginPage)
                #setoffline()
                conn.commit()
                conn.close()
                
        def ExitApplication():
            MsgBox = tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
            if MsgBox == 'yes':
                #logout()
                app.destroy()
            else:
                tk.messagebox.showinfo('Return','You will now return to the application screen')
        
        def Current_User():
            conn = sqlite3.connect("PSMS.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM user WHERE login = 'Online'")
            row = cur.fetchall()
            for i in row:
                #print(i)
                c_user.set(i[0])
            self.usera = Label(self, font=("Helvetica", 20),textvariable = c_user, bg ="grey13", fg = "white")
            self.usera.place(x=75,y=350)
            self.after(1000,Current_User)           
            conn.commit()            
            conn.close()
            
            
        ##leftbar buttons
        Button1 = tk.Button(leftbar, text="HOME", font=("Courier", 18), bd=0, bg="grey13", fg="white", command= lambda: controller.show_frame(HomePage))
        Button1.place(x=40,y=410)
        
        Button2 = tk.Button(leftbar, text="APPOINTMENTS", font=("Courier", 18), bd=0, bg="grey13", fg="white", command= lambda: controller.show_frame(AddPage))
        Button2.place(x=40,y=460)
        
        Button3 = tk.Button(leftbar, text="CUSTOMER", font=("Courier", 18), bd=0, bg="grey13", fg="white", command= lambda: controller.show_frame(customerPage))
        Button3.place(x=40,y=510)
        
        Button4 = tk.Button(leftbar, text="PETS", font=("Courier", 18), bd=0, bg="grey13", fg="white", command= lambda: controller.show_frame(PetPage))
        Button4.place(x=40,y=560)
        
        Button5 = tk.Button(leftbar, text="HISTORY", font=("Courier", 18), bd=0, bg="grey13", fg="white", command= lambda: controller.show_frame(history))
        Button5.place(x=40,y=610)
        
        Button6 = tk.Button(leftbar, text="LOG-OUT", font=("Courier", 18), bd=0, bg="grey13", fg="white", command= logout)
        Button6.place(x=40,y=660)
        
        Button7 = tk.Button(leftbar, text="EXIT", font=("Courier", 18), bd=0, bg="grey13", fg="white", command=ExitApplication)
        Button7.place(x=40,y=710)
        

        def ondoubleclick(event):
            #update()
            x = self.tree.selection()[0]
            values = self.tree.item(x,"values")
            CustomerID.set(values[0])
            Customer_name.set(values[1])
            Customer_mno.set(values[2])
            PetID.set(values[3])
            Breed.set(values[4])
            Pet_type.set(values[5])
            AppointmentID.set(values[6])
            Appointment_details.set(values[7])
            Status.set(values[8])
            Appointment_Date.set(values[9])
            update()
        def onrightclick(event):
            x = self.tree.selection()
            values = self.tree.item(x,"values")
            CustomerID.set(values[0])
            Customer_name.set(values[1])
            Customer_mno.set(values[2])
            PetID.set(values[3])
            Breed.set(values[4])
            Pet_type.set(values[5])
            AppointmentID.set(values[6])
            Appointment_details.set(values[7])
            Status.set(values[8])
            Appointment_Date.set(values[9])
            updatestat()

        def clear():
            CustomerID.set('')
            Customer_name.set('')
            Customer_mno.set('')
            PetID.set('')
            Breed.set('')
            Pet_type.set('')
            AppointmentID.set('')
            Appointment_details.set('')
            Status.set('')
            Appointment_Date.set('')
            SearchBar_Var.set('')

                        
        #Treeview
        style = ttk.Style(self)
        style.configure("Treeview",
            background = "silver",
            foreground = "black",
            fieldbackground = "silver"
            )
        style.map('Treeview',background=[('selected','deep sky blue')])
        scroll_y=Scrollbar(self, orient=VERTICAL)

        self.tree = ttk.Treeview(self, height=10, columns=("PetID","Pet_name","Breed","Pet_type"), yscrollcommand=scroll_y.set)
        
        self.tree.heading("PetID", text="Pet ID")
        self.tree.heading("Pet_name", text="Pet name")

        self.tree.heading("Breed", text="Breed")
        self.tree.heading("Pet_type", text="Type")

        self.tree['show'] = 'headings'


        self.tree.column("PetID", width=50)
        self.tree.column("Pet_name", width=60)        
        self.tree.column("Breed", width=100)
        self.tree.column("Pet_type", width=40)

        self.tree.bind("<Double-Button-1>", ondoubleclick)
        self.tree.bind("<Return>", onrightclick)
    
        
        self.tree.place(x=300,y=175,width=1000,height=560)
        
        
        def search():
            for i in self.tree.get_children():
                self.tree.delete(i)

            search = self.SearchBar.get()
            conn=sqlite3.connect("PSMS.db")
            cur=conn.cursor()
            cur.execute("SELECT * FROM PET ")
            rows=cur.fetchall()
            
            for row in rows:
                if row[0].startswith(search) or row[1].startswith(search) or row[2].startswith(search) or row[3].startswith(search) or row[4].startswith(search):
                    self.tree.insert("", tk.END,text=row[0], values=(row[0],row[1],row[2],row[3],row[4]))
            conn.close()


        def deletedata():
            global role
            conn=sqlite3.connect('PSMS.db')
            cur=conn.cursor()
            cur.execute("SELECT * FROM user WHERE login = 'Online'")
            item = cur.fetchall()
            for m in item:
                role = m[2]#role
                response = messagebox.askyesno("Are you sure you want to delete this??")                              
                if response > 0:
                    if role == 'Admin':
                        click = self.tree.selection()[0]
                        pet_id = self.tree.item(click)["values"][1]
                        conn = sqlite3.connect("PSMS.db")
                        cur=conn.cursor()
                        cur.execute("SELECT * FROM PET ")
                        rows = cur.fetchall()
                        for row in rows:
                            if pet_id == row[1]:
                                pet_id = row[1]
                        print(pet_id)
                        cur.execute("DELETE FROM PET WHERE Pet_id = ?", (pet_id,))

                        conn.commit()
                        self.tree.delete(click)
                        display()
                    else:
                        tkinter.messagebox.showinfo("Pet Shop Management System","Only The Admin can DELETE Appointment")


        def display():
            self.tree.tag_configure('oddrow',background="white")
            self.tree.tag_configure('evenrow',background="silver")
            for i in self.tree.get_children():
                self.tree.delete(i)
            conn = sqlite3.connect("PSMS.db")
            cur= conn.cursor()
            cur.execute("PRAGMA foreign_keys = ON")
            cur.execute("SELECT * FROM Customer")
            Cus=cur.fetchall()
            cur.execute("SELECT * FROM Appointment")
            App=cur.fetchall()
            cur.execute("SELECT * FROM PET")
            pet = cur.fetchall()
            count = 0
            for p in pet:
                if count % 2 == 0:
                    self.tree.insert("", tk.END,iid=count,text=f'{count + 1}', values=(p[3],p[0],p[1],p[2]), tags=('evenrow',))
                else:
                    self.tree.insert("", tk.END,iid=count,text=f'{count + 1}', values=(p[3],p[0],p[1],p[2]), tags=('oddrow',))

                count += 1
            conn.commit()
            conn.close()

        self.btnrefresh = tk.Button(self, text="Refresh",font=("Courier", 14), bd=0,command=display,bg="gray50",fg="white",width = 8)
        self.btnrefresh.place(x=330,y=140)
        self.btnrefresh.config(cursor= "hand2")
            
        self.SearchBar = Entry(self, font=("Courier", 14), textvariable=SearchBar_Var, width=47,bg="snow",fg="grey23")
        self.SearchBar.place(x=600,y=140)
        self.SearchBar.insert(0,'Search here')

        self.btnsearch = tk.Button(self, image=self.btna, bd=0, bg="white",command=search)
        self.btnsearch.place(x=1130,y=140)
        self.btnsearch.config(cursor= "hand2")

        Current_User()
        display()


class customerPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller.title("Pet Shop Management System")
        
        CustomerID= StringVar()
        Customer_name = StringVar()
        Customer_mno = StringVar()
        PetID= StringVar()
        Breed = StringVar()
        Pet_type = StringVar()
        AppointmentID = StringVar()
        Appointment_details = StringVar()
        Status = StringVar()
        Appointment_Date = StringVar()
        SearchBar_Var = StringVar()
        c_user = StringVar()
        role = []
        
        
        ##Labels
        leftbar = tk.Label(self,height = 100,width=35, bg= "grey13")
        leftbar.place(x=0,y=0)
        
        topbar = tk.Label(self,height = 2,width=200, bg= "gray60")
        topbar.place(x=250,y=80)
        
        ##topbar label
        
        pagelabel = tk.Label(topbar, text= "LIST OF CUSTOMERS", font=("Helvetica", 15,"bold"), bg="gray60", fg="white")
        pagelabel.place(x=85,y=5)
        
        ##Pics
        
        self.prof1 = PhotoImage(file="bg3a.png", master=self)
        self.prof2 = PhotoImage(file="bg3b.png", master=self)
        self.prof3 = PhotoImage(file="bg3c.png", master=self)
        self.prof4 = PhotoImage(file="bg6a.png", master=self)
        self.prof5 = PhotoImage(file="bg6b.png", master=self)
        self.prof6 = PhotoImage(file="bg6c.png", master=self)
        self.prof7 = PhotoImage(file="bg6d.png", master=self)
        self.prof = PhotoImage(file="gg.png", master=self)
        self.picps = PhotoImage(file="pettt.png", master=self) 
        self.home = PhotoImage(file="home.png", master=self) 
        self.histo = PhotoImage(file="histo.png", master=self) 
        self.cust = PhotoImage(file="borrow.png", master=self) 
        self.out = PhotoImage(file="logout.png", master=self) 
        self.whiapp = PhotoImage(file="whiapp.png", master=self) 
        self.whipet = PhotoImage(file="whipet.png", master=self)
        self.whiexit = PhotoImage(file="whiexit.png", master=self)
        self.btna = PhotoImage(file="j.png", master=self) 
        
        
        app_pl1 = tk.Label(self, image = self.prof1, bd=0, bg="gray60")
        app_pl1.place(x=340,y=5)
        
        app_pl2 = tk.Label(self, image = self.prof2, bd=0, bg="gray60")
        app_pl2.place(x=470,y=1)
        
        app_pl3 = tk.Label(self, image = self.prof3, bd=0, bg="gray60")
        app_pl3.place(x=590,y=1)
        
        app_pl4 = tk.Label(self, image = self.prof4, bd=0, bg="gray60")
        app_pl4.place(x=270,y=760)
        
        app_pl5 = tk.Label(self, image = self.prof5, bd=0, bg="gray60")
        app_pl5.place(x=520,y=750)
        
        app_pl6 = tk.Label(self, image = self.prof6, bd=0, bg="gray60")
        app_pl6.place(x=800,y=750)
        
        app_pl7 = tk.Label(self, image = self.prof7, bd=0, bg="gray60")
        app_pl7.place(x=1075,y=760)
        
        app_pl8 = tk.Label(self, image = self.prof4, bd=0, bg="gray60")
        app_pl8.place(x=1350,y=760)
        
        app_pl = tk.Label(topbar, image = self.cust, bd=0, bg="gray60")
        app_pl.place(x=50,y=0)
        
        app_ps = tk.Label(leftbar, image = self.picps, bd=0, bg="grey13")
        app_ps.place(x=20,y=50)
        
        app_home = tk.Label(leftbar, image = self.home, bd=0, bg="grey13")
        app_home.place(x=6,y=410)
        
        app_histo = tk.Label(leftbar, image = self.histo, bd=0, bg="grey13")
        app_histo.place(x=6,y=610)
        
        app_cust = tk.Label(leftbar, image = self.cust, bd=0, bg="grey13")
        app_cust.place(x=6,y=510)
        
        app_out = tk.Label(leftbar, image = self.out, bd=0, bg="grey13")
        app_out.place(x=6,y=660)
        
        app_whiapp = tk.Label(leftbar, image = self.whiapp, bd=0, bg="grey13")
        app_whiapp.place(x=6,y=460)
        
        app_whipet = tk.Label(leftbar, image = self.whipet, bd=0, bg="grey13")
        app_whipet.place(x=6,y=560)
        
        app_whiexit = tk.Label(leftbar, image = self.whiexit, bd=0, bg="grey13")
        app_whiexit.place(x=6,y=710)
        
        app_prof = tk.Label(leftbar, image = self.prof, bd=0, bg= "grey13")
        app_prof.place(x=45,y=190)
        
        ##Functions for logout and Exit
        
        def logout():
            iExit = tkinter.messagebox.askyesno("Pet Shop Management Sysytem","Do you want to log-out?")
            if iExit > 0:
                
                controller.show_frame(LoginPage)
                #setoffline()
                conn.commit()
                conn.close()
                
        def ExitApplication():
            MsgBox = tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
            if MsgBox == 'yes':
                #logout()
                app.destroy()
            else:
                tk.messagebox.showinfo('Return','You will now return to the application screen')
        
        def Current_User():
            conn = sqlite3.connect("PSMS.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM user WHERE login = 'Online'")
            row = cur.fetchall()
            for i in row:
                #print(i)
                c_user.set(i[0])
            self.usera = Label(self, font=("Helvetica", 20),textvariable = c_user, bg ="grey13", fg = "white")
            self.usera.place(x=75,y=350)
            self.after(1000,Current_User)
            conn.commit()            
            conn.close()
            
            
        ##leftbar buttons
        Button1 = tk.Button(leftbar, text="HOME", font=("Courier", 18), bd=0, bg="grey13", fg="white", command= lambda: controller.show_frame(HomePage))
        Button1.place(x=40,y=410)
        
        Button2 = tk.Button(leftbar, text="APPOINTMENTS", font=("Courier", 18), bd=0, bg="grey13", fg="white", command= lambda: controller.show_frame(AddPage))
        Button2.place(x=40,y=460)
        
        Button3 = tk.Button(leftbar, text="CUSTOMER", font=("Courier", 18), bd=0, bg="grey13", fg="white", command= lambda: controller.show_frame(customerPage))
        Button3.place(x=40,y=510)
        
        Button4 = tk.Button(leftbar, text="PETS", font=("Courier", 18), bd=0, bg="grey13", fg="white", command= lambda: controller.show_frame(PetPage))
        Button4.place(x=40,y=560)
        
        Button5 = tk.Button(leftbar, text="HISTORY", font=("Courier", 18), bd=0, bg="grey13", fg="white", command= lambda: controller.show_frame(history))
        Button5.place(x=40,y=610)
        
        Button6 = tk.Button(leftbar, text="LOG-OUT", font=("Courier", 18), bd=0, bg="grey13", fg="white", command= logout)
        Button6.place(x=40,y=660)
        
        Button7 = tk.Button(leftbar, text="EXIT", font=("Courier", 18), bd=0, bg="grey13", fg="white", command=ExitApplication)
        Button7.place(x=40,y=710)

        def ondoubleclick(event):
            #update()
            x = self.tree.selection()[0]
            values = self.tree.item(x,"values")
            CustomerID.set(values[0])
            Customer_name.set(values[1])
            Customer_mno.set(values[2])
            PetID.set(values[3])
            Breed.set(values[4])
            Pet_type.set(values[5])
            AppointmentID.set(values[6])
            Appointment_details.set(values[7])
            Status.set(values[8])
            Appointment_Date.set(values[9])
            update()
        def onrightclick(event):
            x = self.tree.selection()
            values = self.tree.item(x,"values")
            CustomerID.set(values[0])
            Customer_name.set(values[1])
            Customer_mno.set(values[2])
            PetID.set(values[3])
            Breed.set(values[4])
            Pet_type.set(values[5])
            AppointmentID.set(values[6])
            Appointment_details.set(values[7])
            Status.set(values[8])
            Appointment_Date.set(values[9])
            updatestat()

        def clear():
            CustomerID.set('')
            Customer_name.set('')
            Customer_mno.set('')
            PetID.set('')
            Breed.set('')
            Pet_type.set('')
            AppointmentID.set('')
            Appointment_details.set('')
            Status.set('')
            Appointment_Date.set('')
            SearchBar_Var.set('')

                        
        #Treeview
        style = ttk.Style(self)
        style.configure("Treeview",
            background = "silver",
            foreground = "black",
            fieldbackground = "silver"
            )
        style.map('Treeview',background=[('selected','deep sky blue')])
        scroll_y=Scrollbar(self, orient=VERTICAL)

        self.tree = ttk.Treeview(self, height=10, columns=("CustomerID","Customer_name","Customer_mno",), yscrollcommand=scroll_y.set)

        
        self.tree.heading("CustomerID", text="Customer ID")
        self.tree.heading("Customer_name", text="Name")
        self.tree.heading("Customer_mno", text="Phone number")

        self.tree['show'] = 'headings'

        self.tree.column("CustomerID", width=60)
        self.tree.column("Customer_name", width=110)
        self.tree.column("Customer_mno", width=70)

        self.tree.bind("<Double-Button-1>", ondoubleclick)
        self.tree.bind("<Return>", onrightclick)
        
        
        self.tree.place(x=300,y=175,width=1000,height=560)

        def search():
            for i in self.tree.get_children():
                self.tree.delete(i)

            search = self.SearchBar.get()
            conn=sqlite3.connect("PSMS.db")
            cur=conn.cursor()
            cur.execute("SELECT * FROM Customer ")
            rows=cur.fetchall()
            
            for row in rows:
                if row[0].startswith(search) or row[1].startswith(search) or row[2].startswith(search):
                    self.tree.insert("", tk.END,text=row[0], values=(row[0],row[1],row[2]))

            conn.close()

        def deletedata():
            global role
            conn=sqlite3.connect('PSMS.db')
            cur=conn.cursor()
            cur.execute("SELECT * FROM user WHERE login = 'Online'")
            item = cur.fetchall()
            for m in item:
                role = m[2]#role
                response = messagebox.askyesno("Are you sure you want to delete this??")                              
                if response > 0:
                    if role == 'Admin':
                        click = self.tree.selection()[0]
                        cus_id = self.tree.item(click)["values"][0]
                        conn = sqlite3.connect("PSMS.db")
                        cur=conn.cursor()
                        cur.execute("SELECT * FROM Customer ")
                        rows = cur.fetchall()
                        for row in rows:
                            if cus_id == row[0]:
                                cus_id = row[0]
                        cur.execute("DELETE FROM Customer WHERE Customer_id = ?", (cus_id,))

                        conn.commit()
                        self.tree.delete(click)
                        display()
                    else:
                        tkinter.messagebox.showinfo("Pet Shop Management System","Only The Admin can DELETE Appointment")

        def display():
            self.tree.tag_configure('oddrow',background="white")
            self.tree.tag_configure('evenrow',background="silver")
            for i in self.tree.get_children():
                self.tree.delete(i)
            conn = sqlite3.connect("PSMS.db")
            cur= conn.cursor()
            cur.execute("PRAGMA foreign_keys = ON")
            cur.execute("SELECT * FROM Customer")
            Cus=cur.fetchall()
            cur.execute("SELECT * FROM Appointment")
            App=cur.fetchall()
            cur.execute("SELECT * FROM PET")
            pet = cur.fetchall()
            count = 0
            for c in Cus:
                if count % 2 == 0:
                    self.tree.insert("", tk.END,iid=count,text=f'{count + 1}', values=(c), tags=('evenrow',))
                else:
                    self.tree.insert("", tk.END,iid=count,text=f'{count + 1}', values=(c), tags=('oddrow',))
                count += 1
            conn.commit()
            conn.close()

        self.btnrefresh = tk.Button(self, text="Refresh",font=("Courier", 14), bd=0,command=display,bg="gray50",fg="white",width = 8)
        self.btnrefresh.place(x=330,y=140)
        self.btnrefresh.config(cursor= "hand2")

        self.SearchBar = Entry(self, font=("Courier", 14), textvariable=SearchBar_Var, width=47,bg="snow",fg="grey23")
        self.SearchBar.place(x=600,y=140)
        self.SearchBar.insert(0,'Search here')

        self.btnsearch = tk.Button(self, image=self.btna, bd=0, bg="white",command=search)
        self.btnsearch.place(x=1130,y=140)
        self.btnsearch.config(cursor= "hand2")
        
        Current_User()
        display()



class history(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller.title("PSMS")
        
        SearchBar_Var = StringVar()
        c_user = StringVar()

        ##Labels
        
        leftbar = tk.Label(self,height = 100,width=35, bg= "grey13")
        leftbar.place(x=0,y=0)
        
        topbar = tk.Label(self,height = 2,width=200, bg= "gray60")
        topbar.place(x=250,y=80)
        
        ##topbar label
        
        pagelabel = tk.Label(topbar, text= "HISTORY", font=("Helvetica", 15,"bold"), bg="gray60", fg="white")
        pagelabel.place(x=85,y=5)
        
        ##Pics
        
        self.prof1 = PhotoImage(file="bg3a.png", master=self)
        self.prof2 = PhotoImage(file="bg3b.png", master=self)
        self.prof3 = PhotoImage(file="bg3c.png", master=self)
        self.prof4 = PhotoImage(file="bg6a.png", master=self)
        self.prof5 = PhotoImage(file="bg6b.png", master=self)
        self.prof6 = PhotoImage(file="bg6c.png", master=self)
        self.prof7 = PhotoImage(file="bg6d.png", master=self)
        self.prof = PhotoImage(file="gg.png", master=self)
        self.picps = PhotoImage(file="pettt.png", master=self) 
        self.home = PhotoImage(file="home.png", master=self) 
        self.histo = PhotoImage(file="histo.png", master=self) 
        self.cust = PhotoImage(file="borrow.png", master=self) 
        self.out = PhotoImage(file="logout.png", master=self) 
        self.whiapp = PhotoImage(file="whiapp.png", master=self) 
        self.whipet = PhotoImage(file="whipet.png", master=self)
        self.whiexit = PhotoImage(file="whiexit.png", master=self)
        self.btna = PhotoImage(file="j.png", master=self) 
        
        
        app_pl1 = tk.Label(self, image = self.prof1, bd=0, bg="gray60")
        app_pl1.place(x=340,y=5)
        
        app_pl2 = tk.Label(self, image = self.prof2, bd=0, bg="gray60")
        app_pl2.place(x=470,y=1)
        
        app_pl3 = tk.Label(self, image = self.prof3, bd=0, bg="gray60")
        app_pl3.place(x=590,y=1)
        
        app_pl4 = tk.Label(self, image = self.prof4, bd=0, bg="gray60")
        app_pl4.place(x=270,y=760)
        
        app_pl5 = tk.Label(self, image = self.prof5, bd=0, bg="gray60")
        app_pl5.place(x=520,y=750)
        
        app_pl6 = tk.Label(self, image = self.prof6, bd=0, bg="gray60")
        app_pl6.place(x=800,y=750)
        
        app_pl7 = tk.Label(self, image = self.prof7, bd=0, bg="gray60")
        app_pl7.place(x=1075,y=760)
        
        app_pl8 = tk.Label(self, image = self.prof4, bd=0, bg="gray60")
        app_pl8.place(x=1350,y=760)
        
        app_pl = tk.Label(topbar, image = self.histo, bd=0, bg="gray60")
        app_pl.place(x=50,y=0)
        
        app_ps = tk.Label(leftbar, image = self.picps, bd=0, bg="grey13")
        app_ps.place(x=20,y=50)
        
        app_home = tk.Label(leftbar, image = self.home, bd=0, bg="grey13")
        app_home.place(x=6,y=410)
        
        app_histo = tk.Label(leftbar, image = self.histo, bd=0, bg="grey13")
        app_histo.place(x=6,y=610)
        
        app_cust = tk.Label(leftbar, image = self.cust, bd=0, bg="grey13")
        app_cust.place(x=6,y=510)
        
        app_out = tk.Label(leftbar, image = self.out, bd=0, bg="grey13")
        app_out.place(x=6,y=660)
        
        app_whiapp = tk.Label(leftbar, image = self.whiapp, bd=0, bg="grey13")
        app_whiapp.place(x=6,y=460)
        
        app_whipet = tk.Label(leftbar, image = self.whipet, bd=0, bg="grey13")
        app_whipet.place(x=6,y=560)
        
        app_whiexit = tk.Label(leftbar, image = self.whiexit, bd=0, bg="grey13")
        app_whiexit.place(x=6,y=710)
        
        app_prof = tk.Label(leftbar, image = self.prof, bd=0, bg= "grey13")
        app_prof.place(x=45,y=190)
        
        ##Functions for logout and Exit
        
        def logout():
            iExit = tkinter.messagebox.askyesno("Pet Shop Management Sysytem","Do you want to log-out?")
            if iExit > 0:
                
                controller.show_frame(LoginPage)
                #setoffline()
                conn.commit()
                conn.close()
                
        def ExitApplication():
            MsgBox = tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
            if MsgBox == 'yes':
                #logout()
                app.destroy()
            else:
                tk.messagebox.showinfo('Return','You will now return to the application screen')
        
        def Current_User():
            conn = sqlite3.connect("PSMS.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM user WHERE login = 'Online'")
            row = cur.fetchall()
            for i in row:
                #print(i)
                c_user.set(i[0])
            self.usera = Label(self, font=("Helvetica", 20),textvariable = c_user, bg ="grey13", fg = "white")
            self.usera.place(x=75,y=350)
            self.after(1000,Current_User)
            conn.commit()            
            conn.close()
            
        
        ##leftbar buttons
        Button1 = tk.Button(leftbar, text="HOME", font=("Courier", 18), bd=0, bg="grey13", fg="white", command= lambda: controller.show_frame(HomePage))
        Button1.place(x=40,y=410)
        
        Button2 = tk.Button(leftbar, text="APPOINTMENTS", font=("Courier", 18), bd=0, bg="grey13", fg="white", command= lambda: controller.show_frame(AddPage))
        Button2.place(x=40,y=460)
        
        Button3 = tk.Button(leftbar, text="CUSTOMER", font=("Courier", 18), bd=0, bg="grey13", fg="white", command= lambda: controller.show_frame(customerPage))
        Button3.place(x=40,y=510)
        
        Button4 = tk.Button(leftbar, text="PETS", font=("Courier", 18), bd=0, bg="grey13", fg="white", command= lambda: controller.show_frame(PetPage))
        Button4.place(x=40,y=560)
        
        Button5 = tk.Button(leftbar, text="HISTORY", font=("Courier", 18), bd=0, bg="grey13", fg="white", command= lambda: controller.show_frame(history))
        Button5.place(x=40,y=610)
        
        Button6 = tk.Button(leftbar, text="LOG-OUT", font=("Courier", 18), bd=0, bg="grey13", fg="white", command= logout)
        Button6.place(x=40,y=660)
        
        Button7 = tk.Button(leftbar, text="EXIT", font=("Courier", 18), bd=0, bg="grey13", fg="white", command=ExitApplication)
        Button7.place(x=40,y=710)
        
        
        

        #Treeview
        style = ttk.Style(self)
        style.configure("Treeview",
            background = "silver",
            foreground = "black",
            fieldbackground = "silver"
            )
        style.map('Treeview',background=[('selected','deep sky blue')])
        scroll_y=Scrollbar(self, orient=VERTICAL)

        self.tree = ttk.Treeview(self, height=10, columns=("AppointmentID", "Appointment_details", "Status","Appointment_Date","CustomerID","Appointment_Time"), \
            yscrollcommand=scroll_y.set)
            

        self.tree.heading("AppointmentID", text="Appointment ID")
        self.tree.heading("Appointment_details", text="Details")
        self.tree.heading("Status", text="Status")
        self.tree.heading("Appointment_Date", text="Date")
        self.tree.heading("CustomerID", text="Customer ID")
        self.tree.heading("Appointment_Time", text="Time")
        self.tree['show'] = 'headings'


        self.tree.column("AppointmentID", width=150)
        self.tree.column("Appointment_details", width=300)
        self.tree.column("Status", width=100)
        self.tree.column("Appointment_Date", width=100)
        self.tree.column("CustomerID", width=100)
        self.tree.column("Appointment_Time", width=100)

        self.tree.place(x=300,y=175,width=1000,height=560)


        def display1():
            self.tree.tag_configure('oddrow',background="white")
            self.tree.tag_configure('evenrow',background="silver")
            for i in self.tree.get_children():
                self.tree.delete(i)
            conn = sqlite3.connect("PSMS.db")
            cur= conn.cursor()
            cur.execute("PRAGMA foreign_keys = ON")
            cur.execute("SELECT * FROM History ")
            conn.commit()
            rows = cur.fetchall()
            count=0
            for row in rows:
                if count % 2 == 0:
                    self.tree.insert("", tk.END,iid=count,text=f'{count + 1}', values=(row[0],row[1],row[2],row[3],row[4],row[5]), tags=('evenrow',))
                else:
                    self.tree.insert("", tk.END,iid=count,text=f'{count + 1}', values=(row[0],row[1],row[2],row[3],row[4],row[5]), tags=('oddrow',))
                count +=1
            conn.commit()
            conn.close()
        #display()


        def search():
            for i in self.tree.get_children():
                self.tree.delete(i)
            conn=sqlite3.connect('PSMS.db')
            cur=conn.cursor()
            cur.execute("SELECT * FROM Appointment WHERE username != '-' AND company_name != '-' ")
            item=cur.fetchall()
            for m in item:
                n = m[6]#NAME
                cur.execute("SELECT * FROM user WHERE username = ?",(n,))
                userrow = cur.fetchall()
                for k in userrow:
                    role = k[2]
                    if role == k[2]:#role
                        cur.execute("SELECT * FROM user WHERE role = ? AND username = ?",(role,n))
                        row = cur.fetchall()
                        for c in row:
                            c_name = c[3]

            search = self.SearchBar.get()
            conn=sqlite3.connect("PSMS.db")
            cur=conn.cursor()
            cur.execute("SELECT * FROM History WHERE company_name = ?",(c_name,))
            rows=cur.fetchall()
            
            for row in rows:
                if row[0].startswith(search) or row[1].startswith(search) or row[2].startswith(search) or row[3].startswith(search) or row[4].startswith(search):
                    self.tree.insert("", tk.END, values=(row[0],row[1],row[2],row[3],row[4],row[5]))

            conn.close()
                
        self.SearchBar = Entry(self, font=("Courier", 14), textvariable=SearchBar_Var, width=47,bg="snow",fg="grey23")
        self.SearchBar.place(x=600,y=140)
        self.SearchBar.insert(0,'Search here')

        self.btnsearch = tk.Button(self, image=self.btna, bd=0, bg="white",command=search)
        self.btnsearch.place(x=1130,y=140)
        self.btnsearch.config(cursor= "hand2")

        self.btnrefresh = tk.Button(self, text="Refresh",font=("Courier", 14), bd=0,command=display1,bg="gray50",fg="white",width = 8)
        self.btnrefresh.place(x=330,y=140)
        self.btnrefresh.config(cursor= "hand2")
        Current_User()
        display1()
           
app = Application()
app.mainloop() 
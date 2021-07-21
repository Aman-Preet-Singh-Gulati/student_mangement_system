from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from tkinter import filedialog
import mysql.connector
import time


class Student:
    def __init__(self, root):
        # Setting up the Window of Tkinter GUI
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1320x760+110+15")
        self.root.config(background="#0f0f0f")
        
        # App Icon
        # self.icon = PhotoImage(file="student1.png")
        # self.root.tk.call('wm','iconphoto',self.root._w, self.icon)
        self.root.iconbitmap("student1.ico")


        #Adding Menu Bar

        self.subMenu = Menu(menubar,tearoff = 0)
        menubar.add_cascade(label="Help",menu=self.subMenu)
        self.subMenu.add_command(label="About this app",command=self.about_us)
        self.subMenu.add_command(label="GUIDE (how to use)",command = self.rules)
        self.subMenu.add_command(label="Delete Complete Data",command = self.delete_everything)
        self.subMenu.add_command(label="Exit",command = self.quit)


        self.mode_menu = Menu(menubar,tearoff = 0)
        menubar.add_cascade(label="View",menu=self.mode_menu)
        self.mode_menu.add_command(label="Dark Mode",command=self.night_on)
        self.mode_menu.add_command(label="Light Mode",command = self.night_off)



        self.status = Label(root,text="Welcome to Student Management system....",font=("times new roman",20, "bold"),bd=3,bg="black",pady=1,relief=SUNKEN,fg="white")
        self.status.pack(side=BOTTOM,fill=X)

        title = Label(self.root, text= "Student Management System",bd=10,width=39, relief=GROOVE,pady=3,padx=2, font=("times new roman",40, "bold"),bg="#FFD700", fg="#0f0f0f") 
        title.pack(side=TOP,pady=5)
        
        
        # localtime= time.asctime(time.localtime(time.time()))
        # lblinfo = Label(self.root, font=("times new roman",20, "bold"),text=localtime,fg= "#0f0f0f",bd= 10,anchor='w',bg="#FFD700", relief=GROOVE)
        # lblinfo.pack(side=TOP,pady=5)


        # All variables for database
        self.Roll_No_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()

        self.search_by = StringVar()
        self.search_txt = StringVar()

        self.selected = ""


        Manage_Frame = Frame(self.root, bd=5, relief=GROOVE, bg="#0f0f0f")
        Manage_Frame.place(x=20, y=105, width= 470, height=600)

        self.m_title = Label(Manage_Frame, text = "Manage Student",bd=10,bg='#0f0f0f',fg='#FFD700', font=("times new roman",30, "bold"))
        self.m_title.grid(row=0, columnspan=2, pady=5)

        lbl_roll = Label(Manage_Frame, text = "Roll No.",bd=10,bg='#0f0f0f',fg='#FFD700', font=("times new roman",20, "bold"))
        lbl_roll.grid(row=1, column=0, pady=2, padx=20, sticky='w')

        txt_Roll = Entry(Manage_Frame,textvariable=self.Roll_No_var ,font=("times new roman",15, "bold"),bd=7,bg="white",width=22, relief=SUNKEN)
        txt_Roll.grid(row=1, column=1, pady=2, padx=30, sticky='w')

        lbl_name = Label(Manage_Frame, text = "Name",bd=10,bg='#0f0f0f',fg='#FFD700', font=("times new roman",20, "bold"))
        lbl_name.grid(row=2, column=0, pady=2, padx=20, sticky='w')

        txt_name = Entry(Manage_Frame,textvariable=self.name_var,font=("times new roman",15, "bold"),bd=7,bg="white",width=22, relief=SUNKEN)
        txt_name.grid(row=2, column=1, pady=2, padx=30, sticky='w')

        lbl_Email = Label(Manage_Frame, text = "Email",bd=10,bg='#0f0f0f',fg='#FFD700', font=("times new roman",20, "bold"))
        lbl_Email.grid(row=3, column=0, pady=2, padx=20, sticky='w')

        txt_Email = Entry(Manage_Frame,textvariable=self.email_var,font=("times new roman",15, "bold"),bd=7,bg="white",width=22, relief=SUNKEN)
        txt_Email.grid(row=3, column=1, pady=2, padx=30, sticky='w')

        lbl_Gender = Label(Manage_Frame, text = "Gender",bd=10,bg='#0f0f0f',fg='#FFD700', font=("times new roman",20,"bold"))
        lbl_Gender.grid(row=4, column=0, pady=2, padx=20, sticky='w')

        combo_gender = ttk.Combobox(Manage_Frame,textvariable=self.gender_var,width=20,font=("times new roman",16, "bold"),state="readonly")
        combo_gender['values'] = ("Select","Male", "Female", "Other")
        combo_gender.current(0)
        combo_gender.grid(row=4, column=1, pady=2, padx=30, sticky='w')


        lbl_Contact = Label(Manage_Frame, text = "Contact",bd=10,bg='#0f0f0f',fg='#FFD700', font=("times new roman",20, "bold"))
        lbl_Contact.grid(row=5, column=0, pady=2, padx=20, sticky='w')

        txt_Contact = Entry(Manage_Frame,textvariable=self.contact_var,font=("times new roman",15, "bold"),bd=7,bg="white",width=22, relief=SUNKEN)
        txt_Contact.grid(row=5, column=1, pady=2, padx=30, sticky='w')

        lbl_Dob = Label(Manage_Frame, text = "D.O.B",bd=10,bg='#0f0f0f',fg='#FFD700', font=("times new roman",20, "bold"))
        lbl_Dob.grid(row=6, column=0, pady=2, padx=20, sticky='w')

        txt_Dob = Entry(Manage_Frame,textvariable=self.dob_var,font=("times new roman",15, "bold"),bd=7,bg="white",width=22, relief=SUNKEN)
        txt_Dob.grid(row=6, column=1, pady=2, padx=30, sticky='w')

        lbl_Address = Label(Manage_Frame, text = "Address",bd=10,bg='#0f0f0f',fg='#FFD700', font=("times new roman",20, "bold"))
        lbl_Address.grid(row=7, column=0, pady=2, padx=20, sticky='w')

        self.txt_Address = Text(Manage_Frame, width=20, height=3,bd=7,bg="white", font=("", 14,"bold"))
        self.txt_Address.grid(row=7, column=1, pady=2, padx=30, sticky='w')


# Button Frame 

        btn_Frame = Frame(Manage_Frame, relief=GROOVE, bg="#0f0f0f")
        btn_Frame.place(x=5, y=520, width= 450)

        Addbtn = Button(btn_Frame, text = "Add",bd=8,font=("times new roman",14, "bold"),bg="blue" ,padx=1,pady=5,fg="white",width=8,command=self.add_students).grid(row=0,column=0,padx=1,pady=6)
        updatebtn = Button(btn_Frame, text = "Update",bd=8,font=("times new roman",14, "bold"),bg="red",padx=1,pady=5,fg="white", width=8,command=self.update_data).grid(row=0,column=1,padx=1,pady=6)
        deletebtn = Button(btn_Frame, text = "Delete",bd=8,font=("times new roman",14, "bold"),bg="green",padx=1,pady=5,fg="white", width=8,command=self.delete_data).grid(row=0,column=2,padx=1,pady=6)
        Clearbtn = Button(btn_Frame, text = "Clear",bd=8,bg="blue",font=("times new roman",14, "bold"),padx=1,pady=5,fg="white", width=8,command=self.clear).grid(row=0,column=3,padx=1,pady=6)


#Frame 2

        Detail_Frame = Frame(self.root, bd=5, relief=GROOVE, bg="#0f0f0f")
        Detail_Frame.place(x=500, y=105, width= 800, height=600)

        lbl_search = Label(Detail_Frame, text = "Search By",bd=10,bg='#0f0f0f',fg='#FFD700', font=("times new roman",20, "bold"))
        lbl_search.grid(row=0, column=0, pady=2, padx=10, sticky='w')

        self.combo_search = ttk.Combobox(Detail_Frame,textvariable=self.search_by, width=13,font=("times new roman",14, "bold"),state="readonly")
        self.combo_search['values'] = ("Choose","Roll No.", "Name", "Contact", "Email","Gender","D.O.B.","Address")
        self.combo_search.current(0)
        self.combo_search.grid(row=0, column=1, pady=2, padx=10, sticky='w')

        self.txt_Search = Entry(Detail_Frame, textvariable=self.search_txt ,font=("times new roman",14, "bold"),bd=5, relief=GROOVE)
        self.txt_Search.grid(row=0, column=2, pady=2, padx=10, sticky='w')

        searchbtn = Button(Detail_Frame, text = "Search",bd=8,bg="red",fg="white",font=("times new roman",11, "bold"), width=10,pady=3,command=self.search_data).grid(row=0,column=3,padx=1,pady=3)
        showallbtn = Button(Detail_Frame, text = "Show All",bd=8,bg="blue",fg="white",font=("times new roman",11, "bold"), width=10,pady=3,command=self.fetch_data).grid(row=0,column=4,padx=1,pady=3)


# frame 3 Table frame

        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="#0f0f0f")
        Table_Frame.place(x=10, y=70, width= 770, height=520)

        scroll_x = Scrollbar(Table_Frame, orient =HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient =VERTICAL)
        
        self.Student_table = ttk.Treeview(Table_Frame,style="mystyle.Treeview", columns=("roll", "name","email", "gender","contact", "dob", "Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        self.Student_table.tag_configure('odd')
        self.Student_table.tag_configure('even')
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)

        self.Student_table.heading("roll",text="Roll No.")
        self.Student_table.heading("name",text="Name")
        self.Student_table.heading("email",text="Email")
        self.Student_table.heading("gender",text="Gender")
        self.Student_table.heading("contact",text="Contact")
        self.Student_table.heading("dob",text="D.O.B")
        self.Student_table.heading("Address",text="Address")

        self.Student_table['show']= 'headings'
        self.Student_table.column("roll", width=100)
        self.Student_table.column("name", width=160)
        self.Student_table.column("email", width=160)
        self.Student_table.column("gender", width=100, anchor='center')
        self.Student_table.column("contact", width=150, anchor='center')
        self.Student_table.column("dob", width=100)
        self.Student_table.column("Address", width=150)

        self.Student_table.pack(fill=BOTH,expand=1)

        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()

    def add_students(self):
        op = tkinter.messagebox.askyesno('Adding selected data','Do you really wanna Add selected data to your DATABASE')
        if op>0:
                if self.Roll_No_var.get()=="" or self.name_var.get()=="" or self.email_var.get()=="" or self.contact_var.get()=="" or self.gender_var.get()=="" or self.dob_var.get()=="":  #or self.txt_Address.get('1.0')==""
                        tkinter.messagebox.showerror("Error","You have not given the complete data to database !!!")
                        self.status['text'] = "Please fill all the required fields!"
                else:
                        #conn = pymysql.connect(host="localhost", user="root", password="", database="stm")
                        conn = mysql.connector.connect(host='localhost', user='root', password='1234',database='stm')
                        cur = conn.cursor()
                        cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(
                                self.Roll_No_var.get(),
                                self.name_var.get(),
                                self.email_var.get(),
                                self.gender_var.get(),
                                self.contact_var.get(),
                                self.dob_var.get(),
                                self.txt_Address.get('1.0',END)
                                ))
                        conn.commit()
                        self.fetch_data()
                        tkinter.messagebox.showinfo("Added","New record has been added to database!!!")
                        self.clear()
                        conn.close()
                        self.status['text'] = "New DataBase has been added!"

    def fetch_data(self):
        self.status['text'] = "Database has been Retrieved!"
        conn = mysql.connector.connect(host='localhost', user='root', password='1234',database='stm')
        cur = conn.cursor()
        cur.execute("select * from students")
        rows = cur.fetchall()
        if len(rows) != 0:
                self.Student_table.delete(*self.Student_table.get_children())
                for row in rows:
                        self.Student_table.insert('',END,values=row)
                conn.commit()
        conn.close()

    def clear(self):

        self.status['text'] = "Data has been cleared!"
        self.Roll_No_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt_Address.delete("1.0",END)
        tkinter.messagebox.showinfo("Cleared","Entry Fields has been cleared !!")

    
    def get_cursor(self,ev):
        self.status['text'] = "DataBase has been Selected!"
        cursor_row = self.Student_table.focus()
        contents = self.Student_table.item(cursor_row)
        row = contents['values']
        print(row)
        self.Roll_No_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_Address.delete("1.0",END)
        self.txt_Address.insert(END,row[6])
    
    def update_data(self):
        op = tkinter.messagebox.askyesno('Updating selected data','Do you really wanna update selected data to your DATABASE')
        if op>0:
                if self.Roll_No_var.get()=="" or self.name_var.get()=="" or self.email_var.get()=="" or self.contact_var.get()=="" or self.gender_var.get()=="" or self.dob_var.get()=="":
                        tkinter.messagebox.showerror("Error","You have not given the complete data to database !!!")
                        self.status['text'] = "Please fill all the required fields!"
                #conn = pymysql.connect(host="localhost", user="root", password="", database="stm")
                else:
                        conn = mysql.connector.connect(host='localhost', user='root', password='1234',database='stm')
                        cur = conn.cursor()
                        cur.execute("update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s",(
                                self.name_var.get(),
                                self.email_var.get(),
                                self.gender_var.get(),
                                self.contact_var.get(),
                                self.dob_var.get(),
                                self.txt_Address.get('1.0',END),
                                self.Roll_No_var.get()
                                ))
                        conn.commit()
                        self.fetch_data()
                        tkinter.messagebox.showinfo("Updated","Record has been Updated to database!!!")
                        self.clear()
                        conn.close()
                        self.status['text'] = "DataBase has been Updated!"
    
    def delete_data(self):
        op = tkinter.messagebox.askyesno('Deleting selected data','Do you really wanna delete selected data from your DATABASE')
        if op>0:
                if self.Roll_No_var.get()=="" or self.name_var.get()=="" or self.email_var.get()=="" or self.contact_var.get()=="" or self.gender_var.get()=="" or self.dob_var.get()=="":
                        tkinter.messagebox.showerror("Error","You have not given the complete data to database !!!")
                        self.status['text'] = "Please fill all the required fields!"
                else:
                        conn = mysql.connector.connect(host='localhost', user='root', password='1234',database='stm')
                        cur = conn.cursor()
                        value = self.Roll_No_var.get()
                        query = "delete from students where roll_no=%s"
                        # cur.execute("delete from students where roll_no=(%s)",self.Roll_No_var.get())
                        cur.execute(query,(value,))
                        conn.commit()
                        conn.close()
                        tkinter.messagebox.showinfo("Deleted","Record has been Deleted from database!!!")
                        self.status['text'] = "Selected database has been Deleted!" 
                        self.fetch_data()
                        self.clear()
                        self.status['text'] = "Selected database has been Deleted!" 

    def night_on(self):
            main_color = "#000000"
            second_color = "#373737"
            text_color = "green"
            white = "white"

            self.root.config(bg=main_color)
            self.status.config(bg=main_color, fg=text_color)
            self.m_title.config(fg=second_color)
            self.subMenu.config(bg=main_color)
            self.mode_menu.config(bg=main_color)
            self.subMenu.config(fg=white)
            self.mode_menu.config(fg=white)

    def night_off(self):
            self.root.config(background="#0f0f0f")
            self.status.config(bg="black", fg="white")
            self.m_title.config(fg="#FFD700")
            self.subMenu.config(bg="white")
            self.mode_menu.config(bg="white")
            self.subMenu.config(fg="black")
            self.mode_menu.config(fg="black")


    def about_us(self):
        tkinter.messagebox.showinfo('About Student Management System ','This is an application for Managing Data of Students \n\nMade by : Aman Preet Singh Gulati')
    
    def delete_everything(self):
        #tkinter.messagebox.showinfo('About CryptoCHARM ','This is a application for encoding and decoding THE MESSAGE  \n\n Follow the steps to operate with this application EFFECTIVELY!\n\n1. Enter the MESSAGE which is to be encoded or decoded\n2. Enter the SECRET KEY\n3. Enter E for encoding message or D for decoding message in small alphabets\n4. Then click on OUTPUT BUTTON ,your result will be shown in result entry block ')
        op = tkinter.messagebox.askyesno('Delete complete Database','Do you really wanna delete complete data from your DATABASE')
        if op>0:
                conn = mysql.connector.connect(host='localhost', user='root', password='1234',database='stm')
                cur = conn.cursor()
                cur.execute("TRUNCATE TABLE students")
                conn.close()
    
    def quit(self):
        op = tkinter.messagebox.askyesno("Exit", "Do you really wanna Exit ?")
        if op>0:
            self.status['text'] = "You are quitting with this application"
            self.root.destroy()
    
    def rules(self):
        tkinter.messagebox.showinfo('Guide to folllow..','1. PRESS "Add" for adding new entry to database\n\n2. PRESS "Update" for updating previous entry to database\n\n3. PRESS "Delete" for deleting selected entry from database\n\n4. PRESS "Clear" for clearing existing entry from Entry fields\n\n5. There is status bar at the bottom to make user aware about what is going on \n\n6. There is "SEARCH" option from where user can select the parameter from dropdown menu and search according to that \n\n7. PRESS "Show All" for Retrieving Complete data\n\n8. SELECT "Delete Complete Data" for deleting all the data forever from database\n')
    
     
    def search_data(self):
        present = "no"
        conn = mysql.connector.connect(host='localhost', user='root', password='1234',database='stm')
        cur = conn.cursor()
        print("connected")
        sql=""
        self.selected = self.combo_search.get()
        if self.selected == "Choose":
                print("Search")
        if self.selected == "Roll No.":
                sql = "SELECT * FROM students WHERE roll_no=%s"
                #print("Search1111")
        if self.selected == "Name":
                sql = "SELECT * FROM students WHERE name=%s"
                #print("Search2222")
        if self.selected == "Contact":
                sql = "SELECT * FROM students WHERE contact=%s"
                #print("Search3333")
        if self.selected == "Gender":
                sql = "SELECT * FROM students WHERE gender=%s"
        if self.selected == "Email":
                sql = "SELECT * FROM students WHERE email=%s"
        if self.selected == "Address":
                sql = "SELECT * FROM students WHERE address=%s"
        if self.selected == "D.O.B.":
                sql = "SELECT * FROM students WHERE dob=%s"

        #conn = mysql.connector.connect(host='localhost', user='root', password='1234',database='stm')
        # cur = conn.cursor()
        searched = self.txt_Search.get()
        print(searched)
        name = (searched,)

        #cur.execute("select * from students where"+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        r = cur.execute(sql,name)
        print(type(r))

        rows = cur.fetchall()
        
        if len(rows) != 0:
                self.Student_table.delete(*self.Student_table.get_children())
                present = "yes"
                for row in rows:
                        self.Student_table.insert('',END,values=row)
        conn.commit()
        conn.close()
        
        self.status['text'] = "DataBase has been Searched!"

        if present == "no":
                self.status['text'] = "The data you searched is not present in Database"
                tkinter.messagebox.showerror("Error","The data you searched is not present in Database")


                
root = Tk()
# icon = PhotoImage(file="student1.png")
# root.tk.call('wm','iconphoto',root._w, icon)
menubar = Menu(root)
root.config(menu=menubar)

subMenu = Menu(menubar,tearoff = 0)
# def browse_file():
#     global filename
#     filename = filedialog.askopenfilename()


# menubar.add_cascade(label="File",menu=subMenu)
# subMenu.add_command(label="Open",command= browse_file)


style = ttk.Style()
style.theme_use("clam")
style.configure("mystyle.Treeview", highlightthickness=10, bd=0, font=('Calibri', 12)) #fieldbackground="#252726",
# Modify the font of the body
style.configure("mystyle.Treeview.Heading", font=('Calibri', 14,'bold')) # Modify the font of the headings
style.configure("Treeview", background="#252726", foreground="#ffffff")
ob = Student(root)
root.resizable(width=False, height=False)
root.mainloop()
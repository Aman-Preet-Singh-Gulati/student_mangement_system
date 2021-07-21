from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

class Register:
    def __init__(self,root):
        self.root = root
        self.root.title("Registration Window")
        self.root.geometry("1280x700+130+40")
        self.root.config(bg="brown")


        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        subMenu = Menu(menubar,tearoff = 0)
        menubar.add_cascade(label="Help",menu=subMenu)
        subMenu.add_command(label="Exit/Quit",command=self.exit)

        # Add icon
        # self.icon = PhotoImage(file="student3.png")
        # self.root.tk.call('wm','iconphoto',root._w, self.icon)
        self.root.iconbitmap("student1.ico")


    
        # self.bg = ImageTk.PhotoImage(file="car_background2.jpg")
        bg = Label(self.root,bg="#0f0f0f",relief=RAISED,bd=15)
        bg.place(x=250,y=0,relwidth=1,relheight=1)

        self.left = ImageTk.PhotoImage(file="student3.png")
        left = Label(self.root,image=self.left,bg="black",relief=RAISED,bd=15)
        left.place(x=80,y=100,width=400,height=500)
        left2 = Label(self.root,text="Already have an account?",bg="black",fg="white",font=("times new roman",20,"bold"))
        left2.place(x=120,y=170)

        frame1 = Frame(self.root,bg="#FFFF66",relief=RAISED,bd=10)
        frame1.place(x=480,y=100,width=700,height=500)

        self.top = Label(root,text="Welcome to Registration System",font=("times new roman",25, "bold"),bd=10,bg="black",pady=10,relief=RAISED,fg="white")
        self.top.pack(side=TOP,fill=X)

        self.status = Label(root,text="This will register you to for Student Management System",font=("times new roman",20, "bold"),bd=7,bg="black",pady=3,relief=SUNKEN,fg="white")
        self.status.pack(side=BOTTOM,fill=X)


        title = Label(frame1,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="brown",pady=3,fg="white",bd=7,relief=RAISED)
        title.place(x=50,y=30,width=570)

        f_name = Label(frame1,text="First Name",font=("times new roman",15,"bold"),bg="#FFFF66",fg="black")
        f_name.place(x=50,y=100)
        self.txt_fname = Entry(frame1,font=("times new roman",15),bg="powder blue",bd=5,relief=SUNKEN)
        self.txt_fname.place(x=50,y=130,width=250)

        l_name = Label(frame1,text="Last Name",font=("times new roman",15,"bold"),bg="#FFFF66",fg="black")
        l_name.place(x=370,y=100)
        self.txt_lname = Entry(frame1,font=("times new roman",15),bg="powder blue",bd=5,relief=SUNKEN)
        self.txt_lname.place(x=370,y=130,width=250)

        contact = Label(frame1,text="Contact No.",font=("times new roman",15,"bold"),bg="#FFFF66",fg="black")
        contact.place(x=50,y=170)
        self.txt_contact = Entry(frame1,font=("times new roman",15),bg="powder blue",bd=5,relief=SUNKEN)
        self.txt_contact.place(x=50,y=200,width=250)

        email = Label(frame1,text="Email",font=("times new roman",15,"bold"),bg="#FFFF66",fg="black")
        email.place(x=370,y=170)
        self.txt_email = Entry(frame1,font=("times new roman",15),bg="powder blue",bd=5,relief=SUNKEN)
        self.txt_email.place(x=370,y=200,width=250)

        question = Label(frame1,text="Security Question",font=("times new roman",15,"bold"),bg="#FFFF66",fg="black")
        question.place(x=50,y=240)
        self.cmb_question = ttk.Combobox(frame1,font=("times new roman",13),state="readonly",justify=CENTER)
        self.cmb_question['values'] = ("Select","Your First Pet Name","Your Birth Place","Your Best Friend Name")
        self.cmb_question.place(x=50,y=270,width=250)
        self.cmb_question.current(0)

        answer = Label(frame1,text="Answer",font=("times new roman",15,"bold"),bg="#FFFF66",fg="black")
        answer.place(x=370,y=240)
        self.txt_answer = Entry(frame1,font=("times new roman",15),bg="powder blue",bd=5,relief=SUNKEN)
        self.txt_answer.place(x=370,y=270,width=250)

        
        password = Label(frame1,text="Password",font=("times new roman",15,"bold"),bg="#FFFF66",fg="black")
        password.place(x=50,y=310)
        self.txt_password = Entry(frame1,font=("times new roman",15),bg="powder blue",bd=5,relief=SUNKEN)
        self.txt_password.place(x=50,y=340,width=250)

        cpassword = Label(frame1,text="Confirm Password",font=("times new roman",15,"bold"),bg="#FFFF66",fg="black")
        cpassword.place(x=370,y=310)
        self.txt_cpassword = Entry(frame1,font=("times new roman",15),bg="powder blue",bd=5,relief=SUNKEN)
        self.txt_cpassword.place(x=370,y=340,width=250)

        self.var_chk = IntVar()
        chk = Checkbutton(frame1,text="I Agree to all the Terms & Conditions",variable=self.var_chk,bg="#FFFF66",onvalue=1,offvalue=0,font=("times new roman",12))
        chk.place(x=50,y=380)

        self.btn_register = Button(frame1,command=self.register_data,text="-- Register Now --",cursor="hand2",bg="brown",fg="white",bd=7,width=20,font=("times new roman",15,"bold"))
        self.btn_register.place(x=50,y=420)

        self.btn_register = Button(frame1,command=self.exit,text="-- Exit --",cursor="hand2",bg="brown",fg="white",bd=7,width=19,font=("times new roman",15,"bold"))
        self.btn_register.place(x=370,y=420)

        self.btn_login = Button(self.root,text="Sign In",cursor="hand2",bg="red",fg="white",width=13,bd=10,font=("times new roman",18,"bold"),command=self.login_window)
        self.btn_login.place(x=180,y=480)

    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.cmb_question.current(0)
        self.txt_answer.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_cpassword.delete(0,END)

    def exit(self):
        ask = messagebox.askyesno("Exit/Quit","Do you really wanna Quit/Exit")
        if ask>0:
            self.root.destroy()
        else:
            return

    def login_window(self):
        self.root.destroy()
        import stmLogin

    def register_data(self):
        #print(self.var_fname.get(),self.txt_lname.get())

        if self.txt_fname.get()=="" or self.txt_email.get()=="" or self.cmb_question.get()=="Select" or self.txt_answer.get()=="" or self.txt_password.get()=="" or self.txt_cpassword.get()=="": 
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        elif self.txt_password.get() != self.txt_cpassword.get():
            messagebox.showerror("Error","Password should be matched",parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error","First agree to our terms and conditions",parent=self.root)
        else:
            # messagebox.showinfo("Success","Registration Successfull",parent=self.root)
            # self.txt_lname.get(),
            # self.txt_contact.get(),
            # self.txt_email.get(),
            # self.cmb_question.get(),
            # self.txt_answer.get(),
            # self.txt_password.get(),
            # self.txt_cpassword.get())   
            try:
                con = mysql.connector.connect(host='localhost', user='root', password='1234',database='stm')
                cur = con.cursor()
                # cur.execute("select * from employee where email=%s",self.txt_email.get())
                # row = cur.fetchone()
                # print(row)
                # if row!=None:
                #     messagebox.showinfo("Error","User is already registered",parent=self.root)    

                # else:
                cur.execute("insert into employee (f_name,l_name,contact,email,question,answer,password) values(%s,%s,%s,%s,%s,%s,%s)",
                            (self.txt_fname.get(),
                            self.txt_lname.get(),
                            self.txt_contact.get(),
                            self.txt_email.get(),
                            self.cmb_question.get(),
                            self.txt_answer.get(),
                            self.txt_password.get()
                            ))
                con.commit()
                con.close()
                messagebox.showinfo("Success","Successfully Registered",parent=self.root) 
                self.clear()   


            except Exception as es: 
                messagebox.showerror("Error",f"Error due to {str(es)}",parent=self.root)    



root = Tk()
obj=Register(root)
root.resizable(width=False, height=False)
root.mainloop()
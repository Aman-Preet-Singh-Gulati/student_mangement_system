from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import os
import subprocess
import mysql.connector

class Login_system:
    def __init__(self,root):
        # self.path = path
        self.root = root
        self.root.title("Login Window")
        self.root.geometry("800x663+360+60")
        self.root.configure(bg="#0f0f0f")

        subMenu = Menu(menubar,tearoff = 0)
        menubar.add_cascade(label="Help",menu=subMenu)
        subMenu.add_command(label="Exit/Quit",command=self.exit)

        # self.bg_icon = ImageTk.PhotoImage(file="c10.jpg")
        self.user_icon = PhotoImage(file="lock.png")
        self.pass_icon = PhotoImage(file="lock.png")
        self.logo_icon = PhotoImage(file="student6.png")


        self.uname = StringVar()
        self.passname = StringVar()

        # bg_lbl = Label(self.root, image=self.bg_icon).pack()
        # icon = PhotoImage(file="student1.png")
        # root.tk.call('wm','iconphoto',root._w, icon)
        self.root.iconbitmap("student1.ico")


        self.status = Label(self.root,text="Login System for redirecting to Student Management System",font=("times new roman",20, "bold"),bd=3,bg="black",pady=3,relief=SUNKEN,fg="white")
        self.status.pack(side=BOTTOM,fill=X)

        title = Label(self.root, text="Login System", font = ('times new roman',40,'bold'),bd=10,pady=5,bg='#FFD700',fg='#0f0f0f',relief=GROOVE)
        title.place(x=0,y=0,relwidth=1)

        Login_Frame = Frame(self.root, bg="black",bd=10,relief=GROOVE)
        Login_Frame.place(x=150,y=120)
        logolbl = Label(Login_Frame, image=self.logo_icon,bd=0)
        logolbl.grid(row=0,columnspan=2,pady=20)

        lbluser = Label(Login_Frame, text=" Username", image=self.user_icon,compound=LEFT,font = ('times new roman',20,'bold'),bg="black",fg="#FFD700")
        lbluser.grid(row=1,column=0,padx=20,pady=10)
        self.txtuser = Entry(Login_Frame, bd=5, relief = SUNKEN,textvariable=self.uname, font=("",15))
        self.txtuser.grid(row=1,column=1,padx=20)

        lblpass = Label(Login_Frame, text=" Password", image=self.pass_icon,compound=LEFT,font = ('times new roman',20,'bold'),bg="black",fg="#FFD700")
        lblpass.grid(row=2,column=0,padx=20,pady=10)
        self.txtpass = Entry(Login_Frame, bd=5,show="*", relief = SUNKEN,textvariable=self.passname, font=("",15))
        self.txtpass.grid(row=2,column=1,padx=20)

        btn_log = Button(Login_Frame, text="Login",width=27,bd=12, font=("times new roman",18,"bold"),bg='#FFD700',fg='#0f0f0f',command=self.login)
        btn_log.grid(row=3,columnspan=2,pady=20)
        btn_reg = Button(self.root, text="Don't have an Account?", font=("times new roman",16,"bold"),bg='red',fg='white',bd=9,command=self.register_window)
        btn_reg.place(x=265,y=550)

    def register_window(self):
        self.root.destroy()
        import register

    def login(self):
        if self.uname.get()=="" or self.passname.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                con = mysql.connector.connect(host='localhost', user='root', password='1234',database='stm')
                cur = con.cursor()
                cur.execute("select * from employee where email=%s and password=%s",(self.uname.get(),self.passname.get()))
                row = cur.fetchone()
                print(row)
                if row==None:
                    messagebox.showerror("Error","You dont have an account",parent=self.root)

                else:
                    messagebox.showinfo("Success","Welcome",parent=self.root)
                    self.root.destroy()
                    import stmlog

                con.close()

            except Exception as es:
                messagebox.showerror("Error",f"Error Due to :{str(es)}",parent=self.root)


        # if self.uname.get()=="" and self.passname.get()=="":
        #    self.status['text'] = "Both Fields are required"
        #    messagebox.showerror("Error","Both Fields are required")

        # elif self.uname.get()=="":
        #    self.status['text'] = "Username Field is required"
        #    messagebox.showerror("Error","Username Field is required") 
        
        # elif self.passname.get()=="":
        #    self.status['text'] = "Password Field is required"
        #    messagebox.showerror("Error","Password Field is required")

        # elif self.uname.get()=="Aman" and self.passname.get()=="1234":
        #     self.status['text'] = f"Welcome : {self.uname.get()}"
        #     messagebox.showinfo("Successful",f"Welcome : {self.uname.get()} \nNow you will be redirected to Student Management System")
        #     # os.system('python media.py')
        #     # # OR.....
        #     # subprocess.call([r'D:\python\jarvis\__pycache__\stm_batch.bat'])
        #     self.root.destroy()
        #     import stm_with_log
        #     stm_with_log.Student()
        #     self.uname.set("")
        #     self.passname.set("")
        #     self.status['text'] = "Login System for redirecting to Student Management System"
        
        # elif self.uname.get()!="Aman":
        #     self.status['text'] = "Invalid Username"
        #     messagebox.showerror("Error","Invalid Username")
        
        # elif self.passname.get()!="1234":
        #     self.status['text'] = "Invalid Password"
        #     messagebox.showerror("Error","Invalid Password")
        
        # elif self.uname.get()!="Aman" and self.passname.get()!="1234":
        #     self.status['text'] = "Invalid Username and Password"
        #     messagebox.showerror("Error","Invalid Username and Password")



    def exit(self):
        ask = messagebox.askyesno("Exit/Quit","Do you really wanna Quit/Exit")
        if ask>0:
            self.root.destroy()
        else:
            return

        

root = Tk()
menubar = Menu(root)
root.config(menu=menubar)
obj = Login_system(root)
root.resizable(width=False, height=False)
root.mainloop()

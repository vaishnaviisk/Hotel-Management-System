from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import random
import time
import datetime
import mysql.connector
from Hotel import HotelManagementSystem


def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1500x800+0+0") 

        self.var_passward=StringVar()
        self.var_cpassward=StringVar()
        self.var_security=StringVar()
        self.var_securityans=StringVar()
        self.var_newpassward=StringVar()

        # img=Image.open(r"C:\Hotel Management system\images\Hotel.jpg")
        # img=img.resize((800,1800))
        self.bg=ImageTk.PhotoImage(file=r"C:\Hotel Management system\images\Login Hotel.jpg")
        
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="white")
        frame.place(x=500,y=150,width=300,height=400)

        img1=Image.open(r"C:\Hotel Management system\images\Username logo.jpg")
        img1=img1.resize((80,80),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="white",borderwidth=0)
        lblimg1.place(x=610,y=150,width=80,height=80)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="black",bg="white")
        get_str.place(x=85,y=80)

        # #label
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="black",bg="white")
        username.place(x=40,y=130)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=160,width=230)

        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="black",bg="white")
        password.place(x=40,y=200)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=230,width=230)
        
        #Login Button
        loginbtn=Button(frame,text="Login",command=self.login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="brown")
        loginbtn.place(x=100,y=280,width=120,height=35) 

        #Register Button
        registerbtn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",10,"bold"),border=0,fg="black",bg="white",activeforeground="white",activebackground="brown")
        registerbtn.place(x=30,y=330,width=120)

        #Forgot Password
        forgotbtn=Button(frame,text="Forgot Password",command=self.forgot_passward_window,font=("times new roman",10,"bold"),border=0,fg="black",bg="white",activeforeground="white",activebackground="brown")
        forgotbtn.place(x=25,y=360,width=120)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if  self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all field required")
        elif self.txtuser.get()=="Varshini" and self.txtpass.get()=="Varshi":
            messagebox.showinfo("Success","Welcome to our Hotel")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Varshmysql?",database="Hotel")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where Email=%s and Password=%s",(self.txtuser.get(),self.txtpass.get()))
            row=my_cursor.fetchone()
            if row==None:
               messagebox.showerror("Error","Invalid Username and Passward")
            else:
                open_main=messagebox.askyesno("YesNo","Access only admin")
                if open_main>0:
                   self.new_window=Toplevel(self.root)
                   self.app=HotelManagementSystem(self.new_window)
                else:
                   if not open_main:
                       return
            conn.commit()
            conn.close()

# Reset Password

    def reset_passward(self):
        if self.combo_security.get()=="Select":
            messagebox.showerror("Error","Select the Security Question",parent=self.root2)
        elif self.txt_securityans.get=="":
            messagebox.showerror("Error","Please enter the Answer",parent=self.root2)
        elif self.txt_new_passward.get=="":
            messagebox.showerror("Error","Please enter the New Passward",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Varshmysql?",database="Hotel")
            my_cursor=conn.cursor()
            query=("select * from register where Email=%s and SecurityQ=%s and SecurityA=%s")
            value=(self.txtuser.get(),self.combo_security.get(),self.txt_securityans)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("error","Please enter the Correct Answer")
            else:
                query=("update register set Password=%s where Email=%s")
                value=(self.txt_new_passward.get(),self.txtuser.get())
                my_cursor.execute(query,value)
                conn.commit()
                conn.close()
                messagebox.showinfo("INFO","New Password has been set Successfully, Please login with New Password",parent=self.root2)
                self.root2.destroy()
                    
                   

    

           #=============forgot passward=============

    def forgot_passward_window(self):
        
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the email address to reset passward")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Varshmysql?",database="Hotel")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            # print(row)
            

            if row==None:
                messagebox.showerror=("Error","Please enter the valid user name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+490+100")

                l=Label(self.root2,text="Forgot passward",font=("times new roman",20),fg="black",bg="white")
                l.place(x=0,y=10,relwidth=1)
                security=Label(self.root2,text="Security Question",font=("times new roman",15),fg="black",bg="white")
                security.place(x=20,y=80)
                self.combo_security=ttk.Combobox(self.root2,textvariable=self.var_security,font=("times new roman",15),state="readonly")
                self.combo_security["values"]=("Select","your birth place","father name","primary school name")
                self.combo_security.place(x=20,y=120,width=250)
                self.combo_security.current(0)



                securityans=Label(self.root2,text="Security Question Answer",font=("times new roman",15),fg="black",bg="white")
                securityans.place(x=20,y=170)
                self.txt_securityans=ttk.Entry(self.root2,textvariable=self.var_securityans,font=("times new roman",15))
                self.txt_securityans.place(x=20,y=210,width=250)

                new_passward=Label(self.root2,text="New password",font=("times new roman",15),fg="black",bg="white")
                new_passward.place(x=20,y=260)
                self.txt_new_passward=ttk.Entry(self.root2,textvariable=self.var_newpassward,font=("times new roman",15))
                self.txt_new_passward.place(x=20,y=300,width=350)

                btn=Button(self.root2,text="Reset",command=self.reset_passward,font=("times new roman",15),fg="white",bg="black")
                btn.place(x=150,y=360)








class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        #==============variables=========
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_password=StringVar()
        self.var_cpassword=StringVar()
        self.var_security=StringVar()
        self.var_securityans=StringVar()
        


        #====back ground image============
        self.bg=ImageTk.PhotoImage(file=r"C:\Hotel Management system\images\Register .jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

#         #=============left image=======
#         self.bg1=ImageTk.PhotoImage(file=r"D:\mini project\Hotel images\thought-good-morning-messages-LoveSove.jpg")
#         left_lbl=Label(self.root,image=self.bg1)
#         left_lbl.place(x=50,y=100,width=470,height=550)

        frame=Frame(self.root,bg="white")
        frame.place(x=320,y=75,width=650,height=500)

        register_lbl=Label(frame,text="Register Here",font=("times new roman",20,"bold"),fg="dark green",bg="white")
        register_lbl.place(x=20,y=20)

        #=============label and entry==========
        fname=Label(frame,text="First Name",font=("times new roman",15),fg="green",bg="white")
        fname.place(x=50,y=100)
        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15))
        fname_entry.place(x=50,y=130,width=250)

        lname=Label(frame,text="Last Name",font=("times new roman",15),fg="green",bg="white")
        lname.place(x=370,y=100)
        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)

        contact=Label(frame,text="Contact no",font=("times new roman",15),fg="green",bg="white")
        contact.place(x=50,y=170)
        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("times new roman",15),fg="green",bg="white")
        email.place(x=370,y=170)
        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)

        

        security=Label(frame,text="Security Question",font=("times new roman",15),fg="green",bg="white")
        security.place(x=50,y=240)
        self.combo_security=ttk.Combobox(frame,textvariable=self.var_security,font=("times new roman",15),state="readonly")
        self.combo_security["values"]=("Select","Your birth place","Father name","Primary School name")
        self.combo_security.place(x=50,y=270,width=250)
        self.combo_security.current(0)



        securityans=Label(frame,text="Security Question Answer",font=("times new roman",15),fg="green",bg="white")
        securityans.place(x=370,y=240)
        self.txt_securityans=ttk.Entry(frame,textvariable=self.var_securityans,font=("times new roman",15))
        self.txt_securityans.place(x=370,y=270,width=250)


        password=Label(frame,text="Password",font=("times new roman",15),fg="green",bg="white")
        password.place(x=50,y=310)
        self.txt_password=ttk.Entry(frame,textvariable=self.var_password,font=("times new roman",15))
        self.txt_password.place(x=50,y=340,width=250)

        cpassword=Label(frame,text="Confirm Password",font=("times new roman",15),fg="green",bg="white")
        cpassword.place(x=370,y=310)
        self.txt_cpassword=ttk.Entry(frame,textvariable=self.var_cpassword,font=("times new roman",15))
        self.txt_cpassword.place(x=370,y=340,width=250)

        self.var_check=IntVar()
        self.checkbtn=Checkbutton(frame,variable=self.var_check,text="I agree the terms and conditions",font=("times new roman",15),onvalue=1,offvalue=0,fg="green",bg="white")
        self.checkbtn.place(x=50,y=380)

        #==========================Register button===========================
        registerbtn=Button(frame,command=self.register_data,text="Register",font=("times new roman",15),bd=3,relief=RIDGE,fg="white",bg="Green",activeforeground="white",activebackground="brown")
        registerbtn.place(x=280,y=430,width=120,height=35) 

      
       

#===================function declaration==============
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_security.get()=="Select":
            messagebox.showerror("error","all fields are required")
        elif self.var_password.get()!=self.var_cpassword.get():
            messagebox.showerror("Error","Password and confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("error","please agree our terms and conditions")
        else:
           conn=mysql.connector.connect(host="localhost",username="root",password="Varshmysql?",database="Hotel")
           my_cursor=conn.cursor()
           query=("select * from register where email=%s")
           value=(self.var_email.get(),)
           my_cursor.execute(query,value)
           row=my_cursor.fetchone()
           if row!=None:
               messagebox.showerror("Error","User already exits,please try another email")
           else:
               my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                      self.var_fname.get(),
                                                                                      self.var_lname.get(),
                                                                                      self.var_contact.get(),
                                                                                      self.var_email.get(),
                                                                                      self.var_security.get(),
                                                                                      self.var_securityans.get(),
                                                                                      self.var_password.get()
                                                                                   ))
               messagebox.showinfo("success","Registered Successfully") 
           conn.commit()
           conn.close() 
           self.root.destroy()


if __name__ == "__main__":
    main()
  
        

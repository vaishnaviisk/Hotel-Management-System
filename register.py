from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk  #pip install poillow
from tkinter import messagebox
import mysql.connector
# from login import login_window

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
    root=Tk()
    app=Register(root)
    root.mainloop()

from tkinter import*
from PIL import Image,ImageTk  #pip install pillow
from tkinter import ttk

from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox 

class Employee:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1000x525+250+100")

        #=============VARIABLES===========
        self.var_emp_id=StringVar()
        self.var_emp_name=StringVar()
        self.var_efather=StringVar()
        self.var_egender=StringVar()
        self.var_salary=StringVar()
        self.var_emobile=StringVar()
        self.var_eemail=StringVar()
        self.var_jobdesc=StringVar()
        self.var_eaddress=StringVar()
        self.var_eid_type=StringVar()
        self.var_eid_number=StringVar()

     # =========title===============
        lbl_title=Label(self.root,text="EMPLOYEE DETAILS",font=("times new roman",18),bg="black",fg="light green",bd=4,relief=RIDGE)        
        lbl_title.place(x=0,y=0,width=1000,height=50)

     # ===============logo=================
        
        img2=Image.open(r"C:\Hotel Management system\images\Hotel Logo.png")
        img2=img2.resize((100,40), Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)


        lbling=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lbling.place(x=5,y=5,width=100,height=40)

    # ====================labelFrame==============

        labelframeleft1=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Employee Details",font=("times new roman",12,"bold"),bg="white",fg="dark green",padx=2,)
        labelframeleft1.place(x=5,y=50,width=425,height=490)

     # ==========labels and entry==================
        #================ employee id ===================
        lbl_cust_ref=Label(labelframeleft1,font=("times new roman",12),text="Employee ID",bg="white",fg="green",padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)

        enty_ref=ttk.Entry(labelframeleft1,textvariable=self.var_emp_id,font=("times new roman",13),width=29)
        enty_ref.grid(row=0,column=1)

        # EMPLOYEE name
        ename=Label(labelframeleft1,text="Employee Name",font=("times new roman",12),bg="white",fg="green",padx=2,pady=6)
        ename.grid(row=1,column=0,sticky=W)
        txtename=ttk.Entry(labelframeleft1,textvariable=self.var_emp_name,font=("times new roman",13),width=29)
        txtename.grid(row=1,column=1)

        # father name
        lblFrname=Label(labelframeleft1,text="Father Name",font=("times new roman",12),bg="white",fg="green",padx=2,pady=6)
        lblFrname.grid(row=2,column=0,sticky=W)

        txtFrname=ttk.Entry(labelframeleft1,textvariable=self.var_efather,font=("times new roman",13),width=29)
        txtFrname.grid(row=2,column=1)

        # gender combobox
        lbl_gender=Label(labelframeleft1,text="Gender",font=("times new roman",12),bg="white",fg="green",padx=2,pady=6)
        lbl_gender.grid(row=3,column=0,sticky=W)
        combo_gender=ttk.Combobox(labelframeleft1,textvariable=self.var_egender,font=("times new roman",13),width=27,state="readonly")
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)

        
        # Salary
        lblPostCode1=Label(labelframeleft1,text="Salary",font=("times new roman",12),bg="white",fg="green",padx=2,pady=6)
        lblPostCode1.grid(row=4,column=0,sticky=W)

        txtPostCode1=ttk.Entry(labelframeleft1,textvariable=self.var_salary,font=("times new roman",13),width=29)
        txtPostCode1.grid(row=4,column=1)

        # mobile number
        lblMobile=Label(labelframeleft1,text="Mobile No",font=("times new roman",12),bg="white",fg="green",padx=2,pady=6)
        lblMobile.grid(row=5,column=0,sticky=W)

        txtMobile=ttk.Entry(labelframeleft1,textvariable=self.var_emobile,font=("times new roman",13),width=29)
        txtMobile.grid(row=5,column=1)

        # email
        lblEmail1=Label(labelframeleft1,text="Email",font=("times new roman",12),bg="white",fg="green",padx=2,pady=6)
        lblEmail1.grid(row=6,column=0,sticky=W)

        txtEmail=ttk.Entry(labelframeleft1,textvariable=self.var_eemail,font=("times new roman",13),width=29)
        txtEmail.grid(row=6,column=1)

        # job desc
        lbljobdesc=Label(labelframeleft1,text="Job Description",font=("times new roman",12),bg="white",fg="green",padx=2,pady=6)
        lbljobdesc.grid(row=7,column=0,sticky=W)
        combo_jobdesc=ttk.Combobox(labelframeleft1,textvariable=self.var_jobdesc,font=("times new roman",13),width=27,state="readonly")
        combo_jobdesc["value"]=("Reception","Maintainance","Kitchen","Manager")
        combo_jobdesc.current(0)
        combo_jobdesc.grid(row=7,column=1)


        # idproof combobox
        lblIdProof1=Label(labelframeleft1,text="Id Proof Type",font=("times new roman",12),bg="white",fg="green",padx=2,pady=6)
        lblIdProof1.grid(row=8,column=0,sticky=W)
        combo_id1=ttk.Combobox(labelframeleft1,textvariable=self.var_eid_type,font=("times new roman",13),width=27,state="readonly")
        combo_id1["value"]=("Aadhar","Pan","Driving licence","Passport")
        combo_id1.current(0)
        combo_id1.grid(row=8,column=1)

        # idproof no
        lblIdNumber=Label(labelframeleft1,text="Id Number",font=("times new roman",12),bg="white",fg="green",padx=2,pady=6)
        lblIdNumber.grid(row=9,column=0,sticky=W)

        txtIdNumber=ttk.Entry(labelframeleft1,textvariable=self.var_eid_number,font=("times new roman",13),width=29)
        txtIdNumber.grid(row=9,column=1)

        #address
        lblAddress=Label(labelframeleft1,text="Address",font=("times new roman",12),bg="white",fg="green",padx=2,pady=6)
        lblAddress.grid(row=10,column=0,sticky=W)

        txtAddress=ttk.Entry(labelframeleft1,textvariable=self.var_eaddress,font=("times new roman",13),width=29)
        txtAddress.grid(row=10,column=1)

        #=======================btns=============================
        btn_frame=Frame(labelframeleft1,bd=2,relief=RIDGE)
        btn_frame.place(x=5,y=400,width=410,height=35)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("times new roman",12),bg="black",fg="light green",width=10)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.Update,font=("times new roman",12),bg="black",fg="light green",width=10)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("times new roman",12),bg="black",fg="light green",width=10)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("times new roman",12),bg="black",fg="light green",width=10)
        btnReset.grid(row=0,column=3,padx=1)

        # ===========table frame search system==================
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("times new roman",12,"bold"),bg="white",fg="dark green",padx=2,)
        Table_Frame.place(x=435,y=50,width=555,height=490)

        lblSearchBy=Label(Table_Frame,font=("times new roman",12),text="Search By",bg="green",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)
        self.Search_var=StringVar()
        combo_Search=ttk.Combobox(Table_Frame,textvariable=self.Search_var,font=("times new roman",13),width=15,state="readonly")
        combo_Search["value"]=("Mobile","Ref")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()
        txtSearch=ttk.Entry(Table_Frame,textvariable=self.txt_search,font=("times new roman",13),width=15)
        txtSearch.grid(row=0,column=2,padx=2)

        btnSearch=Button(Table_Frame,text="Search",command=self.Search,font=("times new roman",12),bg="green",fg="white",width=8)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowAll=Button(Table_Frame,text="Show All",command=self.fetch_data,font=("times new roman",12),bg="green",fg="white",width=8)
        btnShowAll.grid(row=0,column=4,padx=1)

        # ======shw data table========

        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=840,height=350)
        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Emp_Details_Table=ttk.Treeview(details_table,column=("EmpID","EmpName","EmpFather","EmpGender","EmpSalary","EmpMobile","EmpEmail","JobDesc","EmpIDType","EmpIDNumber","EmpAddress"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Emp_Details_Table.xview)
        scroll_y.config(command=self.Emp_Details_Table.yview)


        self.Emp_Details_Table.heading("EmpID",text="Employee ID")
        self.Emp_Details_Table.heading("EmpName",text="Name")
        self.Emp_Details_Table.heading("EmpFather",text="Mother")
        self.Emp_Details_Table.heading("EmpGender",text="Gender")
        self.Emp_Details_Table.heading("EmpSalary",text="Salary")
        self.Emp_Details_Table.heading("EmpMobile",text="Mobile")
        self.Emp_Details_Table.heading("EmpEmail",text="Email")
        self.Emp_Details_Table.heading("JobDesc",text="Job description")
        self.Emp_Details_Table.heading("EmpIDType",text="Idproof")
        self.Emp_Details_Table.heading("EmpIDNumber",text="IdNumber")
        self.Emp_Details_Table.heading("EmpAddress",text="Address")

        self.Emp_Details_Table["show"]="headings"
        self.Emp_Details_Table.column("EmpID",width=100)
        self.Emp_Details_Table.column("EmpName",width=100)
        self.Emp_Details_Table.column("EmpFather",width=100)
        self.Emp_Details_Table.column("EmpGender",width=100)
        self.Emp_Details_Table.column("EmpSalary",width=100)
        self.Emp_Details_Table.column("EmpMobile",width=100)
        self.Emp_Details_Table.column("EmpEmail",width=100)
        self.Emp_Details_Table.column("JobDesc",width=100)
        self.Emp_Details_Table.column("EmpIDType",width=100)
        self.Emp_Details_Table.column("EmpIDNumber",width=100)
        self.Emp_Details_Table.column("EmpAddress",width=100)

        self.Emp_Details_Table.pack(fill=BOTH,expand=1)
        self.Emp_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    def add_data(self):
        if self.var_emobile.get()=="" or self.var_efather.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Varshmysql?",database="Hotel")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into employee values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                self.var_emp_id.get(),
                                                                                self.var_emp_name.get(),
                                                                                self.var_efather.get(),
                                                                                self.var_egender.get(),
                                                                                self.var_salary.get(),
                                                                                self.var_emobile.get(),
                                                                                self.var_eemail.get(),
                                                                                self.var_jobdesc.get(),
                                                                                self.var_eid_type.get(),
                                                                                self.var_eid_number.get(),
                                                                                self.var_eaddress.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Employee has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning","some thing went wrong:{str(es)}",parent=self.root)

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Varshmysql?",database="Hotel")            
        my_cursor=conn.cursor()
        my_cursor.execute("select * from employee")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Emp_Details_Table.delete(*self.Emp_Details_Table.get_children())
            for i in rows:
                self.Emp_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()
    def get_cursor(self,event=""):
        cursor_row=self.Emp_Details_Table.focus()
        content=self.Emp_Details_Table.item(cursor_row)
        row=content["values"]

        self.var_emp_id.set(row[0]),
        self.var_emp_name.set(row[1]),
        self.var_efather.set(row[2]),
        self.var_egender.set(row[3]),
        self.var_salary.set(row[4]),
        self.var_emobile.set(row[5]),
        self.var_eemail.set(row[6]),
        self.var_jobdesc.set(row[7]),
        self.var_eid_type.set(row[8]),
        self.var_eid_number.set(row[9]),
        self.var_eaddress.set(row[10])

    def Update(self):
        if self.var_emobile.get()=="":
            messagebox.showerror("Error","Please enter Mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Varshmysql?",database="Hotel")            
            my_cursor=conn.cursor()
            my_cursor.execute("update employee set EmpName=%s,EmpFather=%s,EmpGender=%s,EmpSalary=%s,EmpMobile=%s,EmpEmail=%s,JobDesc=%s,EmpIDType=%s,EmpIDNumber=%s,EmpAddress=%s where EmpID=%s",(
                                                                                                                                                                        self.var_emp_name.get(),
                                                                                                                                                                        self.var_efather.get(),
                                                                                                                                                                        self.var_egender.get(),
                                                                                                                                                                        self.var_salary.get(),
                                                                                                                                                                        self.var_emobile.get(),
                                                                                                                                                                        self.var_eemail.get(),
                                                                                                                                                                        self.var_jobdesc.get(),
                                                                                                                                                                        self.var_eid_type.get(),
                                                                                                                                                                        self.var_eid_number.get(),
                                                                                                                                                                        self.var_eaddress.get(),
                                                                                                                                                                        self.var_emp_id.get(),
                                                                                                                                                                    ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("update","Employee details has been updated Successfully",parent=self.root)

    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","do you want delete employee",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Varshmysql?",database="Hotel")            
            my_cursor=conn.cursor()
            query="delete from employee where EmpID=%s"
            value=(self.var_emp_id.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.cl.set("")

    def reset(self):
        self.var_emp_id.set(""),
        self.var_emp_name.set(""),
        self.var_efather.set(""),
        #self.var_egender.set(""),
        self.var_salary.set(""),
        self.var_emobile.set(""),
        self.var_eemail.set(""),
        #self.var_jobdesc.set(""),
        #self.var_eid_type.set(""),
        self.var_eid_number.set(""),
        self.var_eaddress.set("")

    def Search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Varshmysql?",database="Hotel")            
        my_cursor=conn.cursor()

        my_cursor.execute("Select * from employee where " + str(self.search_var.get()) + " LIKE '%" + str(self.txt_search.get()) + "%'")

        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Emp_Details_Table.delete(*self.Emp_Details_Table.get_children())
            for i in rows:
                self.Emp_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
    

 


if __name__ == "__main__":
    root=Tk()
    obj=Employee(root)
    root.mainloop()


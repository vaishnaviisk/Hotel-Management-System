from tkinter import*
from PIL import Image,ImageTk  #pip install pillow
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox 

class Roombooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1000x520+250+100")

        #======variables=======
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()


        # =========title===============
        lbl_title=Label(self.root,text="ROOM BOOKING DETAILS",font=("times new roman",18),bg="black",fg="light green",bd=4,relief=RIDGE)        
        lbl_title.place(x=0,y=0,width=1000,height=50)

        # ===============logo=================
        
        img2=Image.open(r"C:\Hotel Management system\images\Hotel Logo.png")
        img2=img2.resize((100,40), Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)


        lbling=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lbling.place(x=5,y=5,width=100,height=40)

        # ====================labelFrame==============

        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Booking Details",font=("times new roman",12,"bold"),bg="white",fg="dark green",padx=2,)
        labelframeleft.place(x=5,y=50,width=425,height=490)

        # ==========labels and entry==================
        # custref
        lbl_cust_contact=Label(labelframeleft,font=("times new roman",12),text="Customer Contact",bg="white",fg="green",padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)

        entry_contact=ttk.Entry(labelframeleft,textvariable=self.var_contact,font=("times new roman",13),width=20)
        entry_contact.grid(row=0,column=1,sticky=W)

        #fetch data button
        btnFetchData=Button(labelframeleft,command=self.Fetch_contact,text="Fetch Data",font=("times new roman",9),bg="green",fg="white",width=9)
        btnFetchData.place(x=310,y=4)

        #check in date
        check_in_date=Label(labelframeleft,font=("times new roman",12),text="Check_in Date",bg="white",fg="green",padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)
        txtcheck_in_date=ttk.Entry(labelframeleft,textvariable=self.var_checkin,font=("times new roman",13),width=29)
        txtcheck_in_date.grid(row=1,column=1)

        #check out date
        lbl_Check_out=Label(labelframeleft,font=("times new roman",12),text="Check_Out Date",bg="white",fg="green",padx=2,pady=6)
        lbl_Check_out.grid(row=2,column=0,sticky=W)
        txt_Check_out=ttk.Entry(labelframeleft,textvariable=self.var_checkout,font=("times new roman",13),width=29)
        txt_Check_out.grid(row=2,column=1)

        #Room type
        label_RoomType=Label(labelframeleft,font=("times new roman",12),text="Room Type",bg="white",fg="green",padx=2,pady=6)
        label_RoomType.grid(row=3,column=0,sticky=W)

        conn=mysql.connector.connect(host="localhost",username="root",password="Varshmysql?",database="hotel")            
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomType from details")
        row1=my_cursor.fetchall()

        combo_RoomType=ttk.Combobox(labelframeleft,textvariable=self.var_roomtype,font=("times new roman",13),width=27,state="readonly")
        combo_RoomType["value"]=row1
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3,column=1)

        #Available room
        lblRoomAvailable=Label(labelframeleft,font=("times new roman",12),text="Room Available",bg="white",fg="green",padx=2,pady=6)
        lblRoomAvailable.grid(row=4,column=0,sticky=W)
        # txtRoomAvailable=ttk.Entry(labelframeleft,textvariable=self.var_roomavailable,font=("times new roman",13),width=29)
        # txtRoomAvailable.grid(row=4,column=1)

        conn=mysql.connector.connect(host="localhost",username="root",password="Varshmysql?",database="hotel")            
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomNo from details")
        row2=my_cursor.fetchall()

        combo_RoomNo=ttk.Combobox(labelframeleft,textvariable=self.var_roomavailable,font=("times new roman",13),width=27,state="readonly")
        combo_RoomNo["value"]=row2
        combo_RoomNo.current(0)
        combo_RoomNo.grid(row=4,column=1)


        #meal
        lblMeal=Label(labelframeleft,font=("times new roman",12),text="Meal",bg="white",fg="green",padx=2,pady=6)
        lblMeal.grid(row=5,column=0,sticky=W)
        txtMeal=ttk.Entry(labelframeleft,textvariable=self.var_meal,font=("times new roman",13),width=29)
        txtMeal.grid(row=5,column=1)

        #No of days
        lblNoOfDays=Label(labelframeleft,font=("times new roman",12),text="No Of Days",bg="white",fg="green",padx=2,pady=6)
        lblNoOfDays.grid(row=6,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(labelframeleft,textvariable=self.var_noofdays,font=("times new roman",13),width=29)
        txtNoOfDays.grid(row=6,column=1)

        #Paid tax
        lblIdNumber=Label(labelframeleft,font=("times new roman",12),text="Paid Tax",bg="white",fg="green",padx=2,pady=6)
        lblIdNumber.grid(row=7,column=0,sticky=W)
        txtIdNumber=ttk.Entry(labelframeleft,textvariable=self.var_paidtax,font=("times new roman",13),width=29)
        txtIdNumber.grid(row=7,column=1)

        #Sub total
        lblNoOfDays=Label(labelframeleft,font=("times new roman",12),text="Sub Total",bg="white",fg="green",padx=2,pady=6)
        lblNoOfDays.grid(row=8,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(labelframeleft,textvariable=self.var_actualtotal,font=("times new roman",13),width=29)
        txtNoOfDays.grid(row=8,column=1)

        #Total Cost
        lblIdNumber=Label(labelframeleft,font=("times new roman",12),text="Total Cost",bg="white",fg="green",padx=2,pady=6)
        lblIdNumber.grid(row=9,column=0,sticky=W)
        txtIdNumber=ttk.Entry(labelframeleft,textvariable=self.var_total,font=("times new roman",13),width=29)
        txtIdNumber.grid(row=9,column=1)

        #===========bill btn==========
        btnBill=Button(labelframeleft,text="Bill",command=self.total,font=("times new roman",12),bd=2,relief=RIDGE,bg="green",fg="white",width=9)
        btnBill.place(x=7,y=355,width=100,height=35)


        # ---------------------btn---------------------------
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=5,y=400,width=410,height=35)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("times new roman",12),bg="black",fg="light green",width=10)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.Update,font=("times new roman",12),bg="black",fg="light green",width=10)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("times new roman",12),bg="black",fg="light green",width=10)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("times new roman",12),bg="black",fg="light green",width=10)
        btnReset.grid(row=0,column=3,padx=1)

        #==========================RIGHT SIDE IMAGE======================
        img3=Image.open(r"C:\Hotel Management system\images\Bedroom.jpg")
        img3=img3.resize((320,230 ), Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg=Label(self.root,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg.place(x=680,y=50,width=320,height=230)



        # ===========table frame search system==================
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("times new roman",12,"bold"),bg="white",fg="dark green",padx=2,)
        Table_Frame.place(x=435,y=280,width=565,height=260)

        lblSearchBy=Label(Table_Frame,font=("times new roman",12),text="Search By",bg="green",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)
        self.Search_var=StringVar()
        combo_Search=ttk.Combobox(Table_Frame,textvariable=self.Search_var,font=("times new roman",13),width=15,state="readonly")
        combo_Search["value"]=("Contact","Room")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()
        txtSearch=ttk.Entry(Table_Frame,textvariable=self.txt_search,font=("times new roman",13),width=15)
        txtSearch.grid(row=0,column=2,padx=2)

        btnSearch=Button(Table_Frame,text="Search",command=self.Search,font=("times new roman",12),bg="green",fg="white",width=8)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowAll=Button(Table_Frame,text="Show All",command=self.fetch_data,font=("times new roman",12),bg="green",fg="white",width=8)
        btnShowAll.grid(row=0,column=4,padx=1)

         # ======show data table========

        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=40,width=550,height=180)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.room_table=ttk.Treeview(details_table,column=("contact","checkin","checkout","roomtype"
                                                                   ,"roomavailable","meal","noOfdays"
                                                                   ),xscrollcommand=scroll_x.set,
                                                                   yscrollcommand=scroll_y)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("contact",text="Contact")
        self.room_table.heading("checkin",text="Check In")
        self.room_table.heading("checkout",text="Check Out")
        self.room_table.heading("roomtype",text="Room Type")
        self.room_table.heading("roomavailable",text="Room No")
        self.room_table.heading("meal",text="Meal")
        self.room_table.heading("noOfdays",text="No of Days")
        

        self.room_table["show"]="headings"
        self.room_table.column("contact",width=100)
        self.room_table.column("checkin",width=100)
        self.room_table.column("checkout",width=100)
        self.room_table.column("roomtype",width=100)
        self.room_table.column("roomavailable",width=100)
        self.room_table.column("meal",width=100)
        self.room_table.column("noOfdays",width=100)
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()

#=======================add data=========================
    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Varshmysql?",database="hotel")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                self.var_contact.get(),
                                                                                self.var_checkin.get(),
                                                                                self.var_checkout.get(),
                                                                                self.var_roomtype.get(),
                                                                                self.var_roomavailable.get(),
                                                                                self.var_meal.get(),
                                                                                self.var_noofdays.get()
                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Room booked",parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning","Something went wrong:{str(es)}",parent=self.root)

    # =====fetch data==============
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Varshmysql?",database="hotel")            
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    
 #===============get_cursor====================
    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]

        self.var_contact.set(row[0]),
        self.var_checkin.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_roomavailable.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_noofdays.set(row[6])    

#====update function==============
    def Update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter Contact number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Varshmysql?",database="hotel")            
            my_cursor=conn.cursor()
            my_cursor.execute("update room set Check_in=%s,Check_out=%s,Roomtype=%s,Room=%s,Meal=%s,Noofdays=%s where Contact=%s",(
                                                                                                                                                                        
                                                                                                                                        self.var_checkin.get(),
                                                                                                                                        self.var_checkout.get(),
                                                                                                                                        self.var_roomtype.get(),
                                                                                                                                        self.var_roomavailable.get(),
                                                                                                                                        self.var_meal.get(),
                                                                                                                                        self.var_noofdays.get(),
                                                                                                                                        self.var_contact.get()
                                                                                                                                     ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room details has been updated successfully",parent=self.root)
    
#=============delete========
    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you want delete Customer",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Varshmysql?",database="hotel")            
            my_cursor=conn.cursor()
            query="delete from room where Contact=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        self.var_contact.set(""),
        self.var_checkin.set(""),
        self.var_checkout.set(""),
        self.var_roomtype.set(""),
        self.var_roomavailable.set(""),
        self.var_meal.set(""),
        self.var_noofdays.set("") 
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("") 

        #================All data fetch========

    def Fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","please enter contact number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Varshmysql?",database="hotel")            
            my_cursor=conn.cursor()
            query=("Select Name from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","This Number Not Found",parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataframe.place(x=430,y=50,width=250,height=230)

                lblName=Label(showDataframe,text="Name:",font=("times new roman",12))
                lblName.place(x=0,y=0)

                lbl=Label(showDataframe,text=row,font=("times new roman",12))
                lbl.place(x=45,y=0)

                #========================gender===========================
                conn=mysql.connector.connect(host="localhost",username="root",password="Varshmysql?",database="hotel")            
                my_cursor=conn.cursor()
                query=("select Gender from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblGender=Label(showDataframe,text="Gender:",font=("times new roman",12))
                lblGender.place(x=0,y=30)

                lbl2=Label(showDataframe,text=row,font=("times new roman",12))
                lbl2.place(x=50,y=30)

                #===============email================
                conn=mysql.connector.connect(host="localhost",username="root",password="Varshmysql?",database="hotel")            
                my_cursor=conn.cursor()
                query=("select Email from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblmail=Label(showDataframe,text="Email:",font=("times new roman",12))
                lblmail.place(x=0,y=60)

                lbl3=Label(showDataframe,text=row,font=("times new roman",12))
                lbl3.place(x=43,y=60)

                #============================nationality================
                conn=mysql.connector.connect(host="localhost",username="root",password="Varshmysql?",database="hotel")            
                my_cursor=conn.cursor()
                query=("select Nationality from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblNationality=Label(showDataframe,text="Nationality:",font=("times new roman",12))
                lblNationality.place(x=0,y=90)

                lbl4=Label(showDataframe,text=row,font=("times new roman",12))
                lbl4.place(x=70,y=90)

                #====================address===============
                conn=mysql.connector.connect(host="localhost",username="root",password="Varshmysql?",database="hotel")            
                my_cursor=conn.cursor()
                query=("select Address from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblAddress=Label(showDataframe,text="Address:",font=("times new roman",12))
                lblAddress.place(x=0,y=120)

                lbl5=Label(showDataframe,text=row,font=("times new roman",12))
                lbl5.place(x=55,y=120)

#===================Search system====================
    def Search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Varshmysql?",database="hotel")            
        my_cursor=conn.cursor()

        my_cursor.execute("Select * from room where " + str(self.Search_var.get()) + " LIKE '%" + str(self.txt_search.get()) + "%'")

        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def total(self):
        inDate=self.var_checkin.get()
        outDate=self.var_checkout.get()
        inDate=datetime.strptime(inDate,"%d/%m/%Y")
        outDate=datetime.strptime(outDate,"%d/%m/%Y")
        self.var_noofdays.set(abs(outDate-inDate).days)
                
        if (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Luxury"):
            q1=float(250)
            q2=float(1200)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Single"):
            q1=float(300)
            q2=float(900)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Luxury"):
            q1=float(300)
            q2=float(1200)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Luxury"):
            q1=float(450)
            q2=float(1200)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Single"):
            q1=float(250)
            q2=float(900)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        
        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Single"):
            q1=float(450)
            q2=float(900)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Double"):
            q1=float(500)
            q2=float(1500)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Double"):
            q1=float(600)
            q2=float(1500)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Double"):
            q1=float(900)
            q2=float(1500)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)


if __name__ == "__main__":
    root=Tk()
    obj=Roombooking(root)
    root.mainloop()

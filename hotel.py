from tkinter import*
from PIL import Image,ImageTk  #pip install pillow
from Customer import Cust_Win
from Room import Roombooking
from Details import DetailsRoom
from Employee import Employee


class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")


        # ==================logo=================
        img2=Image.open(r"C:\Hotel Management system\images\Hotel Logo.png")
        img2=img2.resize((230,200), Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lbling=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lbling.place(x=0,y=0,width=230,height=200)
        
        # =======================title==============
        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman",40),bg="black",fg="white",bd=4,relief=RIDGE)        
        lbl_title.place(x=230,y=0,width=1075,height=50)

        # ==============main frame=================
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)


        # ====================menu===============
        lbl_menu=Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="white",bd=4,relief=RIDGE)        
        lbl_menu.place(x=0,y=0,width=225)

        # ================btn frame============
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=40,width=225,height=200)

        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=18,font=("times new roman",16),bg="black",fg="light green",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn=Button(btn_frame,text="ROOM",command=self.Roombooking,width=18,font=("times new roman",16),bg="black",fg="light green",bd=0,cursor="hand1")
        room_btn.grid(row=1,column=0,pady=1)

        details_btn=Button(btn_frame,text="DETAILS",command=self.details_room,width=18,font=("times new roman",16),bg="black",fg="light green",bd=0,cursor="hand1")
        details_btn.grid(row=2,column=0,pady=1)

        report_btn=Button(btn_frame,text="EMPLOYEE",command=self.emp_details,width=18,font=("times new roman",16),bg="black",fg="light green",bd=0,cursor="hand1")
        report_btn.grid(row=3,column=0,pady=1)

        logout_btn=Button(btn_frame,text="LOGOUT",command=self.logout,width=18,font=("times new roman",16),bg="black",fg="light green",bd=0,cursor="hand1")
        logout_btn.grid(row=4,column=0,pady=1)


        
        # ===============right side img============
        img3=Image.open(r"C:\Hotel Management system\images\Hotel.jpg")
        img3=img3.resize((1100,590), Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lbling1=Label(self.root,image=self.photoimg3,bd=4,relief=RIDGE)
        lbling1.place(x=230,y=50,width=1100,height=590)

    # =============down img====================
        
        img4=Image.open(r"c:\Hotel Management system\images\Food.jpeg")
        img4=img4.resize((230,210), Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lbling1=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lbling1.place(x=0,y=230,width=230,height=220)



    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_Win(self.new_window)

    def Roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app=Roombooking(self.new_window)

    def details_room(self):
        self.new_window=Toplevel(self.root)
        self.app=DetailsRoom(self.new_window)

    def emp_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Employee(self.new_window)


    def logout(self):
        self.root.destroy()


if __name__ == "__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()

from cProfile import label
from cgitb import text
from tkinter import *
from tkinter import font , font
from turtle import width
from unicodedata import category
from PIL import Image,ImageTk
from numpy import product
from empolyee import employeeclass
from Supplier import supplierclass
from sales import salesclass 
from category import categoryclass
from product import productclass
import sqlite3
from tkinter import messagebox
import os
import time
class IMS:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Inventory Management System   |   Developed by ANISH")
        self.root.config(bg="White")

        #___Title___
        self.icon_title = PhotoImage(file="images/loogss.png")
        title = Label(self.root,text="INVENTORY MANAGEMENT SYSTEM",image = self.icon_title,compound=LEFT,font=("times new roman",35,"bold"),bg="#87cefa",fg="dark blue",anchor="w",padx=20).place(x=0,y=0,relwidth = 1,height = 80)
        
        #___button_logout__
        btn_logout=Button(self.root,text="Logout",command=self.logout,font=("Consolas",15,"bold"),bg="#F9ED52",cursor="hand2").place(x=1385,y=15,height=50,width=100)

        #___clock___
        self.lbl_clock= Label(self.root,text="Welcome to Inventory Management System\t\t  Date::DD|MM|YYYY\t\t  Time::HH:MM:SS",font=("Constantia"),bg="#808080",fg="white")
        self.lbl_clock.place(x=0,y=80,relwidth = 1,height = 35)

        #____left menu__
        self.Menu_logo = Image.open("images/cat1.jpg")
        self.Menu_logo = self.Menu_logo.resize((400,250),Image.ANTIALIAS)
        self.Menu_logo = ImageTk.PhotoImage(self.Menu_logo)

        LeftMenu = Frame(self.root,bd=2,relief=RIDGE,bg="white")
        LeftMenu.place(x=0,y=115,height=670,width=400)

        Lbl_Menulogo = Label(LeftMenu,image=self.Menu_logo)
        Lbl_Menulogo.pack(side=TOP,fill=X,)

        self.icon_side = PhotoImage(file="images/side.png")
        
        btn_menu=Button(LeftMenu,text="----- MENU -----",font=("Consolas",20),bg="#000080",fg="white").pack(side=TOP,fill=X)
        btn_employee=Button(LeftMenu,text="EMPLOYEE",command=self.employee,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("Courier",20,"bold"),bg="#ADD8E6",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_supplier=Button(LeftMenu,text="SUPPLIER",command=self.supplier,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("Courier",20,"bold"),bg="#ADD8E6",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_category=Button(LeftMenu,text="CATEGORY",command=self.category,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("Courier",20,"bold"),bg="#ADD8E6",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_product=Button(LeftMenu,text="PRODUCT",command=self.product,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("Courier",20,"bold"),bg="#ADD8E6",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_sales=Button(LeftMenu,text="SALES",command=self.sales,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("Courier",20,"bold"),bg="#ADD8E6",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_exit=Button(LeftMenu,text="EXIT",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("Courier",20,"bold"),bg="#ADD8E6",bd=3,cursor="hand2").pack(side=TOP,fill=X)

        #___content__

        self.lbl_employee=Label(self.root,text="Total Employee\n [ 0 ]",bd=5,relief=RIDGE,bg="#00CC99",fg="black",font=("Microsoft Sans Serif",20,"bold"))
        self.lbl_employee.place(x=450,y=160,height=150,width=300)

        self.lbl_supplier=Label(self.root,text="Total Supplier\n [ 0 ]",bd=5,relief=RIDGE,bg="#00CCCC",fg="black",font=("Microsoft Sans Serif",20,"bold"))
        self.lbl_supplier.place(x=800,y=160,height=150,width=300)

        self.lbl_category=Label(self.root,text="Total Category\n [ 0 ]",bd=5,relief=RIDGE,bg="#00CCFF",fg="black",font=("Microsoft Sans Serif",20,"bold"))
        self.lbl_category.place(x=1150,y=160,height=150,width=300)

        self.lbl_product=Label(self.root,text="Total Product\n [ 0 ]",bd=5,relief=RIDGE,bg="#00FF99",fg="black",font=("Microsoft Sans Serif",20,"bold"))
        self.lbl_product.place(x=450,y=410,height=150,width=300)

        self.lbl_sales=Label(self.root,text="Total Sales\n [ 0 ]",bd=5,relief=RIDGE,bg="#00FFCC",fg="black",font=("Microsoft Sans Serif",20,"bold"))
        self.lbl_sales.place(x=800,y=410,height=150,width=300)

         #___foter___
        lbl_footer= Label(self.root,text="INVENTORY MANAGEMENT SYSTEM ------------------------------------ For any Query Cantact : 88xxxxxx94",font=("Leelawadee UI",13),bg="#282828",fg="white").pack(side=BOTTOM,fill=X)
        self.update_content()
#__________________________________________________

    def employee(self):
        self.new_winn=Toplevel(self.root)
        self.new_objj=employeeclass(self.new_winn)


    def supplier(self):
        self.new_winn=Toplevel(self.root)
        self.new_objj=supplierclass(self.new_winn)


    def sales(self):
        self.new_winn=Toplevel(self.root)
        self.new_objj=salesclass(self.new_winn)

    
    def category(self):
        self.new_winn=Toplevel(self.root)
        self.new_objj=categoryclass(self.new_winn)


    def product(self):
        self.new_winn=Toplevel(self.root)
        self.new_objj=productclass(self.new_winn)

    def update_content(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from product")
            product = cur.fetchall()
            self.lbl_product.config(text = f"Total Products\n [ {str(len(product))} ]")

            cur.execute("select * from supplier")
            supplier = cur.fetchall()
            self.lbl_supplier.config(text = f"Total Supplier\n [ {str(len(supplier))} ]")

            cur.execute("select * from empolyee")
            employee = cur.fetchall()
            self.lbl_employee.config(text = f"Total Employees\n [ {str(len(employee))} ]")

            cur.execute("select * from category")
            category = cur.fetchall()
            self.lbl_category.config(text = f"Total Category\n [ {str(len(category))} ]")

            bill = len(os.listdir('bill'))
            self.lbl_sales.config(text = f"Total Sales\n [{str(bill)}]")


            time_=time.strftime("%I:%M:%S")
            date_=time.strftime("%d/%m/%Y")
            self.lbl_clock.config(text=f"Welcome to Inventory Management System\t\t  Date::{str(date_)}\t\t  Time::{str(time_)}",font=("Constantia"),bg="#808080",fg="white")
            self.lbl_clock.after(200,self.update_content)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)

    def logout(self):
        self.root.destroy()
        os.system("python loginpagee.py")




if __name__=="__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()
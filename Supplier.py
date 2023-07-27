from cProfile import label
from cgitb import text
from tkinter import *
from tkinter import font , font
from tkinter import messagebox
from turtle import title, width
from PIL import Image,ImageTk
from tkinter import ttk
import sqlite3

# from Supplier1 import supplierclass
class supplierclass:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1100x615+410+150")
        self.root.title("Inventory Management System   |   Developed by ANISH")
        self.root.config(bg="White")
        self.root.focus_force()

        #_____ALL VARIABLES____
        self.var_searchby=StringVar()
        self.var_searchtext=StringVar()

        self.var_supplier_invoice=StringVar()
        self.var_name=StringVar()
        self.var_contact=StringVar()
        

        #____TITLE____
        title = Label(self.root,text="Manage Supplier Details",font=("Consolas",30,"bold"),bg="#87cefa",fg="dark blue",bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=20)
        
        #______SEARCH____

        lbl_invoice= Label(self.root,text="Invoice No.",font=("Franklin Gothic",15),bg="white").place(x=650,y=100)
        txt_search = Entry(self.root,textvariable=self.var_searchtext,font=("RomanD",10,"bold"),bg="#66FFFF").place(x=760,y=100,width=210)
        btn_search = Button(self.root,text="Search",font=("RomanD",10,"bold"),command=self.search,bg="#00CC33",fg="black",cursor="hand2").place(x=980,y=100,width=100,height=22)


        #_______CONTENT__
        lbl_invoice= Label(self.root,text="Invoice No.",font=("Franklin Gothic",15),bg="white").place(x=20,y=100)
        lbl_sup_name= Label(self.root,text="Supplier Name",font=("Franklin Gothic",15),bg="white").place(x=20,y=150)
        lbl_contact= Label(self.root,text="Contact",font=("Franklin Gothic",15),bg="white").place(x=20,y=200)
        lbl_description= Label(self.root,text="Description",font=("Franklin Gothic",15),bg="white").place(x=20,y=250)

        txt_invoice=Entry(self.root,textvariable=self.var_supplier_invoice,font=("Franklin Gothic",15),bg="#66FFFF").place(x=180,y=100,width=180) 
        txt_sup_name=Entry(self.root,textvariable=self.var_name,font=("Franklin Gothic",15),bg="#66FFFF").place(x=180,y=150,width=180)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("Franklin Gothic",15),bg="#66FFFF").place(x=180,y=200,width=180)
        self.txt_description=Text(self.root,font=("Franklin Gothic",15),bg="#66FFFF")
        self.txt_description.place(x=180,y=250,width=400,height=110)

        #______BUTTONS____

        btn_add=Button(self.root,text="Save",font=("Consolas",15,"bold"),command=self.add,bg="#0066FF",cursor="hand2").place(x=50,y=375,height=30,width=120)
        btn_update=Button(self.root,text="Update",font=("Consolas",15,"bold"),command=self.update,bg="#0099CC",cursor="hand2").place(x=200,y=375,height=30,width=110)
        btn_delete=Button(self.root,text="Delete",font=("Consolas",15,"bold"),command=self.delete,bg="#990033",cursor="hand2",fg="white").place(x=350,y=375,height=30,width=110)
        btn_clear=Button(self.root,text="Clear",font=("Consolas",15,"bold"),command=self.clear,bg="#996633",cursor="hand2",fg="white").place(x=500,y=375,height=30,width=110)

        #_______SUPPLIER IMAGES______
        self.supp_photo = Image.open("images/category.jpg")
        self.supp_photo = self.supp_photo.resize((590,190),Image.ANTIALIAS)
        self.supp_photo = ImageTk.PhotoImage(self.supp_photo)

        lbl_image=Label(self.root,image=self.supp_photo,bd=0)
        lbl_image.place(x=20,y=410)

        #________FRAME_________

        supp_frame = Frame(self.root,bd=3,relief=RIDGE)
        supp_frame.place(x=630,y=150,width=460,height=450)

        scrolly=Scrollbar(supp_frame,orient=VERTICAL)
        scrollx=Scrollbar(supp_frame,orient=HORIZONTAL)

        self.SupplierTable =ttk.Treeview(supp_frame,columns=("Invoice","Name","Contact","Description"),yscrollcommand=scrolly.set,xscrollcommand=scrollx)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.SupplierTable.xview)
        scrolly.config(command=self.SupplierTable.yview)

        self.SupplierTable.heading("Invoice",text="Invoice")
        self.SupplierTable.heading("Name",text="Name")
        self.SupplierTable.heading("Contact",text="Contact")
        self.SupplierTable.heading("Description",text="Description")
        self.SupplierTable["show"]="headings"

        self.SupplierTable.column("Invoice",width=20)
        self.SupplierTable.column("Name",width=20)
        self.SupplierTable.column("Contact",width=20)
        self.SupplierTable.column("Description",width=20)
        self.SupplierTable.pack(fill=BOTH,expand=1)
        self.SupplierTable.bind("<ButtonRelease-1>",self.getdata)

        self.show()


#__________________________________________________________________________________________________
    
    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_supplier_invoice.get()=="":
                messagebox.showerror("Error","Invoice No. must be required",parent=self.root)
            else:
                cur.execute("Select * from supplier where Invoice=?",(self.var_supplier_invoice.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Invoice no already assinged,try diffrent",parent=self.root)
                else:
                    cur.execute("Insert into supplier (Invoice,Name,Contact,Description) values(?,?,?,?)",(
                        self.var_supplier_invoice.get(),
                        self.var_name.get(),
                        self.var_contact.get(),
                        self.txt_description.get('1.0',END),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Supplier Added successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)


    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select * from supplier")
            rows=cur.fetchall()
            self.SupplierTable.delete(*self.SupplierTable.get_children())
            for row in rows:
                self.SupplierTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)


    def getdata(self,ev):
        f=self.SupplierTable.focus()
        content=(self.SupplierTable.item(f))
        row=content['values']
        # print(row)
        self.var_supplier_invoice.set(row[0])
        self.var_name.set(row[1])
        self.var_contact.set(row[2])
        self.txt_description.delete('1.0',END),
        self.txt_description.insert(END,row[3]),


    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_supplier_invoice.get()=="":
                messagebox.showerror("Error","Invoice No must be required",parent=self.root)
            else:
                cur.execute("Select * from supplier where Invoice=?",(self.var_supplier_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","This Invoice no. is Invalid",parent=self.root)
                else:
                    cur.execute("Update supplier set Name=?,Contact=?,Description=? where Invoice=?",(
                        
                        self.var_name.get(),
                        self.var_contact.get(),
                        self.txt_description.get('1.0',END),
                        self.var_supplier_invoice.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Supplier Updated successfully",parent=self.root)
                    self.clear()
                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)

    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_supplier_invoice.get()=="":
                messagebox.showerror("Error","Invoice no must be required",parent=self.root)
            else:
                cur.execute("Select * from supplier where Invoice=?",(self.var_supplier_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","This Invoiceis Invalid",parent=self.root)
                else:
                    op=messagebox.askyesno("Error","Do you want to delete?",parent=self.root)
                    if op==TRUE:
                        cur.execute("Delete from supplier where Invoice=?",(self.var_supplier_invoice.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Supplier Deleted Successfully",parent=self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)

    def clear(self):
        self.var_supplier_invoice.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.txt_description.delete('1.0',END),
        self.var_searchtext.set("")
        self.show()

    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_searchtext.get()=="":
                messagebox.showerror("Error","Search Invoice no should be required",parent=self.root)
            else:
                cur.execute("Select * from supplier where Invoice=?",(self.var_searchtext.get(),))
                row=cur.fetchone()
                if row!=None:
                    self.SupplierTable.delete(*self.SupplierTable.get_children())
                    self.SupplierTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found!!!",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
        

if __name__=="__main__":
    root = Tk()
    obj = supplierclass(root)
    root.mainloop()
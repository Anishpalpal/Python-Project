from cgitb import text
from msilib.schema import SelfReg
from sys import builtin_module_names
from tkinter import *
from tkinter import font , font
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import ttk
import sqlite3


class productclass:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1100x615+410+150")
        self.root.title("Inventory Management System   |   Developed by ANISH")
        self.root.config(bg="White")
        self.root.focus_force()


        self.var_searchby=StringVar()
        self.var_searchtext=StringVar()
        self.var_pid = StringVar()
        self.var_category=StringVar()
        self.var_supplier=StringVar()
        self.var_status=StringVar()
        self.var_search=StringVar()
        self.cat_list = []
        self.supp_list = []
        self.fetch_cat_supp()


        self.var_name=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()

        #_____________________________________________________________________
        
        product_frame=Frame(self.root,bd = 2,relief=RIDGE,bg="white")
        product_frame.place(x=10,y=10,width=450,height=600)

        product_title=Label(product_frame,text="Manage Product Details",font=("Consolas",20,"bold"), bg="#87cefa",fg="dark blue").pack(side=TOP, fill=X)

        lbl_Category= Label(product_frame,text="Category",font=("Franklin Gothic",15),bg="white").place(x=20,y=60)
        lbl_gender= Label(product_frame,text="supplier",font=("Franklin Gothic",15),bg="white").place(x=20,y=110)
        lbl_contact= Label(product_frame,text="Name",font=("Franklin Gothic",15),bg="white").place(x=20,y=160)
        lbl_name= Label(product_frame,text="Price",font=("Franklin Gothic",15),bg="white").place(x=20,y=210)
        lbl_qty= Label(product_frame,text="Quantity",font=("Franklin Gothic",15),bg="white").place(x=20,y=260)
        lbl_status= Label(product_frame,text="Status",font=("Franklin Gothic",15),bg="white").place(x=20,y=310)


#________________TEXT AREA_____________________________________


        cmb_category = ttk.Combobox(product_frame,textvariable=self.var_category,values=self.cat_list,state="readonly",justify=CENTER,font=("RomanD",10,"bold"))
        cmb_category.place(x=140,y=60,width=180)
        cmb_category.current(0)

        txt_name=Entry(product_frame,textvariable=self.var_name,font=("Franklin Gothic",15),bg="#66FFFF").place(x=140,y=160,width=180)
        txt_price=Entry(product_frame,textvariable=self.var_price,font=("Franklin Gothic",15),bg="#66FFFF").place(x=140,y=210,width=180)
        txt_qty= Entry(product_frame,textvariable=self.var_qty,font=("Franklin Gothic",15),bg="#66FFFF").place(x=140,y=260,width=180)

        cmb_supplier = ttk.Combobox(product_frame,textvariable=self.var_supplier,values=self.supp_list,state="readonly",justify=CENTER,font=("RomanD",10,"bold"))
        cmb_supplier.place(x=140,y=110,width=180)
        cmb_supplier.current(0)

        cmb_status = ttk.Combobox(product_frame,textvariable=self.var_status,values=("Active","Inactive"),state="readonly",justify=CENTER,font=("RomanD",10,"bold"))
        cmb_status.place(x=140,y=310,width=180)
        cmb_status.current(0)

        #_____BUTTONs____
        btn_add=Button(product_frame,text="Save",command=self.add,font=("Consolas",15,"bold"),bg="#0066FF",cursor="hand2").place(x=20,y=370,height=30,width=90)
        btn_update=Button(product_frame,text="Update",command=self.update,font=("Consolas",15,"bold"),bg="#0099CC",cursor="hand2").place(x=130,y=370,height=30,width=90)
        btn_delete=Button(product_frame,text="Delete",command=self.delete,font=("Consolas",15,"bold"),bg="#990033",cursor="hand2",fg="white").place(x=235,y=370,height=30,width=90)
        btn_clear=Button(product_frame,text="Clear",command=self.clear,font=("Consolas",15,"bold"),bg="#996633",cursor="hand2",fg="white").place(x=340,y=370,height=30,width=90)

        #_______product IMAGES______
        self.product_photo = Image.open("images/product.jpg")
        self.product_photo = self.product_photo.resize((420,150),Image.ANTIALIAS)
        self.product_photo = ImageTk.PhotoImage(self.product_photo)

        lbl_image=Label(product_frame,image=self.product_photo,bd=0)
        lbl_image.place(x=10,y=430)


        #____search frame__
        Searchframe = LabelFrame(self.root,text="Search Product",font=("RomanD",10,"bold"),bd=2,relief=RIDGE,bg="White")
        Searchframe.place(x=480,y=10,width=600,height=70)

        #___option__
        cmb_search = ttk.Combobox(Searchframe,textvariable=self.var_searchby,values=("Select","Category","Supplier","Name"),state="readonly",justify=CENTER,font=("RomanD",10,"bold"))
        cmb_search.place(x=10,y=10,width=130)
        cmb_search.current(0)

        txt_search = Entry(Searchframe,textvariable=self.var_searchtext,font=("RomanD",10,"bold"),bg="#66FFFF").place(x=150,y=10,width=250)
        btn_search = Button(Searchframe,text="Search",command=self.search,font=("RomanD",10,"bold"),bg="#00CC33",fg="black",cursor="hand2").place(x=420,y=10,width=130,height=22)
        #___PRODUCT DETAIL___

        pro_frame = Frame(self.root,bd=3,relief=RIDGE)
        pro_frame.place(x=480,y=100,width=600,height=500)

        scrolly=Scrollbar(pro_frame,orient=VERTICAL)
        scrollx=Scrollbar(pro_frame,orient=HORIZONTAL)

        self.Product_table =ttk.Treeview(pro_frame,columns=("PID","Category","Supplier","Name","Price","Quantity","Status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.Product_table.xview)
        scrolly.config(command=self.Product_table.yview)
        self.Product_table.heading("PID",text="PID")
        self.Product_table.heading("Category",text="Category")
        self.Product_table.heading("Supplier",text="Supplier")
        self.Product_table.heading("Name",text="Name")
        self.Product_table.heading("Price",text="Price")
        self.Product_table.heading("Quantity",text="Quantity")
        self.Product_table.heading("Status",text="Status")
        self.Product_table["show"]="headings"

        self.Product_table.column("PID",width=90)
        self.Product_table.column("Category",width=90)
        self.Product_table.column("Supplier",width=90)
        self.Product_table.column("Name",width=90)
        self.Product_table.column("Price",width=90)
        self.Product_table.column("Quantity",width=90)
        self.Product_table.column("Status",width=90)
        self.Product_table.pack(fill=BOTH,expand=1)
        self.Product_table.bind("<ButtonRelease-1>",self.getdata)

        self.show()
        


#___________________________________________________________________________________________________



    def fetch_cat_supp(self):
        self.cat_list.append("Empty")
        self.supp_list.append("Empty")
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select Name from category")
            cat =cur.fetchall()
            
            if len(cat)>0:
                del self.cat_list[:]
                self.cat_list.append("Select")
                    
                for i in cat:
                    self.cat_list.append(i[0])

            cur.execute("Select Name from supplier")
            supp =cur.fetchall()
            
            if len(supp)>0:
                del self.supp_list[:]
                self.supp_list.append("Select")
                    
                for i in supp:
                    self.supp_list.append(i[0])


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)


    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_category.get()=="Select" or self.var_supplier.get()=="Select" or self.var_name.get()=="":
                messagebox.showerror("Error","All feilds must be required",parent=self.root)
            else:
                cur.execute("Select * from product where Name=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Product Already present,Try diffrent",parent=self.root)
                else:
                    cur.execute("Insert into product (Category,Supplier,Name,Price,Quantity,Status) values(?,?,?,?,?,?)",(
                        self.var_category.get(),
                        self.var_supplier.get(),
                        self.var_name.get(),
                        self.var_price.get(),
                        self.var_qty.get(),
                        self.var_status.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Product Added successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)


    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select * from product")
            rows=cur.fetchall()
            self.Product_table.delete(*self.Product_table.get_children())
            for row in rows:
                self.Product_table.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)


    def getdata(self,ev):
        f=self.Product_table.focus()
        content=(self.Product_table.item(f))
        row=content['values']
        self.var_pid.set(row[0]),
        self.var_category.set(row[1]),
        self.var_supplier.set(row[2]),
        self.var_name.set(row[3]),
        self.var_price.set(row[4]),
        self.var_qty.set(row[5]),
        self.var_status.set(row[6]),
        


    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_pid.get()=="":
                messagebox.showerror("Error","Please select product from list",parent=self.root)
            else:
                cur.execute("Select * from product where PID=?",(self.var_pid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","This Product is Invalid",parent=self.root)
                else:
                    cur.execute("Update product set Category=?,Supplier=?,Name=?,Price=?,Quantity=?,Status=? where PID=?",(
                        
                        self.var_category.get(),
                        self.var_supplier.get(),
                        self.var_name.get(),
                        self.var_price.get(),
                        self.var_qty.get(),
                        self.var_status.get(),
                        self.var_pid.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Product Updated successfully",parent=self.root)
                    self.clear()
                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)

    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_pid.get()=="":
                messagebox.showerror("Error","Select product from the list",parent=self.root)
            else:
                cur.execute("Select * from product where PID=?",(self.var_pid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","This Product is Invalid",parent=self.root)
                else:
                    op=messagebox.askyesno("Error","Do you want to delete?",parent=self.root)
                    if op==TRUE:
                        cur.execute("Delete from product where PID=?",(self.var_pid.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Product Deleted Successfully",parent=self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)

    def clear(self):
        self.var_category.set("Select"),
        self.var_supplier.set("Select"),
        self.var_name.set(""),
        self.var_price.set(""),
        self.var_qty.set(""),
        self.var_status.set("Active"),
        self.var_pid.set(""),
        self.var_searchby.set("Select")
        self.var_searchtext.set("")
        self.show()

    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select search by option",parent=self.root)
            elif self.var_searchtext.get()=="":
                messagebox.showerror("Error","Search input should be required",parent=self.root)
            else:
                cur.execute("Select * from product where "+self.var_searchby.get()+"  LIKE  '%"+self.var_searchtext.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.Product_table.delete(*self.Product_table.get_children())
                    for row in rows:
                        self.Product_table.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found!!!",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
        

if __name__=="__main__":
    root = Tk()
    obj = productclass(root)
    root.mainloop()
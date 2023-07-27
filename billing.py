from cProfile import label
from cgitb import text
from email import message_from_string
from tkinter import *
from tkinter import font , font
from turtle import bgcolor, width
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
import time
import os
import tempfile

class BillClass:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Inventory Management System   |   Developed by ANISH")
        self.root.config(bg="White")

        
        self.var_Cname = StringVar()
        self.var_Ccontact = StringVar()
        self.cart_list=[]
        self.chk_print = 0
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

        #______Product_Frame___
        self.var_search = StringVar()
        productframe1 = Frame(self.root,bd=3,relief=RIDGE,bg="white")
        productframe1.place(x=6,y=120,width=500,height=685)

        pTitle = Label(productframe1,text="All Products",font=("Consolas",25,"bold"), bg="#87cefa",fg="dark blue").pack(side=TOP, fill=X)
        
        productframe2 = Frame(productframe1,bd=2,relief=RIDGE,bg="white")
        productframe2.place(x=3,y=47,width=488,height=140)

        F2_label = Label(productframe2,text="Search Products | By Name",font=("Franklin Gothic",16,"bold"),fg="#006600",bg="white").place(x=2,y=2)
        F2_button1 = Button(productframe2,text="Show All",command=self.show,cursor = "hand2",font=("Consolas",15,"bold"),fg="white",bg="#990033").place(x=355,y=4,height=25,width=125)

        F2_button2 = Button(productframe2,text="Search",command=self.search,cursor = "hand2",font=("Consolas",15,"bold"),fg="white",bg="#996633").place(x=355,y=90,height=25,width=125)

        F2_label = Label(productframe2,text="Product Name",font=("Franklin Gothic",17,"bold"),fg="black",bg="white").place(x=4,y=57)
        F2_text = Entry(productframe2,textvariable=self.var_search,font=("Franklin Gothic",16,"bold"),fg="black",bg="light gray").place(x=4,y=90,width=330)
        

        product_frame = Frame(productframe1,bd=3,relief=RIDGE)
        product_frame.place(x=2,y=190,width=490,height=450)

        scrolly=Scrollbar(product_frame,orient=VERTICAL)
        scrollx=Scrollbar(product_frame,orient=HORIZONTAL)

        self.productTable =ttk.Treeview(product_frame,columns=("PID","Name","Price","Quantity","Status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.productTable.xview)
        scrolly.config(command=self.productTable.yview)

        self.productTable.heading("PID",text="PID")
        self.productTable.heading("Name",text="Name")
        self.productTable.heading("Price",text="Price")
        self.productTable.heading("Quantity",text="Quantity")
        self.productTable.heading("Status",text="Status")
        self.productTable["show"]="headings"

        self.productTable.column("PID",width=20)
        self.productTable.column("Name",width=20)
        self.productTable.column("Price",width=20)
        self.productTable.column("Quantity",width=20)
        self.productTable.column("Status",width=20)
        self.productTable.pack(fill=BOTH,expand=1)
        self.productTable.bind("<ButtonRelease-1>",self.getdata)

        # self.show()
        lvl_notes = Label(productframe1,text="Note : Enter 0 Quantity to remove Product from cart",font=("Consolas",12,"bold"),bg="White",fg="Red").pack(side=BOTTOM,fill=X)


        #_____________________CUSTOMER FRAME__________________

        Customerframe1 = Frame(self.root,bd=3,relief=RIDGE,bg="white")
        Customerframe1.place(x=510,y=120,width=500,height=685)

        CTitle = Label(Customerframe1,text="Customer Details",font=("Consolas",25,"bold"), bg="#87cefa",fg="dark blue").pack(side=TOP, fill=X)

        C_label = Label(Customerframe1,text="Name : ",font=("Franklin Gothic",17,"bold"),fg="black",bg="white").place(x=4,y=57)
        C_text = Entry(Customerframe1,textvariable=self.var_Cname,font=("Franklin Gothic",15,"bold"),fg="black",bg="light gray").place(x=85,y=58)
         
        C1_label = Label(Customerframe1,text="Contact No : ",font=("Franklin Gothic",17,"bold"),fg="black",bg="white").place(x=4,y=97)
        C1_text = Entry(Customerframe1,textvariable=self.var_Ccontact,font=("Franklin Gothic",15,"bold"),fg="black",bg="light gray").place(x=150,y=97)

        customer_frame = Frame(Customerframe1,bd=3,relief=RIDGE)
        customer_frame.place(x=2,y=135,width=490,height=300)

        self.CTitle = Label(customer_frame,text="CART--------TOTAL PRODUCTS : [0]",font=("Consolas",17,"bold"), bg="light yellow",fg="dark violet")
        self.CTitle.pack(side=TOP, fill=X)

        scrolly=Scrollbar(customer_frame,orient=VERTICAL)
        scrollx=Scrollbar(customer_frame,orient=HORIZONTAL)

        self.cartproTable =ttk.Treeview(customer_frame,columns=("PID","Name","Price","QTY"),yscrollcommand=scrolly.set,xscrollcommand=scrollx)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.cartproTable.xview)
        scrolly.config(command=self.cartproTable.yview)

        self.cartproTable.heading("PID",text="PID")
        self.cartproTable.heading("Name",text="Name")
        self.cartproTable.heading("Price",text="Price")
        self.cartproTable.heading("QTY",text="QTY")
        self.cartproTable["show"]="headings"

        self.cartproTable.column("PID",width=20)
        self.cartproTable.column("Name",width=20)
        self.cartproTable.column("Price",width=20)
        self.cartproTable.column("QTY",width=20)
        self.cartproTable.pack(fill=BOTH,expand=1)
        self.cartproTable.bind("<ButtonRelease-1>",self.getdata_cart)

#___________________________________________________________
        Customerframe2 = Frame(Customerframe1,bd=2,relief=RIDGE,bg="white")
        Customerframe2.place(x=3,y=440,width=488,height=230)
        self.var_cus_pid = StringVar()
        self.var_cus_name = StringVar()
        self.var_cus_price = StringVar()
        self.var_cus_qty = StringVar()
        self.var_stock = StringVar()

        lbl_pname = Label(Customerframe2,text="Product Name",font=("Franklin Gothic",15,"bold"),fg="black",bg="white").place(x=4,y=5)
        txt_pname = Entry(Customerframe2,textvariable=self.var_cus_name,font=("Franklin Gothic",15,"bold"),fg="black",bg="light gray").place(x=150,y=5)

        lbl_price = Label(Customerframe2,text="Price Per Qty",font=("Franklin Gothic",15,"bold"),fg="black",bg="white").place(x=4,y=50)
        txt_price = Entry(Customerframe2,textvariable=self.var_cus_price,font=("Franklin Gothic",15,"bold"),fg="black",bg="light gray").place(x=150,y=50)

        lbl_qtyy = Label(Customerframe2,text="Quantity",font=("Franklin Gothic",15,"bold"),fg="black",bg="white").place(x=4,y=95)
        txt_qtyy = Entry(Customerframe2,textvariable=self.var_cus_qty,font=("Franklin Gothic",15,"bold"),fg="black",bg="light gray").place(x=150,y=95)

        self.lbl_inStock = Label(Customerframe2,text="In Stock",font=("Franklin Gothic",15,"bold"),fg="black",bg="white")
        self.lbl_inStock.place(x=4,y=135)

        btn_clear=Button(Customerframe2,text="Clear",command=self.clear_cart,font=("Consolas",15,"bold"),bg="#996633",cursor="hand2",fg="white").place(x=100,y=190,height=30,width=110)
        btn_update_add =Button(Customerframe2,text="Add | Update Cart",command=self.add_update_cart,font=("Consolas",15,"bold"),bg="#990033",cursor="hand2",fg="white").place(x=225,y=190,height=30,width=250)

        #_______BILLING AREA __________

        billframe1 = Frame(self.root,bd=3,relief=RIDGE,bg="white")
        billframe1.place(x=1015,y=120,width=515,height=500)

        BTitle = Label(billframe1,text="Customer Bill",font=("Consolas",19,"bold"), bg="red",fg="white").pack(side=TOP, fill=X)
        scrolly = Scrollbar(billframe1,orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill=Y)

        self.txt_bill_area = Text(billframe1,yscrollcommand=scrolly.set)
        self.txt_bill_area.pack(fill=BOTH,expand=1)
        scrolly.config(command=self.txt_bill_area.yview)

        #___________BILLING BUTTONS___________

        billframe2 = Frame(self.root,bd=3,relief=RIDGE,bg="white")
        billframe2.place(x=1015,y=620,width=515,height=183)

        #_____LABELS
        self.lbl_amount = Label(billframe2,text='Bill Amount\n[0]',font=("Consolas",14,"bold"),fg="black",bg="yellow")
        self.lbl_amount.place(x=2,y=4,width=160,height=70)

        self.lbl_discount = Label(billframe2,text='Discount\n[5%]',font=("Consolas",14,"bold"),fg="black",bg="yellow")
        self.lbl_discount.place(x=172,y=4,width=160,height=70)

        self.lbl_net_pay = Label(billframe2,text='Net Payment\n[0]',font=("Consolas",14,"bold"),fg="black",bg="yellow")
        self.lbl_net_pay.place(x=342,y=4,width=160,height=70)

        #_____BUTTONS
        btn_print = Button(billframe2,text="Print",command = self.print_bill,font=("Consolas",15,"bold"),bg="yellow",cursor="hand2",fg="black")
        btn_print.place(x=2,y=100,height=70,width=160)

        btn_clear = Button(billframe2,text="Clear",command=self.clear_all,font=("Consolas",15,"bold"),bg="yellow",cursor="hand2",fg="black")
        btn_clear.place(x=172,y=100,height=70,width=160)

        btn_generate = Button(billframe2,text="Generate\nBill",command=self.generate_bill,font=("Consolas",15,"bold"),bg="yellow",cursor="hand2",fg="black")
        btn_generate.place(x=342,y=100,height=70,width=160)

        # btn_print=Button(billframe2,text="Print",font=("Consolas",15,"bold"),bg="yellow",cursor="hand2",fg="black").place(x=2,y=100,height=70,width=160)
        # btn_clear=Button(billframe2,text="Clear",font=("Consolas",15,"bold"),bg="yellow",cursor="hand2",fg="black").place(x=172,y=100,height=70,width=160)
        # btn_generate=Button(billframe2,text="Generate\nBill",font=("Consolas",15,"bold"),bg="yellow",cursor="hand2",fg="black").place(x=342,y=100,height=70,width=160)
        

        self.show()
        # self.bill_top()
        self.update_date_time()
#_________________ALL FUNCCTIONS___________________



    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
                # self.productTable =ttk.Treeview(product_frame,columns=("PID","Name","Price","QTY","Status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx)
            cur.execute("Select PID,Name,Price,Quantity,Status from product where Status = 'Active'")
            rows=cur.fetchall()
            self.productTable.delete(*self.productTable.get_children())
            for row in rows:
                self.productTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)

    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_search.get()=="":
                messagebox.showerror("Error","Search input should be required",parent=self.root)
            else:
                cur.execute("Select PID,Name,Price,Quantity,Status from product where Name LIKE  '%"+self.var_search.get()+"%' and Status='Active'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.productTable.delete(*self.productTable.get_children())
                    for row in rows:
                        self.productTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found!!!",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)

    def getdata(self,ev):
        f=self.productTable.focus()
        content=(self.productTable.item(f))
        row=content['values']
        self.var_cus_pid.set(row[0])
        self.var_cus_name.set(row[1])
        self.var_cus_price.set(row[2])
        self.lbl_inStock.config(text=f"In Stock [{str(row[3])}]")
        self.var_stock.set(row[3])
        self.var_cus_qty.set('1')
        
    def getdata_cart(self,ev):
        f=self.cartproTable.focus()
        content=(self.cartproTable.item(f))
        row=content['values']
        self.var_cus_pid.set(row[0])
        self.var_cus_name.set(row[1])
        self.var_cus_price.set(row[2])
        self.var_cus_qty.set(row[3])
        self.lbl_inStock.config(text=f"In Stock [{str(row[4])}]")
        self.var_stock.set(row[4])
        

    def add_update_cart(self):
        if self.var_cus_pid.get()=='':
            messagebox.showerror('Error',"Please Select product from the list!!",parent=self.root)
        elif self.var_cus_qty.get()=='':
            messagebox.showerror('Error',"Quantity is Required!!",parent=self.root)
        elif int(self.var_cus_qty.get())>int(self.var_stock.get()):
            messagebox.showerror('Error',"Invalid Quantity!!",parent=self.root)
        else:
            # price_cal=int(self.var_cus_qty.get())*float(self.var_cus_price.get())
            # price_cal=float(price_cal)
            #     # print(price_cal)PID,Name,Price,Quantity,Stock
            price_cal=self.var_cus_price.get()
            cartdata = [self.var_cus_pid.get(),self.var_cus_name.get(),price_cal,self.var_cus_qty.get(),self.var_stock.get()]
            
            # print(self.cart_list)
            #+UPDATE CART____
            present='no'
            index_=0
            for row in self.cart_list:
                if self.var_cus_pid.get()==row[0]:
                    present='yes'
                    break
                index_+=1

            if present=='yes':
                op=messagebox.askyesno('Confirm',"Product Already present \nDo you want UPDATE | REMOVE from the cart list",parent = self.root)
                if op==True:
                    if self.var_cus_qty.get()=="0":
                        self.cart_list.pop(index_)
                    else:
                        # self.cart_list[index_][2]=price_cal 
                        self.cart_list[index_][3]=self.var_cus_qty.get()
            else:
            # print(present,index_)
                self.cart_list.append(cartdata)
            self.showcart()
            self.bill_update()

    def bill_update(self):
        self.billamt=0
        self.netpay=0
        self.discount = 0
        for row in self.cart_list:
            self.billamt=self.billamt+(float(row[2])*int(row[3]))
        self.discount=(self.billamt*5)/100
        self.netpay=self.billamt-((self.billamt*5)/100)
        self.lbl_amount.config(text=f'Bill Amount\n{str(self.billamt)}')
        self.lbl_net_pay.config(text=f'Net Pay\n{str(self.netpay)}')
        self.CTitle.config(text=f'CART--------TOTAL PRODUCTS : [{str(len(self.cart_list))}]')



    def showcart(self):
        try:
                # self.productTable =ttk.Treeview(product_frame,columns=("PID","Name","Price","QTY","Status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx)
            self.cartproTable.delete(*self.cartproTable.get_children())
            for row in self.cart_list:
                self.cartproTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)

    def generate_bill(self):
        if self.var_Cname.get()=='' or self.var_Ccontact.get()=='':
            messagebox.showerror('Error',f"Customer Detail required!!",parent = self.root)
        elif len(self.cart_list)==0:
            messagebox.showerror('Error',f"Please Add product to the Cart!!",parent = self.root)
        else:
            #____BILL TOP___
            self.bill_top()
            #____BILL MIDDLE___
            self.bill_middle()
            #____BILL BOTTOM___
            self.bill_bottom()

            fp = open(f'bill/{str(self.invoice)}.txt','w')
            fp.write(self.txt_bill_area.get('1.0',END))
            fp.close()
            messagebox.showinfo('Saved',"Bill has been generated.",parent=self.root)
            self.chk_print = 1

    def bill_top(self):
        self.invoice=int(time.strftime("%H%M%S"))+int(time.strftime("%d%m%Y"))
        bill_top_temp = f'''
\t\t\tIMS-Inventory
\t\tPhone No : 889814**** , Mumbai-400043
{str("="*61)}
 Customer Name : {self.var_Cname.get()}
 Phone No : {self.var_Ccontact.get()}
 Bill no : {str(self.invoice)}\t\t\tDate : {str(time.strftime("%d/%m/%Y"))}
{str("="*61)}
 Product Name:\t\t\tQuantity:\t\tPrice:
{str("="*61)}
        '''
        self.txt_bill_area.delete('1.0',END)
        self.txt_bill_area.insert('1.0',bill_top_temp)

    def bill_bottom(self):
        bill_bottom_temp =f'''
{str("="*61)}
 Bill Amount : \t\t\t\t\t Rs. {self.billamt}
 Discount :  \t\t\t\t\t Rs. {self.netpay}
 Net Pay :  \t\t\t\t\t Rs. {self.discount}
{str("="*61)}\n
        '''
        self.txt_bill_area.insert(END,bill_bottom_temp)

    def bill_middle(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            for row in self.cart_list:
                PID = row[0]
                Name = row[1]
                Quantity = int(row[4]) - int(row[3])
                if int(row[3])== int(row[4]):
                    Status = 'Inactive'
                if int(row[3])!= int(row[4]):
                    Status = 'Active'
                Price = float(row[2])*int(row[3])
                Price = str(Price)
                self.txt_bill_area.insert(END,"\n "+Name+"\t\t\t"+row[3]+"\t\t Rs."+ Price)

                cur.execute('Update product set Quantity=?,Status=? where PID=?',(
                    Quantity,
                    Status,
                    PID
                ))
                con.commit()
            con.close()
            self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)


    def clear_cart(self):
        self.var_cus_pid.set('')
        self.var_cus_name.set('')
        self.var_cus_price.set('')
        self.var_cus_qty.set('')
        self.lbl_inStock.config(text=f"In Stock")
        self.var_stock.set('')

    def clear_all(self):
        del self.cart_list[:]
        self.var_Cname.set('')
        self.var_Ccontact.set('')
        self.txt_bill_area.delete('1.0',END)
        self.CTitle.config(text=f'CART--------TOTAL PRODUCTS : [0]')
        self.var_search.set('')
        self.clear_cart()
        self.show()
        self.showcart()
        self.chk_print=0

    def update_date_time(self):
        time_=time.strftime("%I:%M:%S")
        date_=time.strftime("%d/%m/%Y")
        self.lbl_clock.config(text=f"Welcome to Inventory Management System\t\t  Date::{str(date_)}\t\t  Time::{str(time_)}",font=("Constantia"),bg="#808080",fg="white")
        self.lbl_clock.after(200,self.update_date_time)

    def print_bill(self):
        if self.chk_print ==1:
            messagebox.showinfo('Print',"Please wait while printing...",parent = self.root)
            new_file = tempfile.mktemp('.txt')
            open(new_file,'w').write(self.txt_bill_area.get('1.0',END))
            os.startfile(new_file,'print')
        else:
            messagebox.showerror('Print',"Please generate bill, to print the receipt....",parent = self.root)

    def logout(self):
        self.root.destroy()
        os.system("python loginpagee.py")
            

if __name__=="__main__":
    root = Tk()
    obj = BillClass(root)
    root.mainloop()
from cProfile import label
from cgitb import text
from email import message
from tkinter import *
from tkinter import font , font
from tkinter import messagebox
from turtle import title, width
from xmlrpc.server import list_public_methods
from PIL import Image,ImageTk
from tkinter import ttk
import os
class salesclass:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1100x615+410+150")
        self.root.title("Inventory Management System   |   Developed by ANISH")
        self.root.config(bg="White")
        self.root.focus_force()

        self.bill_list=[]
        self.var_invoice=StringVar()


#_____TITLE____
        title = Label(self.root,text="View Customer Bills",font=("Consolas",30,"bold"),bg="#87cefa",fg="dark blue",bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=20)
        lbl_invoice=Label(self.root,text="Invoice No. ",font=("Consolas",15),bg="white").place(x=50,y=100)
        txt_invoice=Entry(self.root,textvariable=self.var_invoice,font=("Consolas",15),bg="#66FFFF").place(x=180,y=100,width=260)

        btn_search = Button(self.root,text="Search",command=self.search,font=("RomanD",10,"bold"),bg="#00CC33",fg="black",cursor="hand2").place(x=460,y=100,width=130,height=25)
        btn_clear = Button(self.root,text="Clear",command=self.clear,font=("RomanD",10,"bold"),bg="#996633",fg="white",cursor="hand2").place(x=600,y=100,width=130,height=25)

#_________BILL LIST_____
        sales_frame = Frame(self.root,bd=3,relief=RIDGE)
        sales_frame.place(x=50,y=150,width=250,height=450)

        scrolly=Scrollbar(sales_frame,orient=VERTICAL)
        self.sales_list=Listbox(sales_frame,font=("RomanD",15),bg="white",yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.sales_list.yview)
        self.sales_list.pack(fill=BOTH,expand=1)
        self.sales_list.bind("<ButtonRelease-1>",self.getdata)

#__________BILL AREA____
        bill_frame = Frame(self.root,bd=3,relief=RIDGE)
        bill_frame.place(x=325,y=150,width=515,height=450)

        title2 = Label(bill_frame,text="Customer Bill Area",font=("Consolas",20,"bold"),bg="#87cefa",fg="dark blue").pack(side=TOP,fill=X)

        scrolly2=Scrollbar(bill_frame,orient=VERTICAL)
        self.bill_area=Text(bill_frame,bg="white",yscrollcommand=scrolly2.set)
        scrolly2.pack(side=RIGHT,fill=Y)
        scrolly2.config(command=self.bill_area.yview)
        self.bill_area.pack(fill=BOTH,expand=1)

#_________SALES IMAGES___________
        
        # self.bill_photo = Image.open("images/sales1.jpg")
        # self.bill_photo = self.bill_photo.resize((350,550),Image.ANTIALIAS)
        # self.bill_photo = ImageTk.PhotoImage(self.bill_photo)

        # lbl_image=Label(self.root,image=self.bill_photo,bd=0)
        # lbl_image.place(x=740,y=80)

        self.show()
#________________________________________________________
    
    def show(self):
        del self.bill_list[:]
        self.sales_list.delete(0,END)
        for i in os.listdir('bill'):
            if i.split('.')[-1]=='txt':
                self.sales_list.insert(END,i)
                self.bill_list.append(i.split('.')[0])
    def getdata(self,ev):
        index_=self.sales_list.curselection()
        file_name=self.sales_list.get(index_)
        # print(file_name)
        self.bill_area.delete('1.0',END)
        fp=open(f'bill/{file_name}','r')
        for i in fp:
            self.bill_area.insert(END,i)
        fp.close()

    def search(self):
        if self.var_invoice.get()=="":
            messagebox.showerror("Error","Invoice No. should be required",parent=self.root)
        else:
            if self.var_invoice.get() in self.bill_list:
                fp=open(f'bill/{self.var_invoice.get()}.txt','r')
                self.bill_area.delete('1.0',END)
                for i in fp:
                  self.bill_area.insert(END,i)
                fp.close()
            else:
                messagebox.showerror("Error","Invalid Invoice No.",parent=self.root)

   
    def clear(self):
        self.show()
        self.bill_area.delete('1.0',END)




if __name__=="__main__":
    root = Tk()
    obj = salesclass(root)
    root.mainloop()
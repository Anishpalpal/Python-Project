from cgitb import text
from msilib.schema import SelfReg
from sys import builtin_module_names
from tkinter import *
from tkinter import font , font
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import ttk
import sqlite3


class categoryclass:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1100x615+410+150")
        self.root.title("Inventory Management System   |   Developed by ANISH")
        self.root.config(bg="White")
        self.root.focus_force()

        self.var_cat_id=StringVar()
        self.var_name=StringVar()



    #======TITLES======

        lbl_title=Label(self.root,text="Manage Product Category",font=("Consolas",30,"bold"), bg="#87cefa",fg="dark blue",bd=3,relief=RIDGE).pack(side=TOP, fill=X,padx=10,pady=20)
        lbl_name=Label(self.root,text="Enter Category Name", font=("Consolas",20), bg="white",).place(x=50,y=100)
        text_name=Entry(self.root,textvariable=self.var_name, font=("Consolas",20), bg="#66FFFF",).place(x=55,y=140,width=300)

        btn_add=Button(self.root,text="Add",font=("Consolas",15,"bold"),command=self.add,bg="#0066FF",cursor="hand2").place(x=370,y=140,height=35,width=120)
        btn_delete=Button(self.root,text="Delete",font=("Consolas",15,"bold"),command=self.delete,bg="#990033",cursor="hand2",fg="white").place(x=505,y=140,height=35,width=120)

        #_______CATEGORY IMAGES______
        self.category_photo = Image.open("images/categoryy.jpg")
        self.category_photo = self.category_photo.resize((650,450),Image.ANTIALIAS)
        self.category_photo = ImageTk.PhotoImage(self.category_photo)

        lbl_image=Label(self.root,image=self.category_photo,bd=0)
        lbl_image.place(x=10,y=180)

#___________FRAMES_________
        
        category_frame = Frame(self.root,bd=3,relief=RIDGE)
        category_frame.place(x=680,y=100,width=400,height=500)

        scrolly=Scrollbar(category_frame,orient=VERTICAL)
        scrollx=Scrollbar(category_frame,orient=HORIZONTAL)

        self.categoryTable =ttk.Treeview(category_frame,columns=("CID","Name"),yscrollcommand=scrolly.set,xscrollcommand=scrollx)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.categoryTable.xview)
        scrolly.config(command=self.categoryTable.yview)

        self.categoryTable.heading("CID",text="CID")
        self.categoryTable.heading("Name",text="Name")
        self.categoryTable["show"]="headings"

        self.categoryTable.column("CID",width=90)
        self.categoryTable.column("Name",width=90)
        self.categoryTable.pack(fill=BOTH,expand=1)
        self.categoryTable.bind("<ButtonRelease-1>",self.getdata)        

        self.show()


#_______________________________________________________________________________________________


    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error","Category Name should be required",parent=self.root)
            else:
                cur.execute("Select * from category where Name=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Category already present,try diffrent",parent=self.root)
                else:
                    cur.execute("Insert into category (Name) values(?)",(self.var_name.get(),))
                    con.commit()
                    messagebox.showinfo("Success","Category Added successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)


    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select * from category")
            rows=cur.fetchall()
            self.categoryTable.delete(*self.categoryTable.get_children())
            for row in rows:
                self.categoryTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)

    def getdata(self,ev):
        f=self.categoryTable.focus()
        content=(self.categoryTable.item(f))
        row=content['values']
        # print(row)
        self.var_cat_id.set(row[0])
        self.var_name.set(row[1])


    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_cat_id.get()=="":
                messagebox.showerror("Error","Please select Category from the list",parent=self.root)
            else:
                cur.execute("Select * from category where CID=?",(self.var_cat_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","TPlease try again",parent=self.root)
                else:
                    op=messagebox.askyesno("Error","Do you want to delete?",parent=self.root)
                    if op==TRUE:
                        cur.execute("Delete from category where CID=?",(self.var_cat_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Category Deleted Successfully",parent=self.root)
                        self.show()
                        self.var_cat_id.set("")
                        self.var_name.set("")
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)



if __name__=="__main__":
    root = Tk()
    obj = categoryclass(root)
    root.mainloop()



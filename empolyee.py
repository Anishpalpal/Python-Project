from cProfile import label
from cgitb import text
from tkinter import *
from tkinter import font , font
from turtle import title, width
# from typing_extensions import Self
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3

from numpy import meshgrid
class employeeclass:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1100x615+410+150")
        self.root.title("Inventory Management System   |   Developed by ANISH")
        self.root.config(bg="White")
        self.root.focus_force()

        #_____ALL VARIABLES____
        self.var_searchby=StringVar()
        self.var_searchtext=StringVar()

        self.var_emp_id=StringVar()
        self.var_gender=StringVar()
        self.var_cantact=StringVar()
        self.var_name=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_email=StringVar()
        self.var_pass=StringVar()
        self.var_utype=StringVar()
        self.var_salary=StringVar()



        #____search frame__
        Searchframe = LabelFrame(self.root,text="Search Employee",font=("RomanD",10,"bold"),bd=2,relief=RIDGE,bg="White")
        Searchframe.place(x=250,y=30,width=600,height=70)

        #___option__
        cmb_search = ttk.Combobox(Searchframe,textvariable=self.var_searchby,values=("Select","Email","Name","Contact"),state="readonly",justify=CENTER,font=("RomanD",10,"bold"))
        cmb_search.place(x=10,y=10,width=150)
        cmb_search.current(0)

        txt_search = Entry(Searchframe,textvariable=self.var_searchtext,font=("RomanD",10,"bold"),bg="#66FFFF").place(x=170,y=10,width=250)
        btn_search = Button(Searchframe,text="Search",command=self.search,font=("RomanD",10,"bold"),bg="#00CC33",fg="black",cursor="hand2").place(x=430,y=10,width=150,height=22)

        #______title_____
        title= Label(self.root,text="Employee Details",font=("Gadugi",17,"bold"),bg="#9900FF",fg="white").place(x=50,y=110,width=1000)


        #____Content___
#ROW1
        lbl_empid= Label(self.root,text="Emp ID",font=("Franklin Gothic",15),bg="white").place(x=50,y=160)
        lbl_gender= Label(self.root,text="Gender",font=("Franklin Gothic",15),bg="white").place(x=400,y=160)
        lbl_contact= Label(self.root,text="Contact",font=("Franklin Gothic",15),bg="white").place(x=750,y=160)
        
        txt_empid=Entry(self.root,textvariable=self.var_emp_id,font=("Franklin Gothic",15),bg="#66FFFF").place(x=140,y=160,width=180)
        # txt_gender=Entry(self.root,textvariable=self.var_gender,font=("Franklin Gothic",15),bg="white").place(x=500,y=155,width=180)
        cmb_gender = ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female"),state="readonly",justify=CENTER,font=("RomanD",12,"bold"))
        cmb_gender.place(x=490,y=160,width=180)
        cmb_gender.current(0)

        txt_contact= Entry(self.root,textvariable=self.var_cantact,font=("Franklin Gothic",15),bg="#66FFFF").place(x=840,y=160,width=180)
#ROW2
        lbl_name= Label(self.root,text="Name",font=("Franklin Gothic",15),bg="white").place(x=50,y=200)
        lbl_dob= Label(self.root,text="D.O.B",font=("Franklin Gothic",15),bg="white").place(x=400,y=200)
        lbl_doj= Label(self.root,text="D.O.J",font=("Franklin Gothic",15),bg="white").place(x=750,y=200)
        
        txt_name=Entry(self.root,textvariable=self.var_name,font=("Franklin Gothic",15),bg="#66FFFF").place(x=140,y=200,width=180)
        txt_dob=Entry(self.root,textvariable=self.var_dob,font=("Franklin Gothic",15),bg="#66FFFF").place(x=490,y=200,width=180)
        txt_doj= Entry(self.root,textvariable=self.var_doj,font=("Franklin Gothic",15),bg="#66FFFF").place(x=840,y=200,width=180)
#ROW3
        lbl_email= Label(self.root,text="Email",font=("Franklin Gothic",15),bg="white").place(x=50,y=240)
        lbl_password= Label(self.root,text="Password",font=("Franklin Gothic",15),bg="white").place(x=400,y=240)
        lbl_utype= Label(self.root,text="User Type",font=("Franklin Gothic",15),bg="white").place(x=750,y=240)
        
        
        txt_email=Entry(self.root,textvariable=self.var_email,font=("Franklin Gothic",15),bg="#66FFFF").place(x=140,y=240,width=180)
        txt_password=Entry(self.root,textvariable=self.var_pass,font=("Franklin Gothic",15),bg="#66FFFF").place(x=510,y=240,width=180)
        # txt_utype= Entry(self.root,textvariable=self.var_utype,font=("Franklin Gothic",15),bg="#66FFFF").place(x=860,y=235,width=180)
        cmb_utype = ttk.Combobox(self.root,textvariable=self.var_utype,values=("Admin","Employee"),state="readonly",justify=CENTER,font=("RomanD",12,"bold"))
        cmb_utype.place(x=860,y=240,width=180)
        cmb_utype.current(0)
#ROW4
        lbl_address= Label(self.root,text="Address",font=("Franklin Gothic",15),bg="white").place(x=50,y=280)
        lbl_salary= Label(self.root,text="Salary",font=("Franklin Gothic",15),bg="white").place(x=450,y=280)

        self.txt_address=Text(self.root,font=("Franklin Gothic",15),bg="#66FFFF")
        self.txt_address.place(x=140,y=280,width=250,height=80)
        txt_salary=Entry(self.root,textvariable=self.var_salary,font=("Franklin Gothic",15),bg="#66FFFF").place(x=520,y=280,width=180)

        #_____BUTTONs____
        btn_add=Button(self.root,text="Save",command=self.add,font=("Consolas",15,"bold"),bg="#0066FF",cursor="hand2").place(x=450,y=330,height=30,width=120)
        btn_update=Button(self.root,text="Update",command=self.update,font=("Consolas",15,"bold"),bg="#0099CC",cursor="hand2").place(x=610,y=330,height=30,width=110)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("Consolas",15,"bold"),bg="#990033",cursor="hand2",fg="white").place(x=760,y=330,height=30,width=110)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("Consolas",15,"bold"),bg="#996633",cursor="hand2",fg="white").place(x=910,y=330,height=30,width=110)

        #___EMPOLYEE DETAIL___

        emp_frame = Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=380,relwidth=1,height=233)

        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)

        self.EmployeeTable =ttk.Treeview(emp_frame,columns=("EID","Name","Email","Gender","Contact","DOB","DOJ","Password","Usertype","Address","Salary"),yscrollcommand=scrolly.set,xscrollcommand=scrollx)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)
        self.EmployeeTable.heading("EID",text="EID")
        self.EmployeeTable.heading("Name",text="Name")
        self.EmployeeTable.heading("Email",text="Email")
        self.EmployeeTable.heading("Gender",text="Gender")
        self.EmployeeTable.heading("Contact",text="Contact")
        self.EmployeeTable.heading("DOB",text="DOB")
        self.EmployeeTable.heading("DOJ",text="DOJ")
        self.EmployeeTable.heading("Password",text="Password")
        self.EmployeeTable.heading("Usertype",text="User type")
        self.EmployeeTable.heading("Address",text="Address")
        self.EmployeeTable.heading("Salary",text="Salary")
        self.EmployeeTable["show"]="headings"

        self.EmployeeTable.column("EID",width=90)
        self.EmployeeTable.column("Name",width=90)
        self.EmployeeTable.column("Email",width=90)
        self.EmployeeTable.column("Gender",width=90)
        self.EmployeeTable.column("Contact",width=90)
        self.EmployeeTable.column("DOB",width=90)
        self.EmployeeTable.column("DOJ",width=90)
        self.EmployeeTable.column("Password",width=90)
        self.EmployeeTable.column("Usertype",width=90)
        self.EmployeeTable.column("Address",width=90)
        self.EmployeeTable.column("Salary",width=90)
        self.EmployeeTable.pack(fill=BOTH,expand=1)
        self.EmployeeTable.bind("<ButtonRelease-1>",self.getdata)

        self.show()

#___________________________________________________________________________________________________

    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID must be required",parent=self.root)
            else:
                cur.execute("Select * from empolyee where EID=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Employee ID is already assinged,try diffrent",parent=self.root)
                else:
                    cur.execute("Insert into empolyee (EID,Name,Email,Gender,Contact,DOB,DOJ,Password,Usertype,Address,Salary) values(?,?,?,?,?,?,?,?,?,?,?)",(
                        self.var_emp_id.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_cantact.get(),
                        self.var_dob.get(),
                        self.var_doj.get(),
                        self.var_pass.get(),
                        self.var_utype.get(),
                        self.txt_address.get('1.0',END),
                        self.var_salary.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Employee Added successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)


    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select * from empolyee")
            rows=cur.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
                self.EmployeeTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)


    def getdata(self,ev):
        f=self.EmployeeTable.focus()
        content=(self.EmployeeTable.item(f))
        row=content['values']
        # print(row)
        self.var_emp_id.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_cantact.set(row[4])
        self.var_dob.set(row[5])
        self.var_doj.set(row[6])
        self.var_pass.set(row[7])
        self.var_utype.set(row[8])
        self.txt_address.delete('1.0',END),
        self.txt_address.insert(END,row[9]),
        self.var_salary.set(row[10])


    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID must be required",parent=self.root)
            else:
                cur.execute("Select * from empolyee where EID=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","This Employee ID is Invalid",parent=self.root)
                else:
                    cur.execute("Update empolyee set Name=?,Email=?,Gender=?,Contact=?,DOB=?,DOJ=?,Password=?,Usertype=?,Address=?,Salary=? where EID=?",(
                        
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_cantact.get(),
                        self.var_dob.get(),
                        self.var_doj.get(),
                        self.var_pass.get(),
                        self.var_utype.get(),
                        self.txt_address.get('1.0',END),
                        self.var_salary.get(),
                        self.var_emp_id.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Employee Updated successfully",parent=self.root)
                    self.clear()
                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)

    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID must be required",parent=self.root)
            else:
                cur.execute("Select * from empolyee where EID=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","This Employee ID is Invalid",parent=self.root)
                else:
                    op=messagebox.askyesno("Error","Do you want to delete?",parent=self.root)
                    if op==TRUE:
                        cur.execute("Delete from empolyee where EID=?",(self.var_emp_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Employee Deleted Successfully",parent=self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)

    def clear(self):
        self.var_emp_id.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_cantact.set("")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_pass.set("")
        self.var_utype.set("Admin")
        self.txt_address.delete('1.0',END),
        self.var_salary.set("")
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
                cur.execute("Select * from empolyee where "+self.var_searchby.get()+"  LIKE  '%"+self.var_searchtext.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                    for row in rows:
                        self.EmployeeTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found!!!",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
        



if __name__=="__main__":
    root = Tk()
    obj = employeeclass(root)
    root.mainloop()
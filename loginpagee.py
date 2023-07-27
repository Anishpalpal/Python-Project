from tkinter import *
from tokenize import String
from PIL import Image,ImageTk
import sqlite3
from tkinter import messagebox
import os
import email_pass
import smtplib
import time

class IMS:
    def __init__(self,root):
        self.root = root
        self.root.geometry("650x500+450+180")
        self.root.title("Inventory Management System   |   Developed by ANISH")
        self.root.config(bg="White")

        self.otp=''

        self.employeeID = StringVar()
        self.password = StringVar()

        Userframe = LabelFrame(self.root,text="Login",font=("RomanD",10,"bold"),bd=2,relief=RIDGE,bg="White")
        Userframe.place(x=10,y=10,width=625,height=480)

        lbl_user= Label(Userframe,text="Employee ID",font=("Franklin Gothic",15),bg="white").place(x=20,y=20)
        txt_user=Entry(Userframe,textvariable=self.employeeID,font=("Franklin Gothic",15),bg="#ECECEC").place(x=25,y=50,width=180)

        lbl_pswd= Label(Userframe,text="Password",font=("Franklin Gothic",15),bg="white").place(x=20,y=90)
        txt_pswd=Entry(Userframe,textvariable=self.password,show="*",font=("Franklin Gothic",15),bg="#ECECEC").place(x=25,y=120,width=180)
        

        btn_Login = Button(Userframe,text="LOGIN",command = self.loginn,font=("RomanD",10,"bold"),bg="#00CC33",fg="black",cursor="hand2").place(x=40,y=165,width=130,height=25)
        
        lbl_or= Label(Userframe,text="------------ OR --------------",font=("Franklin Gothic",15),bg="white").place(x=2,y=200)

        btn_forget = Button(Userframe,text="Forget Password ?",command=self.forget_window,font=("RomanD",10,"bold"),bg="white",fg="black",cursor="hand2",bd= 0,activebackground="white").place(x=20,y=250,width=200,height=25)
        
        self.bill_photo = Image.open("images/sales1.jpg")
        self.bill_photo = self.bill_photo.resize((400,450),Image.ANTIALIAS)
        self.bill_photo = ImageTk.PhotoImage(self.bill_photo)

        lbl_image=Label(Userframe,image=self.bill_photo,bd=0)
        lbl_image.place(x=220,y=0)

        # self.send_email('pal40417@gmail.com')


#_______________ALL FUNCTION_______________


    def loginn(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.employeeID.get()=="" or self.password.get()=="":
                messagebox.showerror("Error","All feild are required!!",parent = self.root)
            else:
                cur.execute("select Usertype from empolyee where EID=? AND Password=?",(self.employeeID.get(),self.password.get()))
                user = cur.fetchone()
                if user==None:
                    messagebox.showerror("Error","Invalid USERNAME / PASSWORD!!",parent = self.root)
                else:
                    if user[0]=="Admin":
                        self.root.destroy()
                        os.system("python dashboard.py")
                    else:
                        self.root.destroy()
                        os.system("python billing.py")

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
        # if self.employeeID.get()=="" or self.password.get()=="":
        #     messagebox.showerror("Error","All feild are required!!")
        # elif self.employeeID.get()!="Anish" or self.password.get()!="1234":
        #     messagebox.showerror("Error","Invalid Employee ID and Password!!!\nTry Again with correct credentials.")
        # else:
        #     messagebox.showinfo("Information",f"Welcome : {self.employeeID .get()}\nYour Password : {self.password.get()}")


    def forget_window(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.employeeID.get()=='':
                messagebox.showerror("Error","Employee ID must be required!!",parent = self.root)
            else:
                cur.execute("select Email from empolyee where EID=? ",(self.employeeID.get(),))
                email_ = cur.fetchone()
                if email_==None:
                    messagebox.showerror("Error","Invalid Employee Id , Try again!!!",parent = self.root)
                else:
                    #                                      forgetwindows
                    # call send_email_function()
                    self.var_otp = StringVar()
                    self.var_newpass = StringVar()
                    self.var_confpass = StringVar()
                    chk = self.send_email(email_[0])
                    if chk=='f':
                        messagebox.showerror('Error',"Connection Error , try again",parent=self.root)
                    else:
                        self.forget_win=Toplevel(self.root)
                        self.forget_win.title("RESET PASSWORD")
                        self.forget_win.geometry("393x435+690+233")
                        self.forget_win.config(bg="White")
                        self.forget_win.focus_force()

                        title= Label(self.forget_win,text="Reset Password",font=("Consolas",15,"bold"), bg="#87cefa",fg="dark blue").pack(side=TOP, fill=X)
                        lbl_reset = Label(self.forget_win,text="Enter OTP Sent on Registered Email",font=("Franklin Gothic",13),bg="white").place(x=20,y=60)
                        txt_reset = Entry(self.forget_win,textvariable=self.var_otp,font=("Franklin Gothic",15),bg="#ECECEC").place(x=25,y=90,width=200)


                        lbl_newpass = Label(self.forget_win,text="New Password : ",font=("Franklin Gothic",13),bg="white").place(x=20,y=150)
                        txt_newpass = Entry(self.forget_win,textvariable=self.var_newpass,font=("Franklin Gothic",15),bg="#ECECEC").place(x=25,y=172,width=200)


                        lbl_confpass = Label(self.forget_win,text="Confirm Password : ",font=("Franklin Gothic",13),bg="white").place(x=20,y=205)
                        txt_confpass = Entry(self.forget_win,textvariable=self.var_confpass,font=("Franklin Gothic",15),bg="#ECECEC").place(x=25,y=225,width=200)

                        self.btn_forget = Button(self.forget_win,text="SUBMIT",command=self.validate_otp,font=("RomanD",10,"bold"),bg="blue",fg="white",cursor="hand2",bd=0)
                        self.btn_forget.place(x=235,y=90,height=25,width=100)
            
                        self.btn_update = Button(self.forget_win,text="UPDATE",command=self.update_password,state = DISABLED,font=("RomanD",10,"bold"),bg="blue",fg="white",cursor="hand2",bd=0)
                        self.btn_update.place(x=150,y=260,height=30,width=100)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)

    def update_password(self):
        if self.var_newpass.get()=='' or self.var_confpass.get()=='':
            messagebox.showerror('Error',"Password is Required",parent=self.forget_win)
        elif self.var_newpass.get()!=self.var_confpass.get():
            messagebox.showerror('Error',"New Password and Confirm Password should be same.",parent=self.forget_win)
        else:
            con=sqlite3.connect(database=r'ims.db')
            cur=con.cursor()
            try:
                cur.execute("Update empolyee SET Password=? where EID=?",(self.var_newpass.get(),self.employeeID.get()))
                con.commit()
                messagebox.showinfo("Success","Password Updated Successfully",parent=self.forget_win)
                self.forget_win.destroy()

            except Exception as ex:
                messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)

    def validate_otp(self):
        if int(self.otp)==int(self.var_otp.get()):
            self.btn_update.config(state=NORMAL)
            self.btn_forget.config(state=DISABLED)
        else:
            messagebox.showerror('Error',"Invalid OTP, Try again",parent=self.forget_win)
    def send_email(self,to_):
        s = smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        email_ = email_pass.email_
        pass_ = email_pass.pass_

        s.login(email_,pass_)
        self.otp=int(time.strftime("%H%S%M"))+int(time.strftime("%S"))
        
        subj = 'IMS-Reset Password OTP'
        msg=f"Dear Sir/Madam,\n\nYour Reset OTP is {str(self.otp)}.\n\nWith Regards,\nIMS team"
        msg="Subject : {}\n\n{}".format(subj,msg)
        s.sendmail(email_,to_,msg)
        chk = s.ehlo()
        if chk[0]==250:
            return 's'
        else:
            return 'f'





if __name__=="__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()
from tkinter import * 
from PIL import Image, ImageTk,ImageSequence
from numpy import imag
import time

root = Tk()
root.geometry("1920x1080")

class loginpage:
    # play_gif()
    def play_gif():
        global img
        img = Image.open("Images/loginpage.gif")
        img = Image.open("Images/loginpage.gif")

        Lbl = Label(root)
        Lbl.place(x=350,y=200)

        for img in ImageSequence.Iterator(img):

            img = ImageTk.PhotoImage(img)
            Lbl.config(image=img)
            root.update()
            # time.sleep(5)
    root.after(0,play_gif)
    
    def timeee_gif():
        pass
        

    # btn1 = Button(root,text="Play",command=play_gif()).place(x= 500,y = 200)
root.mainloop()
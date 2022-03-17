#                        By SALIL CHANDAN      ------->   RAILWAY MANAGEMNET SYSTEM 
from tkinter import *
from PIL import Image,ImageTk                      
from cust import Cust_Detail
from res import RES_Detail
from waiti import Waiting
from dept import Department
from train import Train_detail 


class RAILWAY_MANAGMENT:
    def __init__ (self,root):
        self.root=root
        self.root.title("Railway managment system".center(340).upper())
        self.root.geometry("1550x800")  

        self.img1=Image.open("C:\\Users\\asd\\Pictures\\s.jpg")
        self.img1=self.img1.resize((1550,740),Image.ANTIALIAS)
        self.photoImg1=ImageTk.PhotoImage(self.img1)

        self.lb=Label(self.root,image=self.photoImg1,relief=RIDGE)
        self.lb.place(x=0,y=0,width=1550,height=740)
        
        self.lb_t= Label(self.root,text="RAILWAY MANAGMENT SYSTEM",font=("times new roman",40,"bold"),bg="black",fg="gold",relief=RIDGE)
        self.lb_t.place(x=0,y=0,width=1550,height=70)

        self.lb_menu= Label(self.root,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        self.lb_menu.place(x=500,y=100,width=320)
        
        self.cust_btn=Button(text="CUTOMERS DETAILS",command=self.Customers,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        self.cust_btn.place(x=0,y=150,width=320)

        self.cust_btn=Button(text="DEPARTMENT DETAILS",command=self.Dept,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        self.cust_btn.place(x=1000,y=150,width=320)

        self.cust_btn=Button(text="RESERVATION DETAILS",command=self.Reservation,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        self.cust_btn.place(x=0,y=250,width=320)
        
        self.cust_btn=Button(text="WAITING LIST ",command=self.Waiting,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        self.cust_btn.place(x=1000,y=250,width=320)
    
        self.cust_btn=Button(text="TRAIN DETAILS ",command=self.TRAINS,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        self.cust_btn.place(x=500,y=350,width=320)
    
    def Customers(self):
        self.new_window=Toplevel(self.root)              
        self.app=Cust_Detail(self.new_window)

    def Reservation(self):
        self.new_window=Toplevel(self.root)
        self.app=RES_Detail(self.new_window)

    def Waiting(self):
        self.new_window=Toplevel(self.root)
        self.app=Waiting(self.new_window)

    def Dept(self):
        self.new_window=Toplevel(self.root)
        self.app=Department(self.new_window)

    def TRAINS(self):
        self.new_window=Toplevel(self.root)
        self.app=Train_detail(self.new_window)
        

if __name__ == "__main__":
    root=Tk()
    obj=RAILWAY_MANAGMENT(root)
    root.mainloop()





















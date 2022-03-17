from tkinter import *
from PIL import Image, ImageTk
import cx_Oracle
from tkinter import ttk
from tkinter import messagebox

class RES_Detail:
    def __init__(self, root):
        self.root = root
        self.root.title("RESERVATION  DETAIL")
        self.root.geometry("1295x650")

        self.cutomer_id1=StringVar()

        img1 = Image.open(r"C:\\Users\\asd\\Pictures\\s.jpeg")
        img1 = img1.resize((1295, 650), Image.ANTIALIAS)
        self.photoImg1 = ImageTk.PhotoImage(img1)

        lb = Label(self.root, image=self.photoImg1, bd=4, relief=RIDGE)
        lb.place(x=0, y=0, width=1295, height=650)

        lb_t = Label(self.root, text="RESERVATION LIST ", font=(
            "times new roman", 18, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lb_t.place(x=0, y=0, width=1295, height=90)

        cust_btn=Button(self.root,text="LIST",command=self.fetch_data,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        cust_btn.place(x=500,y=150,width=320)

        cust_btn=Button(self.root,text="SEND TO WAIITNG LIST",command=self.del_customer_info,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        cust_btn.place(x=500,y=250,width=320)

    def fetch_data(self):
        con=cx_Oracle.connect("system/salil")
        my_cursor = con.cursor()
        my_cursor.execute("select * from res_detail ")
        tree=ttk.Treeview(self.root,height="60")
        tree.place(x=1500,y=750)
        tree['show']='headings'
        tree["columns"]=("book_seat","tid","cid","ticket")  
        tree.column("book_seat",width=50,anchor=CENTER)
        tree.column("tid",width=50,anchor=CENTER)
        tree.column("cid",width=100,anchor=CENTER)
        tree.column("ticket",width=150,anchor=CENTER)
        
        tree.heading("book_seat",text="BOOKING",anchor=CENTER)
        tree.heading("tid",text="TRAIN ID",anchor=CENTER)
        tree.heading("cid",text="CUSTOMER ID",anchor=CENTER)
        tree.heading("ticket",text="PRICE",anchor=CENTER)
        count=0
        for i in my_cursor:
            tree.insert('',count,text=" ",values=(i[0],i[1] ,i[2], i[3]))
            count=count+1
        tree.pack(fill='x')
    
    def del_customer_info(self):
        lbl=Label(self.root,text="ENTER CUSTOMER ID",font=("arial",12,"bold"),padx=2,pady=6) 
        lbl.place(x=840,y=250,width=220,height=30)
        entry_reff1= ttk.Entry(self.root,textvariable=self.cutomer_id1,font=("arial",12,"bold"),width=20)
        entry_reff1.place(x=840,y=290)
        del_button=Button(self.root,text=" Delete Details",command=self.del_data,font=("times new roman",14,"bold"),bg="black",fg="green",bd=4,relief=RIDGE)
        del_button.place(x=840,y=320,width=220)

    def del_data(self):
        try:
            con=cx_Oracle.connect("system/salil")
            my_cursor = con.cursor()
            s="delete from res_detail where cid = :1"
            a=my_cursor.execute(s,(self.cutomer_id1.get(),))
            con.commit()
            con.close() 
            messagebox.showinfo("message","SUCESSFULLY DELETED",parent=self.root)
        except Exception as E1:
            messagebox.showwarning("Warning",f"NOT DELETED :{str(E1)} ",parent=self.root)


if __name__ == '__main__':
    root = Tk()
    obj = RES_Detail(root)
    root.mainloop()
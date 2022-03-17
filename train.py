from tkinter import *
from PIL import Image, ImageTk
import cx_Oracle
from tkinter import ttk


class Train_detail:
    def __init__(self, root):
        self.root = root
        self.root.title("CUTOMERS DETAIL")
        self.root.geometry("1295x650")

        self.cutomer_id2=StringVar()

        img1 = Image.open(r"C:\\Users\\asd\\Pictures\\t.jpg")
        img1 = img1.resize((1295, 650), Image.ANTIALIAS)
        self.photoImg1 = ImageTk.PhotoImage(img1)

        lb = Label(self.root, image=self.photoImg1, bd=4, relief=RIDGE)
        lb.place(x=0, y=0, width=1295, height=650)

        lb_t = Label(self.root, text=" TRAIN SECHEDULE  ", font=(
            "times new roman", 18, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lb_t.place(x=0, y=0, width=1295, height=90)

        cust_btn=Button(self.root,text=" SEE THE TRAINS ",command=self.fetch_data,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        cust_btn.place(x=0,y=150,width=320)

        cust_btn=Button(self.root,text=" SEE CUSTOMER TIMING ",command=self.search_info,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        cust_btn.place(x=0,y=350,width=320)

    def fetch_data(self):
        con=cx_Oracle.connect("system/salil")
        my_cursor = con.cursor()
        my_cursor.execute("select * from train_detail")
        tree=ttk.Treeview(self.root,height="60")
        tree.place(x=1500,y=750)
        tree['show']='headings'
        tree["columns"]=("tname","tid","arrival_city","destination_city","manno","total_seat","price","time_arrival")  
        tree.column("tname",width=50,anchor=CENTER)
        tree.column("tid",width=50,anchor=CENTER)
        tree.column("arrival_city",width=50,anchor=CENTER)
        tree.column("destination_city",width=50,anchor=CENTER)
        tree.column("manno",width=100,anchor=CENTER)
        tree.column("total_seat",width=50,anchor=CENTER)
        tree.column("price",width=50,anchor=CENTER)
        tree.column("time_arrival",width=150,anchor=CENTER)

        tree.heading("tname",text="TRAIN NAME",anchor=CENTER)
        tree.heading("tid",text="TRAIN ID",anchor=CENTER)
        tree.heading("arrival_city",text="Arrival CITY",anchor=CENTER)
        tree.heading("destination_city",text="DESTINATION CITY",anchor=CENTER)
        tree.heading("manno",text="MANAGER NO",anchor=CENTER)
        tree.heading("total_seat",text="TOTAL SEAT",anchor=CENTER)
        tree.heading("price",text="COST",anchor=CENTER)
        tree.heading("time_arrival",text="TIMMINGS",anchor=CENTER)
        count=0
        for i in my_cursor:
            tree.insert('',count,text=" ",values=(i[0],i[1] ,i[2], i[3],i[4],i[5] ,i[6], i[7]))
            count=count+1
        tree.pack(fill='x')

    def search_info(self):
        lbl=Label(self.root,text="ENTER CUSTOMER ID",font=("arial",12,"bold"),padx=2,pady=6) 
        lbl.place(x=1000,y=250,width=220,height=20)
        entry_reff1= ttk.Entry(self.root,textvariable=self.cutomer_id2,font=("arial",12,"bold"),width=29)
        entry_reff1.place(x=1000,y=290)
        del_button=Button(self.root,text=" Search Details ",command=self.search_timing,font=("times new roman",14,"bold"),bg="black",fg="green",bd=4,relief=RIDGE)
        del_button.place(x=1000,y=320,width=220)

    def search_timing(self):
        con=cx_Oracle.connect("system/salil")
        my_cursor = con.cursor()
        s="select cid,train_detail.tid,cname,time_arrival,arrival_city,destination_city,coch_no from cust_detail,train_detail where cust_detail.tname=train_detail.tname and cid =:1"
        my_cursor.execute(s,(self.cutomer_id2.get(),))
        tree=ttk.Treeview(self.root,height="60")
        tree.place(x=1500,y=750)
        tree['show']='headings'
        tree["columns"]=("cid","tid","cname","time_arrival","arrival_city","destination_city","Coch_no")  
        tree.column("cid",width=50,anchor=CENTER)
        tree.column("tid",width=50,anchor=CENTER)
        tree.column("cname",width=50,anchor=CENTER)
        tree.column("arrival_city",width=50,anchor=CENTER)
        tree.column("time_arrival",width=150,anchor=CENTER)
        tree.column("destination_city",width=50,anchor=CENTER)
        tree.column("Coch_no",width=50,anchor=CENTER)

        tree.heading("cid",text="SEAT NO ",anchor=CENTER)
        tree.heading("tid",text="TRAIN ID ",anchor=CENTER)
        tree.heading("cname",text="CUSTOMER NAME ",anchor=CENTER)
        tree.heading("time_arrival",text="TIMMINGS",anchor=CENTER)
        tree.heading("arrival_city",text="ARRIVAL CITY ",anchor=CENTER)
        tree.heading("destination_city",text="DESTINATION CITY",anchor=CENTER)
        tree.heading("Coch_no",text="COACH NUMBER ",anchor=CENTER)
        count=0
        for i in my_cursor:
            tree.insert('',count,text=" ",values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
            count=count+1
        tree.pack(fill='x')


if __name__ == '__main__':
    root = Tk()
    obj = Train_detail(root)
    root.mainloop()


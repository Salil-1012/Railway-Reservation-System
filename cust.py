from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk 
import cx_Oracle
from tkinter import messagebox


class Cust_Detail:
    def __init__(self, root):
        self.root = root
        self.root.title("CUTOMERS DETAIL")
        self.root.geometry("1300x650")

        self.cutomer_name=StringVar()
        self.cutomer_coch_no=StringVar()
        self.cutomer_id1=StringVar()
        self.cutomer_id2=StringVar()
        self.cutomer_id3=StringVar()
        self.cutomer_gender=StringVar()
        self.cutomer_city=StringVar()
        self.train_name=StringVar()
        self.train_id=StringVar()
        self.Reser_Status=StringVar()

        img1 = Image.open("C:\\Users\\asd\\Pictures\\s.jpeg")
        img1 = img1.resize((1300, 650), Image.ANTIALIAS)
        self.photoImg1 = ImageTk.PhotoImage(img1)

        self.lb = Label(self.root, image=self.photoImg1, bd=4, relief=RIDGE)
        self.lb.place(x=0, y=0, width=1300, height=650)

        self.lb_t = Label(self.root, text="CUSTOMERS ", font=(
            "times new roman", 18, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        self.lb_t.place(x=0, y=0, width=1300, height=90)

        self.cust_btn=Button(self.root,text=" GET DETAILS",command=self.fetch_data,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        self.cust_btn.place(x=0,y=150,width=220)

        self.cust_btn=Button(self.root,text=" ADD DETAILS",command=self.add_data_detail,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        self.cust_btn.place(x=240,y=150,width=220)

        self.cust_btn=Button(self.root,text=" CANCEL TICKET ",command=self.del_customer_info,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        self.cust_btn.place(x=740,y=150,width=220)

        self.cust_btn=Button(self.root,text=" SEARCH DETAILS ",command=self.search_customer_info,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        self.cust_btn.place(x=1000,y=150,width=220)


    def fetch_data(self):
        con=cx_Oracle.connect("system/salil")
        my_cursor = con.cursor()
        my_cursor.execute("select * from cust_detail")
        tree=ttk.Treeview(self.root,height="60")    
        tree.place(x=1500,y=750)
        tree['show']='headings'
        tree["columns"]=("cname","cid","gender","city","tname","tid","Res_status","Coch_no")  
        tree.column("cname",width=50,anchor=CENTER)
        tree.column("cid",width=100,anchor=CENTER)
        tree.column("gender",width=50,anchor=CENTER)
        tree.column("city",width=150,anchor=CENTER)
        tree.column("tname",width=150,anchor=CENTER)
        tree.column("tid",width=150,anchor=CENTER) 
        tree.column("Res_status",width=150,anchor=CENTER)
        tree.column("Coch_no",width=150,anchor=CENTER)

        tree.heading("cname",text="CUSTOMER",anchor=CENTER)
        tree.heading("cid",text="SEAT NO",anchor=CENTER)
        tree.heading("gender",text="SEX",anchor=CENTER)
        tree.heading("city",text="CITY",anchor=CENTER)
        tree.heading("tname",text="TRAIN",anchor=CENTER)
        tree.heading("tid",text="TRAIN_ID",anchor=CENTER) 
        tree.heading("Res_status",text="BOOK",anchor=CENTER)
        tree.heading("Coch_no",text="COCH NUMBER",anchor=CENTER)
        count=0
        for i in my_cursor:
            tree.insert('',count,text=" ",values=(i[0],i[1] ,i[2], i[3],i[4],i[5],i[6],i[7]))
            count=count+1
        tree.pack(fill='x')
    
    def add_data_detail(self):
        con=cx_Oracle.connect("system/salil")
        lbl_cust_name=Label(self.root,text=" NAME",font=("arial",12,"bold")) 
        lbl_cust_name.place(x=1,y=245,width=50,height=20)
        entry_reff= ttk.Entry(self.root,textvariable=self.cutomer_name,font=("arial",12,"bold"),width=29)
        entry_reff.place(x=0,y=265)
        
        lbl_cust_id=Label(self.root,text="COCH NO",font=("arial",12,"bold")) 
        lbl_cust_id.place(x=1,y=300,width=75,height=20)
        entry_reff= ttk.Entry(self.root,textvariable=self.cutomer_coch_no,font=("arial",12,"bold"),width=29)
        entry_reff.place(x=0,y=317)


        lbl_cust_gender=Label(self.root,text=" GENDER",font=("arial",12,"bold")) 
        lbl_cust_gender.place(x=1,y=345,height=15)
        entry_reff= ttk.Combobox(self.root,textvariable=self.cutomer_gender,font=("arial",12,"bold"),width=29,state="readonly")
        entry_reff["values"]=("M","F")
        entry_reff.current(0)
        entry_reff.place(x=0,y=365)


        lbl_cust_city=Label(self.root,text=" CITY",font=("arial",12,"bold")) 
        lbl_cust_city.place(x=1,y=395,height=15)
        entry_reff= ttk.Entry(self.root,textvariable=self.cutomer_city,font=("arial",12,"bold"),width=29)
        entry_reff.place(x=0,y=415)

        lbl_train_name=Label(self.root,text="TRAIN NAME ",font=("arial",12,"bold"),padx=2,pady=6) 
        lbl_train_name.place(x=1,y=450,height=16)
        entry_reff= ttk.Entry(self.root,textvariable=self.train_name,font=("arial",12,"bold"),width=29)
        entry_reff.place(x=0,y=465)

        lbl_train_id=Label(self.root,text="TRAIN Id ",font=("arial",12,"bold")) 
        lbl_train_id.place(x=1,y=495,height=16)
        entry_reff= ttk.Entry(self.root,textvariable=self.train_id,font=("arial",12,"bold"),width=29)
        entry_reff.place(x=0,y=515)

        lbl_res=Label(self.root,text="Res STATUS ",font=("arial",12,"bold")) 
        lbl_res.place(x=1,y=545,height=16)
        entry_reff= ttk.Entry(self.root,textvariable=self.Reser_Status,font=("arial",12,"bold"),width=29)
        entry_reff.place(x=0,y=565)

        cust_btn=Button(self.root,text=" SAVE DETAILS",command=self.data_added,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        cust_btn.place(x=0,y=610,width=220)

    def data_added(self):
        con=cx_Oracle.connect("system/salil")
        my_cursor = con.cursor()
        try:
            s="insert into cust_detail (cname,gender,city,tname,tid,res_status,coch_no) values(:1, :2, :3, :4 ,:5 ,:6,:7)" 
            my_cursor.execute(s,(self.cutomer_name.get(),
                                                                                            self.cutomer_gender.get(),
                                                                                            self.cutomer_city.get(),
                                                                                            self.train_name.get(),
                                                                                            self.train_id.get(),
                                                                                            self.Reser_Status.get(),
                                                                                            self.cutomer_coch_no.get()
                                                                                        )
                                                                                    )
            
            con.commit()
            con.close() 
            messagebox.showinfo("message","SUCESSFULLY ADDED ",parent=self.root)
        except Exception as E:
            messagebox.showwarning("Warning",f"NOT ADDED :{str(E)} ",parent=self.root)
    
    def del_customer_info(self):
        lbl=Label(self.root,text="ENTER CUSTOMER ID",font=("arial",12,"bold"),padx=2,pady=6) 
        lbl.place(x=740,y=250,width=220,height=30)
        entry_reff1= ttk.Entry(self.root,textvariable=self.cutomer_id1,font=("arial",12,"bold"),width=20) 
        entry_reff1.place(x=740,y=290)
        del_button=Button(self.root,text=" Delete Details",command=self.del_data,font=("times new roman",14,"bold"),bg="black",fg="green",bd=4,relief=RIDGE)
        del_button.place(x=740,y=320,width=220)

    def del_data(self):
        try:
            con=cx_Oracle.connect("system/salil")
            my_cursor = con.cursor()
            s="delete from cust_detail where cid = :1"
            my_cursor.execute(s,(self.cutomer_id1.get(),))
            messagebox.showinfo("message","CHECK IN DETAILS!!!",parent=self.root)
            con.commit()
            con.close() 
        except Exception as E1:
            messagebox.showwarning("Warning",f"NOT DELETED :{str(E1)} ",parent=self.root)


    def search_customer_info(self):
        lbl=Label(self.root,text="ENTER CUSTOMER NAME",font=("arial",12,"bold"),padx=2,pady=6) 
        lbl.place(x=1000,y=250,width=220,height=20)
        entry_reff1= ttk.Entry(self.root,textvariable=self.cutomer_id2,font=("arial",12,"bold"),width=29)
        entry_reff1.place(x=1000,y=290)
        del_button=Button(self.root,text=" Search Details ",command=self.search_data,font=("times new roman",14,"bold"),bg="black",fg="green",bd=4,relief=RIDGE)
        del_button.place(x=1000,y=320,width=220)


    def search_data(self):
        try:
            con=cx_Oracle.connect("system/salil")
            my_cursor = con.cursor()  
            s="select * from cust_detail where cname = :1"
            statement=my_cursor.execute(s,(self.cutomer_id2.get(),))
            messagebox.showinfo("message","CHECK IT PLEASE!!!!",parent=self.root)
            tree=ttk.Treeview(self.root,height="60")
            tree.place(x=1500,y=750)
            tree['show']='headings'
            tree["columns"]=("cname","cid","gender","city","tname","tid","Res_status","Coch_no")  
            tree.column("cname",width=50,minwidth=50,anchor=CENTER)
            tree.column("cid",width=100,minwidth=100,anchor=CENTER)
            tree.column("gender",width=50,minwidth=50,anchor=CENTER)
            tree.column("city",width=150,minwidth=150,anchor=CENTER)
            tree.column("tname",width=150,minwidth=150,anchor=CENTER)
            tree.column("tid",width=150,minwidth=150,anchor=CENTER) 
            tree.column("Res_status",width=150,minwidth=150,anchor=CENTER)
            tree.column("Coch_no",width=150,minwidth=150,anchor=CENTER)

            tree.heading("cname",text="CUSTOMER",anchor=CENTER)
            tree.heading("cid",text="SEAT NO",anchor=CENTER)
            tree.heading("gender",text="SEX",anchor=CENTER)
            tree.heading("city",text="CITY",anchor=CENTER)
            tree.heading("tname",text="TRAIN",anchor=CENTER)
            tree.heading("tid",text="TRAIN_ID",anchor=CENTER) 
            tree.heading("Res_status",text="BOOK",anchor=CENTER)
            tree.heading("Coch_no",text="COACH NUMBER",anchor=CENTER)
            count=0
            for i in statement:
                tree.insert('',count,text=" ",values=(i[0],i[1] ,i[2], i[3],i[4],i[5],i[6],i[7]))
                count=count+1
            tree.pack()
            con.commit()
            con.close() 
        except Exception as E2:
            messagebox.showwarning("Waring",f" NOT FOUND  :{str(E2)}",parent=self.root)
    
        

if __name__ == '__main__':
    root = Tk()
    obj = Cust_Detail(root)
    root.mainloop()
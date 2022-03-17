from tkinter import *
from PIL import Image, ImageTk
import cx_Oracle
from tkinter import ttk
from tkinter import messagebox

class Waiting:
    def __init__(self, root):
        self.root = root
        self.root.title("CUTOMERS DETAIL")
        self.root.geometry("1295x650")

        self.cutomer_id1=StringVar()

        img1 = Image.open(r"C:\\Users\\asd\\Pictures\\s.jpeg")
        img1 = img1.resize((1295, 650), Image.ANTIALIAS)
        self.photoImg1 = ImageTk.PhotoImage(img1)

        lb = Label(self.root, image=self.photoImg1, bd=4, relief=RIDGE)
        lb.place(x=0, y=0, width=1295, height=650)

        lb_t = Label(self.root, text="WAITING LIST", font=(
            "times new roman", 18, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lb_t.place(x=0, y=0, width=1295, height=90)

        cust_btn=Button(self.root,text="WAITING ROOM",command=self.fetch_data,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        cust_btn.place(x=500,y=150,width=320)

    def fetch_data(self):
        con=cx_Oracle.connect("system/salil")
        my_cursor = con.cursor()
        my_cursor.execute("select * from waiting_list")
        tree=ttk.Treeview(self.root,height="60")
        tree.place(x=1500,y=750)
        tree['show']='headings'
        tree["columns"]=("book_seat","cid","tid")  
        tree.column("book_seat",width=50,minwidth=50,anchor=CENTER)
        tree.column("cid",width=100,minwidth=100,anchor=CENTER)
        tree.column("tid",width=50,minwidth=50,anchor=CENTER)

        tree.heading("book_seat",text="BOOKING",anchor=CENTER)
        tree.heading("cid",text="CUSTOMER ID",anchor=CENTER)
        tree.heading("tid",text="TRAIN ID",anchor=CENTER)
        count=0
        for i in my_cursor:
            tree.insert('',count,text=" ",values=(i[0],i[1] ,i[2]))
            count=count+1
        tree.pack(fill='x')


if __name__ == '__main__':
    root = Tk()
    obj = Waiting(root)
    root.mainloop()
from tkinter import *
from PIL import Image, ImageTk
import cx_Oracle
from tkinter import ttk


class Department:
    def __init__(self, root):
        self.root = root
        self.root.title("CUTOMERS DETAIL")
        self.root.geometry("1295x650")

        img1 = Image.open(r"C:\\Users\\asd\\Pictures\\t.png")
        img1 = img1.resize((1295, 650), Image.ANTIALIAS)
        self.photoImg1 = ImageTk.PhotoImage(img1)

        lb = Label(self.root, image=self.photoImg1, bd=4, relief=RIDGE)
        lb.place(x=0, y=0, width=1295, height=650)

        lb_t = Label(self.root, text="  RAILWAY DEPARTMENT ", font=(
            "times new roman", 18, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lb_t.place(x=0, y=0, width=1295, height=90)

        cust_btn=Button(self.root,text="INFORMATION ",command=self.fetch_data,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        cust_btn.place(x=0,y=150,width=320)

    def fetch_data(self):
        con=cx_Oracle.connect("system/salil")
        my_cursor = con.cursor()
        my_cursor.execute("select * from dept ")
        tree=ttk.Treeview(self.root,height="60")
        tree.place(x=1500,y=750)
        tree['show']='headings'
        tree["columns"]=("deptno","manno","mobile","m_name")  
        tree.column("deptno",width=50,anchor=CENTER)
        tree.column("manno",width=100,anchor=CENTER)
        tree.column("mobile",width=50,anchor=CENTER)
        tree.column("m_name",width=150,anchor=CENTER)

        tree.heading("deptno",text="DEPT NO",anchor=CENTER)
        tree.heading("manno",text="MANAGER NO",anchor=CENTER)
        tree.heading("mobile",text="MOBILE",anchor=CENTER)
        tree.heading("m_name",text="MANAGER NAME",anchor=CENTER)
        count=0
        for i in my_cursor:
            tree.insert('',count,text=" ",values=(i[0],i[1] ,i[2], i[3]))
            count=count+1
        tree.pack(fill='x')


if __name__ == '__main__':
    root = Tk()
    obj = Department(root)
    root.mainloop()


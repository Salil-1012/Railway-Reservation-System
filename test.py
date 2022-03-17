# # import cx_Oracle
# # from tkinter import *
# # from tkinter import ttk
# # import cx_Oracle

# # r=Tk()
# # r.title("tables")
# # r.geometry("10800x720")



# con=cx_Oracle.connect("system/salil")
# my_cursor = con.cursor()
# my_cursor.execute("select * from cust_detail")
# rows = my_cursor.fetchall()
# for i in rows:
#     print(f"Name :{i[0]} Cid: {i[1]} Gendre :{i[2]} city: {i[3]} TName :{i[4]} Tid: {i[5]}  Reservation :{i[6]}\n")
# my_cursor.close()

# # tree = ttk.Treeview(r)
# # tree["columns"] = ("cid ","cname")
# # tree.column("cid",width=50,minwidth=50)
# # tree.column("cname",width=100,minwidth=70)

# # tree.heading("CID",text="CID")
# # tree.heading("CNAME",text="NAME")

# # c=0
# # for i in my_cursor:
# #     tree.insert('',c,text="",values=(i[0],i[1] ,i[2] ,i[3] , i[4], i[5] , i[6]))
# # tree.pack()
# # r.mainloop()


# # from tkinter import *
# # from tkinter import ttk
# # import pyttsx3
# # import os
# # class TXT_speech:
# #      def __init__(self,root):
# #         self.root=root
# #         self.root.title("TEXT TO SPEECH CONVERTER")
# #         self.root.geometry("500x300+190+170")

# #         lbtitle1=Label(self.root,text="ENTER TEXT:",font=("times new roman",16,"bold"),bg="black",fg="gold",bd=2,relief=RIDGE)
# #         lbtitle1.place(x=140,y=1,width=200,height=30)
      
# #         entrybox=ttk.Entry(self.root,width=50,font=("times new roman",12,"bold"))
# #         entrybox.grid(row=0,column=0)
# #         entrybox.place(x=50,y=45)

# #         spch_btn3=Button(self.root,text="CONVERT",command=self.converter,width=14,font=("Arial",12,"bold"),bg="black",fg="red",bd=2,relief=RIDGE)
# #         spch_btn3.grid(row=0,column=0)
# #         spch_btn3.place(x=160,y=80)
        
# #         canvas=Frame(self.root,bd=4,relief=RIDGE)
# #         canvas.place(x=0,y=130,width=500,height=170)
      
# #      def a(self,m):
# #          engine=pyttsx3.init('sapi5')
# #          voices= engine.getProperty('voices')
# #          engine.say(self,m)
# #          engine.runAndWait()

# #      def converter(self): 
# #         entrybox=ttk.Entry(self.root,width=50,font=("times new roman",12,"bold"))
# #         entrybox.grid(row=0,column=0)
# #         entrybox.place(x=50,y=45)
# #         m=self.a(self,entrybox)
# #         # self.entrybox.delete(END)
# #         return m

# # if __name__=="__main__":
# #    root=Tk()
# # #    obj=TXT_speech(root)
# # #    root.mainloop()


# # txt=Text(self,borderwidth=0,highlightthickness=0,width=22,height=1)
# # txt.place(x=315,y=150)

# from tkinter import *
# from tkinter import ttk
# from tkinter.messagebox import showinfo
# from PIL import Image,ImageTk
# #from pyttsx3 import engine
# import speech_recognition as sp
# from googletrans import Translator,LANGUAGES
# import pyttsx3
# from gtts import gTTS
# import os
# import time
# root=Tk()

# root.title("SPEECH TO TEXT AND TEXT TO SPEECH CONVERTER")
# root.geometry("1250x670")
# root.configure(bg="white")

# img=Image.open(r"C:\\Users\\asd\\Desktop\\a.png")
# img=img.resize((1250,140),Image.ANTIALIAS)
# photoimg=ImageTk.PhotoImage(img)

# imglabel=Label(image=photoimg,bd=2,relief=RIDGE)
# imglabel.place(x=0,y=0,width=1250,height=140)

# lbtitle=Label(text="SPEECH & TEXT CONVERTER",font=("times new roman",20,"bold"),bg="black",fg="red",bd=2,relief=RIDGE)
# lbtitle.place(x=0,y=140,width=1250,height=50)

# canvas1=Frame(bd=4,bg="skyblue",relief=RIDGE)
# canvas1.place(x=0,y=190,width=625,height=480)

# canvas2=Frame(bd=4,bg="cyan",relief=RIDGE)
# canvas2.place(x=624,y=190,width=625,height=480)

# lbl=Label(canvas1,text="TEXT TO SPEECH CONVERTER",font=("Arial",16,"bold"),bg="black",fg="GOLD",bd=2,relief=RIDGE)
# lbl.place(x=36,y=3,width=550,height=35)

# lbl=Label(canvas2,text="SPEECH TO TEXT CONVERTER",font=("Arial",16,"bold"),bg="black",fg="GOLD",bd=2,relief=RIDGE)
# lbl.place(x=36,y=3,width=550,height=35)

# language=list(LANGUAGES.values())
# src_lang = ttk.Combobox(canvas1,values= language, width =22)
# src_lang.place(x=110,y=48)
# src_lang.set('choose input language')

# dest_lang = ttk.Combobox(canvas1, values= language, width =22)
# dest_lang.place(x=350,y=48)
# dest_lang.set('choose output language')

# lbtitle=Label(canvas1,text="ENTER TEXT:",font=("times new roman",16,"bold"),bg="black",fg="GOLD",bd=2,relief=RIDGE)
# lbtitle.place(x=160,y=80,width=290,height=30)

# txt=Text(canvas1,width=50,font=("times new roman",12,"bold"))
# txt.grid(row=0,column=0)
# txt.place(x=100,y=125,height=30)

# txt1=Text(canvas1,width=50,font=("times new roman",12,"bold"))
# txt1.grid(row=0,column=0)
# txt1.place(x=100,y=215,height=30)

# txt2=Text(canvas2,width=50,font=("times new roman",12,"bold"))
# txt2.grid(row=0,column=0)
# txt2.place(x=100,y=215,height=30)

# def text_converter():
    
#     translator=Translator()
#     trans=translator.translate(text=txt.get(1.0,END),src=src_lang.get(),dest=dest_lang.get())
#     txt1.delete(1.0,END)
#     txt1.insert(END,trans.text)
#     myobj=gTTS(text=txt1.get(1.0,END),lang=dest_lang.get(),slow = False)
#     myobj.save("convert.wav") 
#     os.system("convert.wav") 
#     time.sleep(5)
#     showinfo('Info','File is saved')



# spch_btn1=Button(canvas1,text="PLAY & TRANSALATE ",command=text_converter,width=18,font=("Arial",8,"bold"),bg="black",fg="gold",bd=2,relief=RIDGE)
# spch_btn1.grid(row=0,column=0)
# spch_btn1.place(x=220,y=170)

# # spch_btn1=Button(canvas1,text="TRANSLATE",command=text_translator,width=14,font=("Arial",12,"bold"),bg="black",fg="gold",bd=2,relief=RIDGE)
# # spch_btn1.grid(row=0,column=0)
# # spch_btn1.place(x=235,y=170)

# # spch_btn1=Button(canvas1,text="SAVE",command=text_saver,width=14,font=("Arial",12,"bold"),bg="black",fg="gold",bd=2,relief=RIDGE)
# # spch_btn1.grid(row=0,column=0)
# # spch_btn1.place(x=400,y=170)

# # canvas=Frame(canvas1,bd=4,relief=RIDGE,bg="lightgrey")
# # canvas.place(x=0,y=195,width=616,height=278) 


# language=list(LANGUAGES.values())
# src_lang = ttk.Combobox(canvas2,values= language, width =22)
# src_lang.place(x=150,y=48)
# src_lang.set('choose input language')

# dest_lang = ttk.Combobox(canvas2, values= language, width =22)
# dest_lang.place(x=410,y=48)
# dest_lang.set('choose output language')

# def speech_converter():
#     rc=sp.Recognizer()
#     mic=sp.Microphone()
#     translator=Translator()
#     with mic as source:
#         try:
#             print("Speak something!")
#             rc.adjust_for_ambient_noise(source,duration=0.2)
#             speech_data=rc.listen(source)
#             text=rc.recognize_google(speech_data)
#             print('Text to be translated is : {}'.format(text))
#             txt_to_translate = translator.translate(text,src=src_lang.get(),dest=dest_lang.get())
#             txt=txt_to_translate.text
#             txt2.insert(END,txt_to_translate)
#            # spk=gTTS(text=txt,lang=dest_lang,slow=False)
#             # spk.save("captured_voice.mp3")  
#             # os.system("start captured_voice.mp3")
#             showinfo('Info','File is saved')
#             #print(txt)
#             with open('output.txt',"a") as file:
#                 file.write(txt)
#                 file.write("\n")
#                 print("successfully written")
#                 file.close()
#             print(txt)
#         except sp.UnknownValueError:
#             print("Unable to Understand the Input")
              
#         except sp.RequestError as e:
#             print("Unable to provide Required Output".format(e))


# spch_btn1=Button(canvas2,text="S P E A K",command=speech_converter,width=12,font=("Arial",16,"bold"),bg="black",fg="gold",bd=2,relief=RIDGE)
# spch_btn1.grid(row=0,column=0)
# spch_btn1.place(x=230,y=80)

# canvas3=Frame(canvas2,bd=4,relief=RIDGE,bg="lightgrey")
# canvas3.place(x=0,y=195,width=616,height=278)

# root.mainloop()

# import cx_Oracle

# con=cx_Oracle.connect("system/salil")

# my_cursor= con.cursor()
# rows=my_cursor.execute("insert into student values('LONDON',16,'sachin','C',55,10700)") 
# rows.commit()
# rows.close()
# # except Exception as err:
#     # print("Error, not added")

f=open('notes.txt','r')
l=' '
count=0
for i in f:
    print('line number is ',count)
    print(i)
    print('chara are ',len(i))
    if(len(i)>len(l)):
        l=i
print(l,'is the longest line with',len(l),'character')
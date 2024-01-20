from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox


class roombooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1050x630+230+235")
        
        #variables
        self.var_contact=StringVar()
        self.var_checkIn=StringVar()
        self.var_CheckOut=StringVar()
        self.var_RoomType=StringVar()
        self.var_AvailableRoom=StringVar()
        self.var_Meal=StringVar()
        self.var_Days=StringVar()
        self.var_Tax=StringVar()
        self.var_Total=StringVar()
        
        
        
        
        #title
        lbl_title=Label(self.root,text="ROOM BOOKINGS",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1040,height=50)
        
         # Image 2 (logo)
        img2 = Image.open(r"C:\Users\user\Desktop\hotel\images\logo.png")
        img2 = img2.resize((50, 50), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lbl_img2 = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lbl_img2.place(x=0, y=0, width=50, height=50)
        
         #label
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="ROOM BOOKING DETAILS",font=("times new roman",12,"bold"))
        labelframeleft.place(x=3,y=50,width=400,height=350)
        
         #cust_contact
        lbl_cust_contact=Label(labelframeleft,text="Customer Contact",font=("times new roman",12,"bold"),padx=2,pady=2)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)
        
        entry_contact=ttk.Entry(labelframeleft,textvariable=self.var_contact,font=("arial",11,"bold"),width=30)
        entry_contact.grid(row=0,column=1)
        
        #fetch data button
        btnFetchData=Button(labelframeleft,command=self.Fetch_contact,text="Fetch data",font=("arial",6,"bold"),bg="black",fg="white",width=8)
        btnFetchData.place(x=347,y=4)
        
       
        
        #cust_checkin
        lbl_cust_CheckIn=Label(labelframeleft,text="CheckIn",font=("times new roman",12,"bold"),padx=2,pady=2)
        lbl_cust_CheckIn.grid(row=1,column=0,sticky=W)
        
        entry_CheckIn=ttk.Entry(labelframeleft,textvariable=self.var_checkIn,font=("arial",11,"bold"),width=30)
        entry_CheckIn.grid(row=1,column=1)
        
        #cust_checkout
        lbl_cust_CheckOut=Label(labelframeleft,text="CheckOut",font=("times new roman",12,"bold"),padx=2,pady=2)
        lbl_cust_CheckOut.grid(row=2,column=0,sticky=W)
        
        entry_CheckOut=ttk.Entry(labelframeleft,textvariable=self.var_CheckOut,font=("arial",11,"bold"),width=30)
        entry_CheckOut.grid(row=2,column=1)
        
        #room type
        type=Label(labelframeleft,text="Room Type",font=("times new roman",12,"bold"),padx=2,pady=2)
        type.grid(row=3,column=0,sticky=W)
        
        type=ttk.Combobox(labelframeleft,textvariable=self.var_RoomType,font=("arial",11,"bold"),width=28)
        type["value"]=(" ","Single","Double","Suite")
        type.current(0)
        type.grid(row=3,column=1)
        
        #available room
        lbl_cust_AvailableRoom=Label(labelframeleft,text="AvailableRoom",font=("times new roman",12,"bold"),padx=2,pady=2)
        lbl_cust_AvailableRoom.grid(row=4,column=0,sticky=W)
        
        entry_AvailableRoom=ttk.Entry(labelframeleft,textvariable=self.var_AvailableRoom,font=("arial",11,"bold"),width=30)
        entry_AvailableRoom.grid(row=4,column=1)
        
        #meal
        lbl_cust_Meal=Label(labelframeleft,text="Meal",font=("times new roman",12,"bold"),padx=2,pady=2)
        lbl_cust_Meal.grid(row=5,column=0,sticky=W)
        
        entry_Meal=ttk.Entry(labelframeleft,textvariable=self.var_Meal,font=("arial",11,"bold"),width=30)
        entry_Meal.grid(row=5,column=1)
        
        #no of days
        lbl_cust_Days=Label(labelframeleft,text="Days",font=("times new roman",12,"bold"),padx=2,pady=2)
        lbl_cust_Days.grid(row=6,column=0,sticky=W)
        
        entry_Days=ttk.Entry(labelframeleft,textvariable=self.var_Days,font=("arial",11,"bold"),width=30)
        entry_Days.grid(row=6,column=1)
        
        #paid tax
        lbl_cust_Tax=Label(labelframeleft,text="Tax",font=("times new roman",12,"bold"),padx=2,pady=2)
        lbl_cust_Tax.grid(row=7,column=0,sticky=W)
        
        entry_Tax=ttk.Entry(labelframeleft,textvariable=self.var_Tax,font=("arial",11,"bold"),width=30)
        entry_Tax.grid(row=7,column=1)
        
        #total cost  
        lbl_cust_Total=Label(labelframeleft,text="Total",font=("times new roman",12,"bold"),padx=2,pady=2)
        lbl_cust_Total.grid(row=8,column=0,sticky=W)
        
        entry_Total=ttk.Entry(labelframeleft,textvariable=self.var_Total,font=("arial",11,"bold"),width=30)
        entry_Total.grid(row=8,column=1)
        
        #image
        img3 = Image.open(r"C:\Users\user\Desktop\hotel\images\room.jpg")
        img3 = img3.resize((300, 200), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img3)
        lbl_img3 = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lbl_img3.place(x=750, y=55, width=283, height=150)
  
        
        #buttons
        #add
        b_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        b_frame.place(x=0,y=250,width=412,height=40)
        
        badd=Button(b_frame,text="ADD",command=self.add_data,font=("times new roman",12,"bold"),bg="black",fg="white",width=9)
        badd.grid(row=0,column=0,padx=1)
        
        #update
        update=Button(b_frame,text="UPDATE",font=("times new roman",12,"bold"),bg="black",fg="white",width=10)
        update.grid(row=0,column=1,padx=1)
        
        #delete
        delete=Button(b_frame,text="DELETE",font=("times new roman",12,"bold"),bg="black",fg="white",width=10)
        delete.grid(row=0,column=2,padx=1)
        
        #reset
        reset=Button(b_frame,text="RESET",font=("times new roman",12,"bold"),bg="black",fg="white",width=10)
        reset.grid(row=0,column=3,padx=1)
        
        #search system
        
        dframe=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details",font=("times new roman",12,"bold"))
        dframe.place(x=405,y=200,width=630,height=200)
        
        table=Label(dframe,text="Search",font=("times new roman",9,"bold"),bg="green",fg="white")
        table.grid(row=0,column=0,sticky=W)
        
        self.search_var=StringVar()
        csearch=ttk.Combobox(dframe,textvariable=self.search_var,font=("arial",9,"bold"),width=24,state="readonly")
        csearch["value"]=(" ","Contact no.","Ref no.")
        csearch.current(0)
        csearch.grid(row=0,column=1)
        
        self.txt_search=StringVar()
        seache=ttk.Entry(dframe,textvariable=self.txt_search,font=("arial",9,"bold"),width=24)
        seache.grid(row=0,column=2)
        
        bsearch=Button(dframe,text="Search",font=("times new roman",9,"bold"),bg="black",fg="white",width=5)
        bsearch.grid(row=0,column=3,padx=1)
        
        ball=Button(dframe,text="All",font=("times new roman",9,"bold"),bg="black",fg="white",width=5)
        ball.grid(row=0,column=4,padx=1)
        
        #details table
        
        tdetails=Frame(dframe,bd=2,relief=RIDGE)
        tdetails.place(x=0,y=40,width=630,height=150)
        
        scroll_x=ttk.Scrollbar(tdetails,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(tdetails,orient=VERTICAL)
        
        self.room_table=ttk.Treeview(tdetails,columns=("Customer Contact","CheckIn","CheckOut","RoomType","AvailableRoom","Meal","Days","Tax","Total"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)
        
        # Assuming self.room_table is a Treeview widget
        self.room_table.heading("Customer Contact", text="Contact")
        self.room_table.heading("CheckIn", text="CheckIn")
        self.room_table.heading("CheckOut", text="CheckOut")
        self.room_table.heading("RoomType", text="RoomType")
        self.room_table.heading("AvailableRoom", text="AvailableRoom")
        self.room_table.heading("Meal", text="Meal")
        self.room_table.heading("Days", text="Days")
        self.room_table.heading("Tax", text="Tax")
        self.room_table.heading("Total", text="Total")
        
        self.room_table["show"] = "headings"
        
        self.room_table.column("Customer Contact", width=100)
        self.room_table.column("CheckIn", width=100)
        self.room_table.column("CheckOut", width=100)
        self.room_table.column("RoomType", width=100)
        self.room_table.column("AvailableRoom", width=100)
        self.room_table.column("Meal", width=100)
        self.room_table.column("Days", width=100)
        self.room_table.column("Tax", width=100)
        self.room_table.column("Total", width=100)
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
    
    def add_data(self):
      if self.var_contact.get()=="" or self.var_checkIn.get()=="":
          messagebox.showerror("Error","All fields are required",parent=self.root)
      else:
          try:
              conn=mysql.connector.connect(host="localhost",username="root",password="Saloni442@",database="shreya2")
              my_cursor=conn.cursor()
              my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                  self.var_contact.get(),
                                                                                  self.var_checkIn.get(),
                                                                                  self.var_CheckOut.get(),
                                                                                  self.var_RoomType.get(),
                                                                                  self.var_AvailableRoom.get(),
                                                                                  self.var_Meal.get(),
                                                                                  self.var_Days.get()
                                                                                  ))
              conn.commit()
              self.fetch_data()
              conn.close()
              messagebox.showinfo("success","customer has been added",parent=self.root)
          except Exception as es:
              messagebox.showwarning("Warning",f"Some things went wrong:{str(es)}",parent=self.root)
              
    def fetch_data(self):
      conn=mysql.connector.connect(host="localhost",username="root",password="Saloni442@",database="shreya2")
      my_cursor=conn.cursor()
      my_cursor.execute("select * from room")
      rows=my_cursor.fetchall()
      if len(rows)!=0:
          self.room_table.delete(*self.room_table.get_children())
          for i in rows:
              self.room_table.insert("",END,value=i)
          conn.commit()
      conn.close()
      
    def get_cursor(self,events=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]
        
        
        self.var_contact.set(room[0]),
        self.var_checkIn.set(room[1]),
        self.var_CheckOut.set(room[2]),
        self.var_RoomType.set(room[3]),
        self.var_AvailableRoom.set(room[4]),
        self.var_Meal.set(room[5]),
        self.var_Days.set(room[6])

    
    #fetch all data
    def Fetch_contact(self):
      if self.var_contact.get()=="":
        messagebox.showerror("Error","Please enter contact details",parent=self.root)    
      else:
        conn=mysql.connector.connect(host="localhost",username="root",password="Saloni442@",database="shreya2")
        my_cursor=conn.cursor()
        query=("select name from customer where mobile=%s")
        value=(self.var_contact.get(),)
        my_cursor.execute(query,value)
        row=my_cursor.fetchone()
        
        if row==None:
          messagebox.showerror("Error","This number not found",parent=self.root)
        else:
          conn.commit()
          conn.close()
          #name
          showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
          showDataframe.place(x=400,y=55,width=345,height=145)
          
          lblname=Label(showDataframe,text="Name:",font=("arial",10,"bold"))
          lblname.place(x=0,y=0)
          
          lbl=Label(showDataframe,text=row,font=("arial",10,"bold"))
          lbl.place(x=90,y=0)
          
          #gender
          conn=mysql.connector.connect(host="localhost",username="root",password="Saloni442@",database="shreya2")
          my_cursor=conn.cursor()
          query=("select gender from customer where mobile=%s")
          value=(self.var_contact.get(),)
          my_cursor.execute(query,value)
          row=my_cursor.fetchone()
          
          lblGender=Label(showDataframe,text="Gender:",font=("arial",10,"bold"))
          lblGender.place(x=0,y=30)
          
          lbl2=Label(showDataframe,text=row,font=("arial",10,"bold"))
          lbl2.place(x=90,y=30)
          
          #age
          conn=mysql.connector.connect(host="localhost",username="root",password="Saloni442@",database="shreya2")
          my_cursor=conn.cursor()
          query=("select age from customer where mobile=%s")
          value=(self.var_contact.get(),)
          my_cursor.execute(query,value)
          row=my_cursor.fetchone()
          
          lblage=Label(showDataframe,text="Age:",font=("arial",10,"bold"))
          lblage.place(x=0,y=60)
          
          lbl3=Label(showDataframe,text=row,font=("arial",10,"bold"))
          lbl3.place(x=90,y=60)
          
          
          #email
          conn=mysql.connector.connect(host="localhost",username="root",password="Saloni442@",database="shreya2")
          my_cursor=conn.cursor()
          query=("select email from customer where mobile=%s")
          value=(self.var_contact.get(),)
          my_cursor.execute(query,value)
          row=my_cursor.fetchone()
          
          lblemail=Label(showDataframe,text="Email:",font=("arial",10,"bold"))
          lblemail.place(x=0,y=90)
          
          lbl4=Label(showDataframe,text=row,font=("arial",10,"bold"))
          lbl4.place(x=90,y=90)
          
        
        
        
        
if __name__=="__main__":
    root=Tk()
    obj=roombooking(root)
    root.mainloop()
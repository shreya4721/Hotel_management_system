from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox


class cust_win:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1050x630+230+235")
        
        #variables
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))
        
        self.var_cust_names=StringVar()
        self.var_gender=StringVar()
        self.var_age=StringVar()
        self.var_dob=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_address=StringVar()
        self.var_idproof=StringVar()
        
        
         #title
        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1040,height=50)
        
         # Image 2 (logo)
        img2 = Image.open(r"C:\Users\user\Desktop\hotel\images\logo.png")
        img2 = img2.resize((50, 50), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lbl_img2 = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lbl_img2.place(x=0, y=0, width=50, height=50)
        
        #label
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="CUSTOMER DETAILS",font=("times new roman",12,"bold"))
        labelframeleft.place(x=3,y=50,width=400,height=330)
        
        #cust_ref
        lbl_cust_ref=Label(labelframeleft,text="Customer Ref",font=("times new roman",12,"bold"),padx=2,pady=2)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)
        
        entry_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref,font=("arial",12,"bold"),width=30,state="readonly")
        entry_ref.grid(row=0,column=1)      
        
        #cust name
        custname=Label(labelframeleft,text="Customer Name",font=("times new roman",12,"bold"),padx=2,pady=2)
        custname.grid(row=1,column=0,sticky=W)
        
        cname=ttk.Entry(labelframeleft,textvariable=self.var_cust_names,font=("arial",12,"bold"),width=30)
        cname.grid(row=1,column=1) 
        
        #age
        cage=Label(labelframeleft,text="Customer Age",font=("times new roman",12,"bold"),padx=2,pady=2)
        cage.grid(row=2,column=0,sticky=W)
        
        c_age=ttk.Entry(labelframeleft,textvariable=self.var_age,font=("arial",12,"bold"),width=30)
        c_age.grid(row=2,column=1)
        
        #gender
        gender=Label(labelframeleft,text="Gender",font=("times new roman",12,"bold"),padx=2,pady=2)
        gender.grid(row=3,column=0,sticky=W)
        
        combo_g=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("arial",12,"bold"),width=28,state="readonly")
        combo_g["value"]=(" ","Male","Female","Other")
        combo_g.current(0)
        combo_g.grid(row=3,column=1)
        
        #add
        add=Label(labelframeleft,text="Address",font=("times new roman",12,"bold"),padx=2,pady=2)
        add.grid(row=4,column=0,sticky=W)
        
        add1=ttk.Entry(labelframeleft,textvariable=self.var_address,font=("arial",12,"bold"),width=30)
        add1.grid(row=4,column=1)
        
        
        #dob
        DOB=Label(labelframeleft,text="DOB",font=("times new roman",12,"bold"),padx=2,pady=2)
        DOB.grid(row=7,column=0,sticky=W)
        
        dob=ttk.Entry(labelframeleft,textvariable=self.var_dob,font=("arial",12,"bold"),width=30)
        dob.grid(row=7,column=1)
        
        #mobile
        Mobile=Label(labelframeleft,text="Mobile Number",font=("times new roman",12,"bold"),padx=2,pady=2)
        Mobile.grid(row=8,column=0,sticky=W)
        
        number=ttk.Entry(labelframeleft,textvariable=self.var_mobile,font=("arial",12,"bold"),width=30)
        number.grid(row=8,column=1)
        
        #email
        Email=Label(labelframeleft,text="Email",font=("times new roman",12,"bold"),padx=2,pady=2)
        Email.grid(row=9,column=0,sticky=W)
        
        mail=ttk.Entry(labelframeleft,textvariable=self.var_email,font=("arial",12,"bold"),width=30)
        mail.grid(row=9,column=1)
        
        #id type
        id4=Label(labelframeleft,text="ID Proof",font=("times new roman",12,"bold"),padx=2,pady=2)
        id4.grid(row=10,column=0,sticky=W)
        
        id5=ttk.Combobox(labelframeleft,textvariable=self.var_idproof,font=("arial",12,"bold"),width=28,state="readonly")
        id5["value"]=(" ","Adhar card","Passport","Voter ID")
        id5.current(0)
        id5.grid(row=10,column=1)
        
        #buttons
        #add
        b_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        b_frame.place(x=0,y=250,width=412,height=40)
        
        badd=Button(b_frame,text="ADD",command=self.add_data,font=("times new roman",12,"bold"),bg="black",fg="white",width=9)
        badd.grid(row=0,column=0,padx=1)
        
        #update
        update=Button(b_frame,text="UPDATE",command=self.update,font=("times new roman",12,"bold"),bg="black",fg="white",width=10)
        update.grid(row=0,column=1,padx=1)
        
        #delete
        delete=Button(b_frame,text="DELETE",command=self.mDelete,font=("times new roman",12,"bold"),bg="black",fg="white",width=10)
        delete.grid(row=0,column=2,padx=1)
        
        #reset
        reset=Button(b_frame,text="RESET",comman=self.reset,font=("times new roman",12,"bold"),bg="black",fg="white",width=10)
        reset.grid(row=0,column=3,padx=1)
        
        #detail frame
        dframe=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details",font=("times new roman",12,"bold"))
        dframe.place(x=405,y=50,width=630,height=330)
        
        table=Label(dframe,text="Search",font=("times new roman",9,"bold"),bg="green",fg="white")
        table.grid(row=0,column=0,sticky=W)
        
        self.search_var=StringVar()
        csearch=ttk.Combobox(dframe,textvariable=self.search_var,font=("arial",9,"bold"),width=24,state="readonly")
        csearch["value"]=(" ","Mobile","Ref no.")
        csearch.current(0)
        csearch.grid(row=0,column=1)
        
        self.txt_search=StringVar()
        seache=ttk.Entry(dframe,textvariable=self.txt_search,font=("arial",9,"bold"),width=24)
        seache.grid(row=0,column=2)
        
        badd=Button(dframe,text="Search",command=self.search,font=("times new roman",9,"bold"),bg="black",fg="white",width=5)
        badd.grid(row=0,column=3,padx=1)
        
        badd=Button(dframe,text="All",command=self.fetch_data,font=("times new roman",9,"bold"),bg="black",fg="white",width=5)
        badd.grid(row=0,column=4,padx=1)
        
        #table 
        tdetails=Frame(dframe,bd=2,relief=RIDGE)
        tdetails.place(x=0,y=40,width=630,height=260)
        
        scroll_x=ttk.Scrollbar(tdetails,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(tdetails,orient=VERTICAL)
        
        self.custtable=ttk.Treeview(tdetails,columns=("ref","name","gender","age","dob","mobile","email","address","id proof"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.custtable.xview)
        scroll_y.config(command=self.custtable.yview)
        
        # Assuming self.custtable is a Treeview widget
        self.custtable.heading("ref", text="Refer No")
        self.custtable.heading("name", text="Name")
        self.custtable.heading("gender", text="Gender")
        self.custtable.heading("age", text="Age")
        self.custtable.heading("dob", text="DOB")
        self.custtable.heading("mobile", text="Mobile no")
        self.custtable.heading("email", text="Email")
        self.custtable.heading("address", text="Address")
        self.custtable.heading("id proof", text="id proof")
        
        self.custtable["show"] = "headings"
        
        self.custtable.column("ref", width=100)
        self.custtable.column("name", width=100)
        self.custtable.column("gender", width=100)
        self.custtable.column("age", width=100)
        self.custtable.column("dob", width=100)
        self.custtable.column("mobile", width=100)
        self.custtable.column("email", width=100)
        self.custtable.column("address", width=100)
        self.custtable.column("id proof", width=100)
        
        self.custtable.pack(fill=BOTH,expand=1)
        self.custtable.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        
    def add_data(self):
        if self.var_mobile.get()=="" or self.var_address.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Saloni442@",database="shreya2")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                    self.var_ref.get(),
                                                                                    self.var_cust_names.get(),
                                                                                    self.var_gender.get(),
                                                                                    self.var_age.get(),
                                                                                    self.var_dob.get(),
                                                                                    self.var_mobile.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_mobile.get(),
                                                                                    self.var_idproof.get()
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
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.custtable.delete(*self.custtable.get_children())
            for i in rows:
                self.custtable.insert("",END,value=i)
            conn.commit()
        conn.close()
        
    def get_cursor(self,events=""):
        cursor_row=self.custtable.focus()
        content=self.custtable.item(cursor_row)
        row=content["values"]
        
        
        self.var_ref.set(row[0]),
        self.var_cust_names.set(row[1]),
        self.var_gender.set(row[2]),
        self.var_age.set(row[3]),
        self.var_dob.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_address.set(row[7]),
        self.var_idproof.set(row[8])
        
    def update(self):
        if self.var_mobile.get() == "":
            messagebox.showerror("Error", "Enter mobile number", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Saloni442@", database="shreya2")
                my_cursor = conn.cursor()
                my_cursor.execute("UPDATE customer SET name=%s, gender=%s, age=%s, dob=%s, mobile=%s, email=%s, address=%s, id_proof=%s WHERE ref=%s", (
                    self.var_cust_names.get(),
                    self.var_gender.get(),
                    self.var_age.get(),
                    self.var_dob.get(),
                    self.var_mobile.get(),
                    self.var_email.get(),
                    self.var_address.get(),
                    self.var_idproof.get(),
                    self.var_ref.get()
                ))
                conn.commit()
                self.fetch_data()  # Assuming you have a method named fetch_data to fetch data
                conn.close()
                messagebox.showinfo("Update", "Information updated successfully", parent=self.root)
            except Exception as e:
                messagebox.showwarning("Warning", f"Something went wrong: {str(e)}", parent=self.root)
                
    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System", "Do you want to delete this customer",parent=self.root)
        if mDelete>0:
            conn = mysql.connector.connect(host="localhost", username="root", password="Saloni442@", database="shreya2")
            my_cursor = conn.cursor()
            query="delete from customer WHERE ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()  
        
    def reset(self):
        self.var_ref.set(""),
        self.var_cust_names.set(""),
        self.var_gender.set(""),
        self.var_age.set(""),
        self.var_dob.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        self.var_address.set(""),
        self.var_idproof.set("")
        
    def search(self):
         conn = mysql.connector.connect(host="localhost", username="root", password="Saloni442@", database="shreya2")
         my_cursor = conn.cursor()
         
         my_cursor.execute("select * from customer where "+str(self.search_var.get())+"LIKE'%"+str(self.txt_search.get())+"%'")
         rows=my_cursor.fetchall()
         if len(rows)!=0:
            self.custtable.delete(*self.custtable.get_children())
            for i in rows:
                self.custtable.insert("",END,values=i)
                conn.commit()
                conn.close()
        
    
        
        
        
if __name__=="__main__":
    root=Tk()
    obj=cust_win(root)
    root.mainloop()
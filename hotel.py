from tkinter import *
from PIL import Image, ImageTk
from customer import cust_win
from room import roombooking

class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")

        # Image 1 (hotel banner)
        img1 = Image.open(r"C:\Users\user\Desktop\hotel\images\hotel2.jpg")
        img1 = img1.resize((1400, 150), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lbl_img1 = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lbl_img1.place(x=0, y=0, width=1400, height=150)
        
        # Image 2 (logo)
        img2 = Image.open(r"C:\Users\user\Desktop\hotel\images\logo.png")
        img2 = img2.resize((200, 150), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lbl_img2 = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lbl_img2.place(x=0, y=0, width=200, height=150)
        
        #title
        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=150,width=1400,height=50)
        
        #frame
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=200,width=1400,height=620)
        
        #menu
        lbl_menu=Label(self.root,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="white",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=200,width=230)
        
        #btn frame
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=34,width=225,height=230)
        cust_btn = Button(btn_frame, text="Customer", command=self.cust_details, width=20, font=("times new roman", 15, "bold"), bg="black", fg="white", bd=4)
        cust_btn.grid(row=0,column=0,pady=1)
        
        rooms_btn=Button(btn_frame,text="Room",command=self.roombooking,width=20,font=("times new roman",15,"bold"),bg="black",fg="white",bd=4)
        rooms_btn.grid(row=1,column=0,pady=1)
        
        details_btn=Button(btn_frame,text="Details",width=20,font=("times new roman",15,"bold"),bg="black",fg="white",bd=4)
        details_btn.grid(row=2,column=0,pady=1)
        
        report_btn=Button(btn_frame,text="Report",width=20,font=("times new roman",15,"bold"),bg="black",fg="white",bd=4)
        report_btn.grid(row=3,column=0,pady=1)
        
        logout_btn=Button(btn_frame,text="Logout",width=20,font=("times new roman",15,"bold"),bg="black",fg="white",bd=4)
        logout_btn.grid(row=4,column=0,pady=1)
        
       

        
        #image3
        img3 = Image.open(r"C:\Users\user\Desktop\hotel\images\img3.jpg")
        img3 = img3.resize((1310, 590), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lbl_img1 = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lbl_img1.place(x=225, y=0, width=1100, height=530)
        
        #image4
        img4 = Image.open(r"C:\Users\user\Desktop\hotel\images\img4.jpg")
        img4 = img4.resize((210, 230), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        lbl_img1 = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lbl_img1.place(x=0, y=220, width=230, height=210)
        
      
        
    def cust_details(self):
        try:
            print("Opening customer details window")
            self.new_window = Toplevel(self.root)
            self.app = cust_win(self.new_window)
        except Exception as e:
            print("Exception:", e)

    def roombooking(self):
        try:
            print("Opening room details window")
            self.new_window = Toplevel(self.root)
            self.app = roombooking(self.new_window)
        except Exception as e:
            print("Exception:", e)   
        
        


# Correct indentation for the __name__ block
if __name__ == "__main__":
    root = Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()

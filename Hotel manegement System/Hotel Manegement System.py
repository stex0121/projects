from tkinter import *
from PIL import Image, ImageTk
from tkinter import Label, RIDGE
import customer
import roomservice
import Details
import Sing_in


class HotelManegementSystem:
    def __init__(self, root):
    
        self.root=root
        self.root.title("Hotel Manegement System")
        self.root.geometry("1550x800+0+0")
     
###############################IMAGE IMAGE IMAGE ####################################################
        img1 = Image.open(r"C:\Users\user\Desktop\Hotel manegement System\Untitled.png")
        img1 = img1.resize((1530, 140), Image.LANCZOS)  # Corrected
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lblimg = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=1550, height=140)
################################### LOGO LOGO LOGO ###################################################
        img2 = Image.open(r"C:\Users\user\Desktop\Hotel manegement System\logohotel.png")
        img2 = img2.resize((230, 140), Image.LANCZOS)  # Corrected
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg1 = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg1.place(x=0, y=0, width=230, height=140)
##################################TITLE TITLE TITLE TITLE TITLE###############################################################
        lbl_title=Label(self.root,text="HOTEL MANEGEMENT SYSTEM",font=("Arial",40,'bold'),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)
################################## MAIN FRAME MAIN FRAME MAIN FRAME###############################################
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)
############################### MENU MENU MENU MENU #######################################
        lbl_menu=Label(self.root,text="MENU",font=("Arial",30,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=195,width=230,height=40)

################################## BUTTON FRAme BUTTON Frame #####################################
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=226,height=180)
        customer_btn=Button(btn_frame,text="CUSTOMER",width=17,font=("Arial",14,"bold"),bg='black',fg="gold",bd=0,cursor="hand1",command=open_customer_window)
        customer_btn.grid(row=0,column=0)
        room_btn=Button(btn_frame,text="ROOM",width=17,font=("arial",14,"bold"),bg='black',fg="gold",bd=0,cursor="hand1",command=open_roomservice)
        room_btn.grid(row=1,column=0)
        report_btn=Button(btn_frame,text="REPORT",width=17,font=("arial",14,"bold"),bg='black',fg="gold",bd=0,cursor="hand1")
        report_btn.grid(row=2,column=0)
        details_btn=Button(btn_frame,text="DETAILS",width=17,font=("arial",14,"bold"),bg='black',fg="gold",bd=0,cursor="hand1",command=open_details_window)
        details_btn.grid(row=3,column=0)
        logout_btn=Button(btn_frame,text="LOGOUT",width=17,font=("arial",14,"bold"),bg='black',fg="gold",bd=0,cursor="hand1",command=logout)
        logout_btn.grid(row=4,column=0)
        ################################RIGHT SIDE IMAGE RIGHT SIDE IMAGE#####################################################
        img3 = Image.open(r"C:\Users\user\Desktop\Hotel manegement System\image12.jpg")
        img3 = img3.resize((1270, 450), Image.LANCZOS)  # Corrected
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lblimg3 = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg3.place(x=225, y=0, width=1270, height=450)
################################# DOWN LEFT IMAGES DOWN LEFT IMAGES DOWN LEFT IMAGES ########################

        img4 = Image.open(r"C:\Users\user\Desktop\Hotel manegement System\picture3.jpg")
        img4 = img4.resize((210, 230), Image.LANCZOS)  # Corrected
        self.photoimg4 = ImageTk.PhotoImage(img4)
        lblimg4 = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lblimg4.place(x=0, y=225, width=210, height=230)

def logout():
    root.destroy()
def open_roomservice():
    Room_service_root = Toplevel()
    obj = roomservice.Room_service(Room_service_root)

def open_customer_window():
    customer_root = Toplevel()
    obj = customer.Customer_window(customer_root)

def open_details_window():
    details_root = Toplevel()
    obj = Details.Details(details_root) 
   
if __name__ == "__main__":
    root = Tk()
    ob = HotelManegementSystem(root)  # Corrected instantiation
    root.mainloop()
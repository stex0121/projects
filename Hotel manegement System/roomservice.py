from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random
import mysql.connector
from tkinter import messagebox
from datetime import datetime

class Room_service:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x450+230+220")
###################################### VARIABLES VARIABLES VARIABLES #########################
        self.cust_contact=StringVar()
        self.check_in_date=StringVar()
        self.check_out_date=StringVar()
        self.room_type=StringVar()
        self.avaible_room=StringVar()
        self.meal=StringVar()
        self.no_of_days=StringVar()
        self.paid_tax=StringVar()
        self.Sub_total=StringVar()
        self.Total_cost=StringVar()

        ############################ TITLE TITLE TITLE #####################################

        lbl_title = Label(self.root, text="ROOM BOOKING DETAILS ", font=("Arial", 18, "bold"), bg="black", fg="gold")
        lbl_title.place(x=0, y=0, width=1295, height=50)

        ############################ LOGO LOGO LOGO #####################################
        img2 = Image.open(r"C:\Users\user\Desktop\Hotel manegement System\logohotel.png")
        img2 = img2.resize((100, 50), Image.LANCZOS)  # Corrected
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg1 = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg1.place(x=0, y=0, width=100, height=50)

        ################### LABEL FRAME LABEL FRAME LABEL FRAME #############################
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="ROOM BOOKING Details",font=("Arial", 12, "bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)

        ###### CUSTOMER Contact############
        lbl_cust_contact=Label(labelframeleft,text="Customer contact:",font=("Arial", 9, "bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)
        entry_contact=ttk.Entry(labelframeleft,width=22,font=("Arial", 9, "bold"),textvariable=self.cust_contact)
        entry_contact.grid(row=0,column=1,sticky=W)
        #fetch data
        btnfetch_data=Button(labelframeleft,text="Fetch data",font=("Arial", 8, "bold"),bg='black',fg='gold',width=8,command=self.fetch_Contact)
        btnfetch_data.place(x=330,y=4)
        

        #check_in_date#
        check_in_date=Label(labelframeleft,font=("Arial", 9, "bold"),text="Check in date:",padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)
        txtcheck_in_date=ttk.Entry(labelframeleft,font=("Arial", 9, "bold"),width=29,textvariable=self.check_in_date)
        txtcheck_in_date.grid(row=1,column=1)
        #check_out_date#
        check_out_date=Label(labelframeleft,font=("Arial", 9, "bold"),text="Check out date:",padx=2,pady=6,)
        check_out_date.grid(row=2,column=0,sticky=W)
        txtcheck_out_date = ttk.Entry(labelframeleft, font=("Arial", 9, "bold"), width=29, state="normal",textvariable=self.check_out_date)
        txtcheck_out_date.grid(row=2, column=1)
        #room_type#
        room_type=Label(labelframeleft,font=("Arial", 9, "bold"),text="Room type",padx=2,pady=6)
        room_type.grid(row=3,column=0,sticky=W)
        room_type_gender=ttk.Combobox(labelframeleft,font=("Arial", 9, "bold"),width=27,state="readonly",textvariable=self.room_type)
        room_type_gender["value"]=("Single","Double","Luxury")
        room_type_gender.current(0)
        room_type_gender.grid(row=3,column=1)
        #avaible_room
        avaible_room=Label(labelframeleft,font=("Arial", 9, "bold"),text="Avaible room:",padx=2,pady=6)
        avaible_room.grid(row=4,column=0,sticky=W)
        txtavaible_room=ttk.Entry(labelframeleft,font=("Arial",9, "bold"),width=29,textvariable=self.avaible_room)
        txtavaible_room.grid(row=4,column=1)

        #meal#
        meal=Label(labelframeleft,font=("Arial", 9, "bold"),text="Meal :",padx=2,pady=6)
        meal.grid(row=5,column=0,sticky=W)
        txtmeal=ttk.Entry(labelframeleft,font=("Arial", 9, "bold"),width=29,textvariable=self.meal)
        txtmeal.grid(row=5,column=1)
        #no of days:
        no_of_days=Label(labelframeleft,font=("Arial", 9, "bold"),text="Number of days:",padx=2,pady=6)
        no_of_days.grid(row=6,column=0,sticky=W)
        txtno_of_days=ttk.Entry(labelframeleft,font=("Arial", 9, "bold"),width=29,textvariable=self.no_of_days)
        txtno_of_days.grid(row=6,column=1)
        #paid_tax
        paid_tax=Label(labelframeleft,font=("Arial", 9, "bold"),text="Paid Tax:",padx=2,pady=6)
        paid_tax.grid(row=7,column=0,sticky=W)
        txtpaid_tax=ttk.Entry(labelframeleft,font=("Arial", 9, "bold"),width=29,textvariable=self.paid_tax)
        txtpaid_tax.grid(row=7,column=1)
        #Sub_total
        Sub_total=Label(labelframeleft,font=("Arial", 9, "bold"),text="Sub total:",padx=2,pady=6)
        Sub_total.grid(row=8,column=0,sticky=W)
        txtSub_total=ttk.Entry(labelframeleft,font=("Arial", 9, "bold"),width=29,textvariable=self.Sub_total)
        txtSub_total.grid(row=8,column=1)
        #Total_cost
        Total_cost=Label(labelframeleft,font=("Arial", 9, "bold"),text="Total Cost:",padx=2,pady=6)
        Total_cost.grid(row=9,column=0,sticky=W)
        txtTotal_cost=ttk.Entry(labelframeleft,font=("Arial", 9, "bold"),width=29,textvariable=self.Total_cost) 
        txtTotal_cost.grid(row=9,column=1) 
##################################### BUTON BILL BUTTON BILL BUTTON BILL####################

        btnBill=Button(labelframeleft,text="Bill",font=("Arial", 12, "bold"),bg='black',fg='gold',width=9,command=self.total)
        btnBill.grid(row=11,column=0,padx=1,sticky=W)
        ############################## BUTTON FRAME BUTTTON FRAME BUTTON FRAMRE #########################
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",font=("Arial", 12, "bold"),bg='black',fg='gold',width=9,command=self.add_data)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",font=("Arial", 12, "bold"),bg='black',fg='gold',width=9,command=self.update_data)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",font=("Arial", 12, "bold"),bg='black',fg='gold',width=9,command=self.delete)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",font=("Arial", 12, "bold"),bg='black',fg='gold',width=9,command=self.reset)
        btnReset.grid(row=0,column=3,padx=1) 

        ############################ TABLE FRAME Search System TABLE FRAME TABLE FRAME ######################################

        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search System",font=("Arial", 12, "bold"),padx=2)
        Table_Frame.place(x=435,y=280,width=800,height=260)
        lblSearchBy=Label(Table_Frame,font=("Arial", 12, "bold"),text="Search By:",bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)
        self.search_var=StringVar()
        combo_Search=ttk.Combobox(Table_Frame,font=("Arial", 12, "bold"),width=24,state="readonly",textvariable=self.search_var)
        combo_Search["value"]=("Contact","Room")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1,padx=2)
        self.txt_Search=StringVar()
        txtSearch=ttk.Entry(Table_Frame,font=("Arial", 9, "bold"),width=24,textvariable=self.txt_Search) 
        txtSearch.grid(row=0,column=2,padx=2) 

        btnSearch=Button(Table_Frame,text="Search",font=("Arial", 9, "bold"),bg='black',fg='gold',width=9)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowAll=Button(Table_Frame,text="Show All",font=("Arial", 9, "bold"),bg='black',fg='gold',width=9)
        btnShowAll.grid(row=0,column=4,padx=1)

        ######################### RIGHT SIDE IMAGE RIGHT  SIDE IMAGE############################

        img3 = Image.open(r"C:\Users\user\Desktop\Hotel manegement System\bed.jpeg")
        img3 = img3.resize((550, 220), Image.LANCZOS)  # Corrected
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lblimg3 = Label(self.root, image=self.photoimg3, bd=0, relief=RIDGE)
        lblimg3.place(x=600, y=55, width=550, height=220)

        ################################## SHOW TADA TABLE SHOW DATA TABLE SHOW DATA TABLE ####################
        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=800,height=190)
        
        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)
        self.roomservice_Table=ttk.Treeview(details_table,column=("cust_contact","check_in_date","check_out_date","room_type","avaible_room","meal","no_of_days","paid_tax","Sub_total","Total_cost"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.roomservice_Table.xview)
        scroll_y.config(command=self.roomservice_Table.yview)

        self.roomservice_Table.heading("cust_contact",text="Customer contact")
        self.roomservice_Table.heading("check_in_date",text="Check in date ")
        self.roomservice_Table.heading("check_out_date",text="Check out date ")
        self.roomservice_Table.heading("room_type",text="Room Type")
        self.roomservice_Table.heading("avaible_room",text="Avaible Room")
        self.roomservice_Table.heading("meal",text="Meal")
        self.roomservice_Table.heading("no_of_days",text="Number of days ")
        self.roomservice_Table.heading("paid_tax",text="Paid Tax")
        self.roomservice_Table.heading("Sub_total",text="Sub Total")
        self.roomservice_Table.heading("Total_cost",text="Total Cost")
        
        
        self.roomservice_Table["show"]="headings"

        self.roomservice_Table.column("cust_contact",width=100)
        self.roomservice_Table.column("check_in_date",width=100)
        self.roomservice_Table.column("check_out_date",width=100)
        self.roomservice_Table.column("room_type",width=100)
        self.roomservice_Table.column("avaible_room",width=100)
        self.roomservice_Table.column("meal",width=100)
        self.roomservice_Table.column("no_of_days",width=100)
        self.roomservice_Table.column("paid_tax",width=100)
        self.roomservice_Table.column("Sub_total",width=100)
        self.roomservice_Table.column("Total_cost",width=100)
        


        self.roomservice_Table.pack(fill=BOTH,expand=1)
        self.roomservice_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def fetch_Contact(self):
        if self.cust_contact.get() == "":
            messagebox.showerror("Error", "Please enter Contact Number", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host='localhost',
                    username='root',
                    password='123456789',
                    database='Mydata'
                )
                # Create a cursor object
                my_cursor = conn.cursor()
                query = "SELECT * FROM roombooking WHERE cust_contact=%s"
                values = (self.cust_contact.get(),)
                my_cursor.execute(query, values)

                row = my_cursor.fetchone()
                conn.commit()
                conn.close()

                if row is None:
                    messagebox.showerror("Error", "This number is not found.", parent=self.root)
                else:
                    showDataframe = Frame(self.root, bd=4, relief=RIDGE, padx=2)
                    showDataframe.place(x=455, y=55, width=300, height=180)

                    lblName = Label(showDataframe, text="Name", font=("arial", 12, "bold"))
                    lblName.place(x=0, y=0)

                    lbl = Label(showDataframe, text=row[0], font=("arial", 12, "bold"))
                    lbl2 = Label(showDataframe, text=row[1], font=("arial", 12, "bold"))
                    lbl3 = Label(showDataframe, text=row[2], font=("arial", 12, "bold"))  # Accessing the first element of the tuple
                    lbl.place(x=90, y=0)
                    lbl2.place(x=90, y=40)
                    lbl3.place(x=90, y=80)
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error: {err}", parent=self.root)

    def add_data(self):
    # Check if any required fields are empty
            if any([
                self.cust_contact.get()=="",        
                self.check_in_date.get() == "",
                self.check_out_date.get() == "",
                self.room_type.get() == "",
                self.avaible_room.get() == "",
                self.meal.get() == "",
                self.no_of_days.get() == "",
                
            ]):
                messagebox.showerror("Error", "All fields are required", parent=self.root)
            else:
                try:
                    # Connect to the database
                    conn = mysql.connector.connect(
                        host='localhost', 
                        username='root', 
                        password='123456789', 
                        database='Mydata'
                    )
                    # Create a cursor object
                    my_cursor = conn.cursor()
                    
                    # Execute the INSERT statement
                    query = """INSERT INTO roombooking 
                            VALUES (%s, %s, %s, %s, %s, %s, %s)"""
                    values = (
                        self.cust_contact.get(),
                        self.check_in_date.get(),
                        self.check_out_date.get(),
                        self.room_type.get(),
                        self.avaible_room.get(),
                        self.meal.get(),
                        self.no_of_days.get(),
                        
                        
                    )
                    my_cursor.execute(query, values)
                    
                    # Commit changes and close connection
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    
                    # Show success message
                    messagebox.showinfo("Success", "Room has been added", parent=self.root)
                except Exception as es:
                    # Show error message if an exception occurs
                    messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)
    #fetchdata
    def fetch_data(self):
        try:
            conn = mysql.connector.connect(
                host='localhost', 
                username='root', 
                password='123456789', 
                database='Mydata'
            )
            my_cursor = conn.cursor()
            
            my_cursor.execute("SELECT * FROM roombooking")
            rows = my_cursor.fetchall()
            
            if rows:
                # Clear existing data in the table
                self.roomservice_Table.delete(*self.roomservice_Table.get_children())
                
                # Insert fetched data into the table
                for row in rows:
                    self.roomservice_Table.insert("", END, values=row)
                
                # Commit and close the connection
                conn.commit()
                conn.close()
            else:
                messagebox.showinfo("Info", "No data found", parent=self.root)
        except Exception as e:
            messagebox.showerror("Error", f"Error fetching data: {str(e)}", parent=self.root)
    #get_cursor
    def get_cursor(self, event=""):
        cursor_row = self.roomservice_Table.focus()
        content = self.roomservice_Table.item(cursor_row)
        row = content['values']
    
        print("Row values:", row)  # Debugging statement
    
    # Set Tkinter StringVar variables
        self.cust_contact.set(row[0])
        self.check_in_date.set(row[1])
        self.check_out_date.set(row[2])
        self.room_type.set(row[3])
        self.avaible_room.set(row[4])
        self.meal.set(row[5])
        self.no_of_days.set(row[6])
        self.paid_tax.set(row[7])
        self.Sub_total.set(row[8])
        self.Total_cost.set(row[9])
    #update_function
    def update_data(self):
        try:
            conn = mysql.connector.connect(
                host='localhost',
                username='root',
                password='123456789',
                database='Mydata'
            )
            my_cursor = conn.cursor()

            update_query = """UPDATE roombooking 
                            SET   check_in_date=%s, check_out_date=%s, room_type=%s, avaible_room=%s, 
                                meal=%s, no_of_days=%s
                            WHERE cust_contact=%s"""

            data = (
                self.check_in_date.get(),
                self.check_out_date.get(),
                self.room_type.get(),
                self.avaible_room.get(),
                self.meal.get(),
                self.no_of_days.get(),
                self.cust_contact.get(),  # Added cust_contact value
            )

            my_cursor.execute(update_query, data)
            conn.commit()
            self.fetch_data()
            conn.close()

            messagebox.showinfo("Success", "Customer data updated successfully", parent=self.root)
        except Exception as e:
            messagebox.showerror("Error", f"Error updating customer data: {str(e)}", parent=self.root)
    
    def delete(self):
        delete = messagebox.askyesno("Hotel Management System", "Do you want to delete this Room", parent=self.root)
        if delete:
            try:
                conn = mysql.connector.connect(
                    host='localhost', 
                    username='root', 
                    password='123456789', 
                    database='Mydata'
                )
                my_cursor = conn.cursor()
                query = "DELETE FROM Customer contact WHERE cust_contact=%s"  # Corrected column name here
                value = (self.cust_contact.get(),)
                my_cursor.execute(query, value)
                conn.commit()
                conn.close()
                self.fetch_data()
                messagebox.showinfo("Success", "Customer deleted successfully", parent=self.root)
            except mysql.connector.Error as err:
                messagebox.showerror("MySQL Error", f"MySQL error: {err}", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"Error deleting customer: {str(e)}", parent=self.root)

        
    def reset(self):
        
        self.cust_contact.set("")
        self.check_in_date.set("")
        self.check_out_date.set("")
        self.room_type.set("")
        self.no_of_days.set("")
        self.avaible_room.set("")
        self.meal.set("")
        self.paid_tax.set("")
        self.Sub_total.set("")
        self.Total_cost.set("")

    def total(self):
        InDate = datetime.strptime(self.check_in_date.get(), "%m/%d/%Y")
        outDate = datetime.strptime(self.check_out_date.get(), "%m/%d/%Y")
        
        no_of_days = abs((outDate - InDate).days)
        self.no_of_days.set(no_of_days)

        #if self.meal.get() == "Breakfast" and self.room_type.get() == "Luxury":
        q1 = float(300)
        q2 = float(1500)
        q3 = float(no_of_days)
        q4 = float(q1 + q2)
        q5 = float(q3 + q4)
        Tax = "RSD" + str("%.2f" % (q5 * 0.1))
        ST = "RSD" + str("%.2f" % (q5))
        TT = "RSD" + str("%.2f" % (q5 + (q5) * 0.1))
        self.paid_tax.set(Tax)
        self.Sub_total.set(ST)  # Make sure you have defined Sub_total method
        self.Total_cost.set(TT)

if __name__ == "__main__":
    root = Tk()
    obj =Room_service(root)
    root.mainloop()
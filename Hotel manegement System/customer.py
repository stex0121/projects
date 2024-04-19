from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random
import mysql.connector
from tkinter import messagebox

class Customer_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x450+230+220")
##############################################################################################################
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))
        self.var_cust_name=StringVar()
        self.var_father=StringVar()
        self.var_gender=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_adress=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()
        self.var_post=StringVar()


        ############################ TITLE TITLE TITLE #####################################

        lbl_title = Label(self.root, text="ADD CUSTOMER DETAILS", font=("Arial", 18, "bold"), bg="black", fg="gold")
        lbl_title.place(x=0, y=0, width=1295, height=50)

        ############################ LOGO LOGO LOGO #####################################
        img2 = Image.open(r"C:\Users\user\Desktop\Hotel manegement System\logohotel.png")
        img2 = img2.resize((100, 50), Image.LANCZOS)  # Corrected
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg1 = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg1.place(x=0, y=0, width=100, height=50)
        ################### LABEL FRAME LABEL FRAME LABEL FRAME #############################
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("Arial", 12, "bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)
        ################################## LABELS AND ENTRY ################################
        ###### CUSTOMER REF############
        lbl_cust_ref=Label(labelframeleft,text="Customer Ref:",font=("Arial", 9, "bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)
        entry_ref=ttk.Entry(labelframeleft,width=22,font=("Arial", 9, "bold"),state="readonly",textvariable=self.var_ref)
        entry_ref.grid(row=0,column=1)
        #CUSTOMER NAME#
        cname=Label(labelframeleft,font=("Arial", 9, "bold"),text="Customer Name:",padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)
        txtcname=ttk.Entry(labelframeleft,font=("Arial", 9, "bold"),width=29,textvariable=self.var_cust_name)
        txtcname.grid(row=1,column=1)
        #Fathers Name#
        lblfname=Label(labelframeleft,font=("Arial", 9, "bold"),text="Fathers Name:",padx=2,pady=6,)
        lblfname.grid(row=2,column=0,sticky=W)
        txtfname = ttk.Entry(labelframeleft, font=("Arial", 9, "bold"), width=29, state="normal",textvariable=self.var_father)
        txtfname.grid(row=2, column=1)
        #Gender Combobox#
        label_gender=Label(labelframeleft,font=("Arial", 9, "bold"),text="Gender",padx=2,pady=6)
        label_gender.grid(row=3,column=0,sticky=W)
        combo_gender=ttk.Combobox(labelframeleft,font=("Arial", 9, "bold"),width=27,state="readonly",textvariable=self.var_gender)
        combo_gender["value"]=("Male","Female")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)
        #post code#
        postcode=Label(labelframeleft,font=("Arial", 9, "bold"),text="Post code:",padx=2,pady=6)
        postcode.grid(row=4,column=0,sticky=W)
        txtpostcode=ttk.Entry(labelframeleft,font=("Arial",9, "bold"),width=29,textvariable=self.var_post)
        txtpostcode.grid(row=4,column=1)
        #mobile number#
        mn=Label(labelframeleft,font=("Arial", 9, "bold"),text="Mobile Number :",padx=2,pady=6)
        mn.grid(row=5,column=0,sticky=W)
        txtmn=ttk.Entry(labelframeleft,font=("Arial", 9, "bold"),width=29,textvariable=self.var_mobile)
        txtmn.grid(row=5,column=1)
        #email#
        email=Label(labelframeleft,font=("Arial", 9, "bold"),text="E mail:",padx=2,pady=6)
        email.grid(row=6,column=0,sticky=W)
        txtmail=ttk.Entry(labelframeleft,font=("Arial", 9, "bold"),width=29,textvariable=self.var_email)
        txtmail.grid(row=6,column=1)
        #nationality#
        nationality=Label(labelframeleft,font=("Arial", 9, "bold"),text="Nationality:",padx=2,pady=6)
        nationality.grid(row=7,column=0,sticky=W)
        txtnationality=ttk.Entry(labelframeleft,font=("Arial", 9, "bold"),width=29,textvariable=self.var_nationality)
        txtnationality.grid(row=7,column=1)
        combo_nationality=ttk.Combobox(labelframeleft,font=("Arial", 9, "bold"),width=27,state="readonly",textvariable=self.var_nationality)
        combo_nationality["value"]=("Serbian","Croatian","German","Indian","Chinese","Bosnian","Italian","Spain")
        combo_nationality.current(0)
        combo_nationality.grid(row=7,column=1)
        
        #ID proof type combobox
        lblIdProof=Label(labelframeleft,font=("Arial", 9, "bold"),text="ID proof:",padx=2,pady=6)
        lblIdProof.grid(row=8,column=0,sticky=W)
        combo_IDproof=ttk.Combobox(labelframeleft,font=("Arial", 9, "bold"),width=27,state="readonly",textvariable=self.var_id_proof)
        combo_IDproof["value"]=("Passport","Indetification Card","Driving Licence")
        combo_IDproof.current(0)
        combo_IDproof.grid(row=8,column=1)
           
        # Indetification Number#
        lblIDnumber=Label(labelframeleft,font=("Arial", 9, "bold"),text="Indetification Number:",padx=2,pady=6)
        lblIDnumber.grid(row=9,column=0,sticky=W)
        txtIdNumber=ttk.Entry(labelframeleft,font=("Arial", 9, "bold"),width=29,textvariable=self.var_id_number) 
        txtIdNumber.grid(row=9,column=1)   
        #Adress
        lblAdress=Label(labelframeleft,font=("Arial", 9, "bold"),text="Adress:",padx=2,pady=6)
        lblAdress.grid(row=10,column=0,sticky=W)
        txtAdress=ttk.Entry(labelframeleft,font=("Arial", 9, "bold"),width=29,textvariable=self.var_adress) 
        txtAdress.grid(row=10,column=1) 
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
############################ TABLE FRAME TABLE FRAME TABLE FRAME ######################################

        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search System",font=("Arial", 12, "bold"),padx=2)
        Table_Frame.place(x=435,y=50,width=800,height=490)
        lblSearchBy=Label(Table_Frame,font=("Arial", 12, "bold"),text="Search By:",bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)
        self.search_var=StringVar()
        combo_Search=ttk.Combobox(Table_Frame,font=("Arial", 12, "bold"),width=24,state="readonly",textvariable=self.search_var)
        combo_Search["value"]=("Mobile","Ref")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1,padx=2)
        self.txt_Search=StringVar()
        txtSearch=ttk.Entry(Table_Frame,font=("Arial", 9, "bold"),width=24,textvariable=self.txt_Search) 
        txtSearch.grid(row=0,column=2,padx=2) 

        btnSearch=Button(Table_Frame,text="Search",font=("Arial", 9, "bold"),bg='black',fg='gold',width=9,command=self.search)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowAll=Button(Table_Frame,text="Show All",font=("Arial", 9, "bold"),bg='black',fg='gold',width=9,command=self.get_cursor)
        btnShowAll.grid(row=0,column=4,padx=1)
################################## SHOW TADA TABLE SHOW DATA TABLE SHOW DATA TABLE ####################
        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=800,height=350)
        
        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)
        self.Cust_Details_Table=ttk.Treeview(details_table,column=("ref","cust_name","father","gender","post","mobile","email","nationality","id_proof","id_number","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref",text="Refer No")
        self.Cust_Details_Table.heading("cust_name",text="Name ")
        self.Cust_Details_Table.heading("father",text="Fathers Name")
        self.Cust_Details_Table.heading("gender",text="Gender")
        self.Cust_Details_Table.heading("post",text="Post Code")
        self.Cust_Details_Table.heading("mobile",text="Mobile")
        self.Cust_Details_Table.heading("email",text="Email ")
        self.Cust_Details_Table.heading("nationality",text="Nationality")
        self.Cust_Details_Table.heading("id_proof",text="Id proof")
        self.Cust_Details_Table.heading("id_number",text="Id Number")
        self.Cust_Details_Table.heading("address",text="Adress")
        
        self.Cust_Details_Table["show"]="headings"

        self.Cust_Details_Table.column("ref",width=100)
        self.Cust_Details_Table.column("cust_name",width=100)
        self.Cust_Details_Table.column("father",width=100)
        self.Cust_Details_Table.column("gender",width=100)
        self.Cust_Details_Table.column("post",width=100)
        self.Cust_Details_Table.column("mobile",width=100)
        self.Cust_Details_Table.column("email",width=100)
        self.Cust_Details_Table.column("nationality",width=100)
        self.Cust_Details_Table.column("id_proof",width=100)
        self.Cust_Details_Table.column("id_number",width=100)
        self.Cust_Details_Table.column("address",width=100)


        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
    # Check if any required fields are empty
        if any([
            self.var_ref.get()=="",        
            self.var_mobile.get() == "",
            self.var_cust_name.get() == "",
            self.var_father.get() == "",
            self.var_gender.get() == "",
            self.var_post.get() == "",
            self.var_email.get() == "",
            self.var_nationality.get() == "",
            self.var_id_proof.get() == "",
            self.var_id_number.get() == "",
            self.var_adress.get() == ""
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
                query = """INSERT INTO customer 
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                values = (
                    self.var_ref.get(),
                    self.var_cust_name.get(),
                    self.var_father.get(),
                    self.var_gender.get(),
                    self.var_post.get(),
                    self.var_mobile.get(),
                    self.var_email.get(),
                    self.var_nationality.get(),
                    self.var_id_proof.get(),
                    self.var_id_number.get(),
                    self.var_adress.get()
                )
                my_cursor.execute(query, values)
                
                # Commit changes and close connection
                conn.commit()
                self.fetch_data()
                conn.close()
                
                # Show success message
                messagebox.showinfo("Success", "Customer has been added", parent=self.root)
            except Exception as es:
                # Show error message if an exception occurs
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

    def fetch_data(self): ########### za fetch Details################
        try:
            conn = mysql.connector.connect(
                host='localhost', 
                username='root', 
                password='123456789', 
                database='Mydata'
            )
            my_cursor = conn.cursor()
            
            my_cursor.execute("SELECT * FROM customer")
            rows = my_cursor.fetchall()
            
            if rows:
                # Clear existing data in the table
                self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
                
                # Insert fetched data into the table
                for row in rows:
                    self.Cust_Details_Table.insert("", END, values=row)
                
                # Commit and close the connection
                conn.commit()
                conn.close()
            else:
                messagebox.showinfo("Info", "No data found", parent=self.root)
        except Exception as e:
            messagebox.showerror("Error", f"Error fetching data: {str(e)}", parent=self.root)

    def get_cursor(self, event=""):
        cursor_row = self.Cust_Details_Table.focus()
        content = self.Cust_Details_Table.item(cursor_row)
        row = content['values']
    
        print("Row values:", row)  # Debugging statement
    
    # Set Tkinter StringVar variables
        self.var_ref.set(row[0])
        self.var_cust_name.set(row[1])
        self.var_father.set(row[2])
        self.var_gender.set(row[3])
        self.var_post.set(row[4])
        self.var_mobile.set(row[5])
        self.var_email.set(row[6])
        self.var_nationality.set(row[7])
        self.var_id_proof.set(row[8])
        self.var_id_number.set(row[9])
        self.var_adress.set(row[10])

    def update_data(self):
        try:
            conn = mysql.connector.connect(
                host='localhost', 
                username='root', 
                password='123456789', 
                database='Mydata'
            )
            my_cursor = conn.cursor()
            
            update_query = """UPDATE customer 
                            SET cust_name=%s, father=%s, gender=%s, post=%s, mobile=%s, 
                                email=%s, nationality=%s, id_proof=%s, id_number=%s, address=%s 
                            WHERE ref=%s"""
            
            data = (
                self.var_cust_name.get(),
                self.var_father.get(),
                self.var_gender.get(),
                self.var_post.get(),
                self.var_mobile.get(),
                self.var_email.get(),
                self.var_nationality.get(),
                self.var_id_proof.get(),
                self.var_id_number.get(),
                self.var_adress.get(),
                self.var_ref.get()
            )
            
            my_cursor.execute(update_query, data)
            conn.commit()
            self.fetch_data()
            conn.close()
            
            messagebox.showinfo("Success", "Customer data updated successfully", parent=self.root)
        except Exception as e:
            messagebox.showerror("Error", f"Error updating customer data: {str(e)}", parent=self.root)
    
    def delete(self):
        delete = messagebox.askyesno("Hotel Management System", "Do you want to delete this customer", parent=self.root)
        if delete:
            try:
                conn = mysql.connector.connect(
                    host='localhost', 
                    username='root', 
                    password='123456789', 
                    database='Mydata'
                )
                my_cursor = conn.cursor()
                query = "DELETE FROM customer WHERE Ref=%s"
                value = (self.var_ref.get(),)
                my_cursor.execute(query, value)
                conn.commit()
                conn.close()
                self.fetch_data()
                messagebox.showinfo("Success", "Customer deleted successfully", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"Error deleting customer: {str(e)}", parent=self.root)
        else:
            return
    
    def reset(self):
        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))
        # Reset all other variables
        self.var_cust_name.set("")
        self.var_father.set("")
        self.var_post.set("")
        self.var_mobile.set("")
        self.var_email.set("")
        self.var_id_number.set("")
        self.var_adress.set("")
        self.var_id_proof("")
                
    def search(self):
        try:
            conn = mysql.connector.connect(
                host='localhost',
                username='root',
                password='123456789',
                database='Mydata'
            )
            my_cursor = conn.cursor()

            query = "SELECT * FROM customer"
            # Using parameterized query to prevent SQL injection
            if(self.search_var.get() == "Mobile"):
                query = "SELECT * FROM customer WHERE mobile LIKE %s"
            elif(self.search_var.get() == "Ref"):
                query = "SELECT * FROM customer WHERE ref LIKE %s"
            
            search_value = "%" + self.txt_Search.get() + "%"  # Adding wildcards for partial search
            my_cursor.execute(query, (search_value,))

            rows = my_cursor.fetchall()

            if len(rows) != 0:
                self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
                for i in rows:
                    self.Cust_Details_Table.insert("", END, values=i)
                conn.commit()
            else:
                messagebox.showinfo("No Results", "No matching records found", parent=self.root)

        except mysql.connector.Error as err:
            messagebox.showerror("MySQL Error", f"MySQL error: {err}", parent=self.root)
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}", parent=self.root)
        finally:
            if conn.is_connected():
                conn.close()
                


if __name__ == "__main__":
    root = Tk()
    obj =Customer_window(root)
    root.mainloop()
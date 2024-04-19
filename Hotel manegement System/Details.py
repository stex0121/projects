from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox

class Details:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x450+230+220")

        ############################ TITLE #####################################
        lbl_title = Label(self.root, text=" Details ", font=("Arial", 18, "bold"), bg="black", fg="gold")
        lbl_title.place(x=0, y=0, width=1295, height=50)

        ############################ LOGO #####################################
        img2 = Image.open(r"C:\Users\user\Desktop\Hotel manegement System\logohotel.png")
        img2 = img2.resize((100, 50), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg1 = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg1.place(x=0, y=0, width=100, height=50)

        ################### LABEL FRAME #####################################
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text=" ADD A NEW ROOM", font=("Arial", 12, "bold"), padx=2)
        labelframeleft.place(x=5, y=50, width=540, height=350)

        ######Floor############
        self.var_floor = StringVar()
        lbl_floor = Label(labelframeleft, text="Floor:", font=("Arial", 9, "bold"), padx=2, pady=6)
        lbl_floor.grid(row=0, column=0, sticky=W)
        entry_floor = ttk.Entry(labelframeleft, width=22, font=("Arial", 9, "bold"), textvariable=self.var_floor)
        entry_floor.grid(row=0, column=1, sticky=W)

        ################# ROOM NUMBER ###################
        self.var_room_no = StringVar()
        lbl_room_no = Label(labelframeleft, text="Room number:", font=("Arial", 9, "bold"), padx=2, pady=6)
        lbl_room_no.grid(row=1, column=0, sticky=W)
        entry_room_no = ttk.Entry(labelframeleft, width=22, font=("Arial", 9, "bold"), textvariable=self.var_room_no)
        entry_room_no.grid(row=1, column=1, sticky=W)

        ####################### ROOM TYPE ##################
        self.var_room_type = StringVar()
        lbl_room_type = Label(labelframeleft, text="Room type:", font=("Arial", 9, "bold"), padx=2, pady=6)
        lbl_room_type.grid(row=2, column=0, sticky=W)
        entry_room_type = ttk.Entry(labelframeleft, width=22, font=("Arial", 9, "bold"), textvariable=self.var_room_type)
        entry_room_type.grid(row=2, column=1, sticky=W)

        ############################## BUTTON FRAME #########################
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=200, width=412, height=40)

        btnAdd = Button(btn_frame, text="Add", font=("Arial", 12, "bold"), bg='black', fg='gold', width=9, command=self.add_data)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame, text="Update", font=("Arial", 12, "bold"), bg='black', fg='gold', width=9, command=self.update_data)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="Delete", font=("Arial", 12, "bold"), bg='black', fg='gold', width=9, command=self.delete)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Reset", font=("Arial", 12, "bold"), bg='black', fg='gold', width=9, command=self.reset)
        btnReset.grid(row=0, column=3, padx=1) 

        ############################ TABLE FRAME ##############################
        table_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="SHOW ROOM Details", font=("Arial", 12, "bold"), padx=2)
        table_frame.place(x=600, y=55, width=600, height=350)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.room_table = ttk.Treeview(table_frame, columns=("Floor", "Room_number", "Room_type"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("Floor", text="Floor")
        self.room_table.heading("Room_number", text="Room Number")
        self.room_table.heading("Room_type", text="Room type")

        self.room_table["show"] = "headings"

        self.room_table.column("Floor", width=100)
        self.room_table.column("Room_number", width=100)
        self.room_table.column("Room_type", width=100)
        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind('<ButtonRelease-1>', self.on_tree_click)
      
        self.room_table.pack()
        
        ################# FETCH DATA AND POPULATE TREEVIEW ##################
        try:
            conn = mysql.connector.connect(
                host='localhost', 
                username='root', 
                password='123456789', 
                database='Mydata'
            )
            my_cursor = conn.cursor()
            
            # Execute your SELECT query
            query = "SELECT Floor, Room_number, Room_type FROM details"
            my_cursor.execute(query)
            
            # Fetch all rows from the result
            rows = my_cursor.fetchall()
            
            # Insert fetched data into Treeview
            for row in rows:
                self.room_table.insert("", "end", values=row)
            
            conn.close()
        except Exception as e:
            messagebox.showerror("Error", f"Error fetching data from MySQL: {str(e)}", parent=self.root)


    
    def on_tree_click(self,event):
            item = self.room_table.selection()[0]
            row_data = self.room_table.item(item, 'values')
            self.var_floor.set(row_data[0])
            self.var_room_no.set(row_data[1])
            self.var_room_type.set(row_data[2])
            # Assuming you have an Entry widget named 'entry_field'
            # self.room_table.delete(0, tk.END)
            # entry_field.insert(0, row_data[0]) 

    def add_data(self):
            if any([
                self.var_floor.get()=="",        
                self.var_room_no.get() == "",
                self.var_room_type.get() == ""            
            ]):
                messagebox.showerror("Error", "All fields are required", parent=self.root)
            else:
                try:
                    conn = mysql.connector.connect(
                        host='localhost', 
                        username='root', 
                        password='123456789', 
                        database='Mydata'
                    )
                    my_cursor = conn.cursor()
                    
                    query = """INSERT INTO details 
                            VALUES (%s, %s, %s)"""
                    values = (
                        self.var_floor.get(),
                        self.var_room_no.get(),
                        self.var_room_type.get()              
                    )
                    my_cursor.execute(query, values)
                    
                    conn.commit()
                    my_cursor.fetchall()
                    conn.close()
                    
                    messagebox.showinfo("Success", "Details have been added", parent=self.root)
                except Exception as es:
                    messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)    

    def delete(self):
        delete = messagebox.askyesno("Hotel Management System", "Do you want to delete this Floor", parent=self.root)
        if delete:
            try:
                conn = mysql.connector.connect(
                    host='localhost', 
                    username='root', 
                    password='123456789', 
                    database='Mydata'
                )
                my_cursor = conn.cursor()
                query = "DELETE FROM details WHERE floor=%s"
                value = (self.var_floor.get(),)
                my_cursor.execute(query, value)
                conn.commit()
                my_cursor.fetchall()
                conn.close()
                messagebox.showinfo("Success", "Floor deleted successfully", parent=self.root)
            except mysql.connector.Error as err:
                messagebox.showerror("MySQL Error", f"MySQL error: {err}", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"Error deleting floor: {str(e)}", parent=self.root)
        
    def reset(self):        
        self.var_floor.set("")
        self.var_room_no.set("")
        self.var_room_type.set("")  

    def update_data(self):
        try:
            conn = mysql.connector.connect(
                host='localhost',
                username='root',
                password='123456789',
                database='Mydata'
            )
            my_cursor = conn.cursor()

            update_query = """UPDATE details 
                            SET floor=%s, room_number=%s, room_type=%s
                            WHERE floor=%s"""

            data = (
                self.var_floor.get(),
                self.var_room_no.get(),
                self.var_room_type.get(),
                self.var_floor.get()
            )

            my_cursor.execute(update_query, data)
            conn.commit()
            my_cursor.fetchall()
            conn.close()

            messagebox.showinfo("Success", "Floor data updated successfully", parent=self.root)
        except Exception as e:
            messagebox.showerror("Error", f"Error updating floor data: {str(e)}", parent=self.root)  

    def get_cursor(self, event=""):
        cursor_row = self.room_table.focus()
        content = self.room_table.item(cursor_row)
        row = content['values']
    
        print("Row values:", row)  # Debugging statement
    
        self.var_floor.set(row[0])
        self.var_room_no.set(row[1])
        self.var_room_type.set(row[2])

if __name__ == "__main__":
    root = Tk()
    obj = Details(root)
    root.mainloop()
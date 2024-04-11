from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector




class Hospital:
    def __init__(self,root):

        self.root=root
        self.root.title('Hospital Management System')
        self.root.geometry('1540x800+0+0')
        self.Nameoftablets=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.Lot=StringVar()
        self.Issuedata=StringVar()
        self.ExpDate=StringVar()
        self.DailyDose=StringVar()
        self.Sideeffect=StringVar()
        self.Furtherinformation=StringVar()
        self.StorageAdvice=StringVar()
        self.Drivingusinmachine=StringVar()
        self.Howtousemedication=StringVar()
        self.patientid=StringVar()
        self.Nhsnumber=StringVar()
        self.Patientname=StringVar()
        self.DOB=StringVar()
        self.PatientAdress=StringVar()
        self.PrescriptionData = StringVar()
        self.NoOftablets=StringVar()
        self.bloodpreaseure=StringVar()
        self.patientbirthday=StringVar()
        self.roofttablets=StringVar()
        self.numberoftablets=StringVar()
        self.how_to_use_medication=StringVar()
        
        

        lbltitle=Label(root,bd=20,relief=RIDGE,text='Hospital Management System',fg='green',bg='white',font='Arial,50,bold ')
        lbltitle.pack(side=TOP,fill=X)

        Dataframe=Frame(root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=70,width=1280,height=400)

        Dataframeleft=LabelFrame(Dataframe,bd=10,padx=20,relief=RIDGE,font='arial,12,bold',text='Patient Information',)
        Dataframeleft.place(x=0,y=5,width=800,height=350)

        Dataframeright=LabelFrame(Dataframe,bd=10,padx=20,relief=RIDGE,font='arial,12,bold',text='Prescription of Medicaments')
        Dataframeright.place(x=810,y=5,width=440,height=350)

        Detailsframe=Frame(root,bd=20,relief=RIDGE)
        Detailsframe.place(x=0,y=500,width=1280,height=140)

        lblnametablet=Label(Dataframeleft,state='active',text='Names of Tablet',font='arial,12,bold',padx=2,pady=6)
        lblnametablet.grid(row=0,column=0)
        comNametablet=ttk.Combobox(Dataframeleft,font='arial,12,bold',width=33,textvariable=self.Nameoftablets)
        comNametablet['values']=('Corona vacacine','Acetaminophen','Adderall','Amlodipine','Ativan')
        comNametablet.grid(row=0,column=1)

        lbldose=Label(Dataframeleft,font='arial 9 bold',text='Dose',padx=2,pady=6)
        lbldose.grid(row=2,column=0,sticky=W)
        txtdose=Entry(Dataframeleft,font='arial 9 bold',width=15,textvariable=self.Dose)
        txtdose.grid(row=2,column=1)
        txtdose.place(x=80,y=44)
        
        lblRefNo=Label(Dataframeleft,font='arial 9 bold',text='Refferent NO:',padx=2,pady=6)
        lblRefNo.grid(row=3,column=0,sticky=W)
        txtRefNo=Entry(Dataframeleft,font='arial 9 bold',width=15,textvariable=self.ref)
        lblRefNo.place(x=-20,y=265)
        txtRefNo.grid(row=3,column=1)
        txtRefNo.place(x=80,y=270)

        lblNoOftablets=Label(Dataframeleft,font='arial 9 bold',text='No of tablets',padx=2,pady=6)
        lblNoOftablets.grid(row=3,column=0,sticky=W)
        txtNoOftablets=Entry(Dataframeleft,font='arial 9 bold',width=15,textvariable=self.NoOftablets)
        txtNoOftablets.grid(row=3,column=1)
        txtNoOftablets.place(x=80,y=78)
        
        lbllot=Label(Dataframeleft,font='arial 9 bold',text='Lot',padx=2,pady=6)
        lbllot.grid(row=4,column=0,sticky=W)
        txtlot=Entry(Dataframeleft,font='arial 9 bold',width=15,textvariable=self.Lot)
        txtlot.grid(row=4,column=1)
        txtlot.place(x=80,y=106)

        lblissuedata=Label(Dataframeleft,font='arial 9 bold',text='Issue Date',padx=2,pady=6)
        lblissuedata.grid(row=5,column=0,sticky=W)
        txtissuedata=Entry(Dataframeleft,font='arial 9 bold',width=15,textvariable=self.Issuedata)
        txtissuedata.grid(row=6,column=1)
        txtissuedata.place(x=80,y=136)
        
        lblExpdate=Label(Dataframeleft,font='arial 9 bold',text='Exp Date',padx=2,pady=6)
        lblExpdate.grid(row=6,column=0,sticky=W)
        txtExpdate=Entry(Dataframeleft,font='arial 9 bold',width=15,textvariable=self.ExpDate)
        txtExpdate.grid(row=6,column=1)
        txtExpdate.place(x=80,y=164)
        
        lblDailyDose=Label(Dataframeleft,font='arial 9 bold',text='Daily Dose:',padx=2,pady=4)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtlblDailyDose=Entry(Dataframeleft,font='arial 9 bold',width=15,textvariable=self.DailyDose)
        txtlblDailyDose.grid(row=7,column=1)
        txtlblDailyDose.place(x=80,y=196)
        
        lblsideeffect=Label(Dataframeleft,font='arial 9 bold',text='Side effect:',padx=2,pady=6)
        lblsideeffect.grid(row=8,column=0,sticky=W)
        txtsideeffect=Entry(Dataframeleft,font='arial 9 bold',width=15,textvariable=self.Sideeffect)
        txtsideeffect.grid(row=8,column=1)
        txtsideeffect.place(x=80,y=226)
        
        lblfurtherinfo=Label(Dataframeleft,font='arial 9 bold',text='Further information',padx=2)
        lblfurtherinfo.grid(row=1,column=2,sticky=W)
        lblfurtherinfo.place(x=240,y=60)
        txtfurtherinfo=Entry(Dataframeleft,font='arial 9 bold',width=15,textvariable=self.Furtherinformation)
        txtfurtherinfo.grid(row=1,column=3)
        txtfurtherinfo.place(x=360,y=60)
       
        lblbloodpreaseure=Label(Dataframeleft,font='arial 9 bold',text='Blood Preassure',padx=2,pady=6)
        lblbloodpreaseure.grid(row=2,column=2,sticky=W)
        lblbloodpreaseure.place(x=240,y=80)
        txtbloodpreaseure=Entry(Dataframeleft,font='arial 9 bold',width=15,textvariable=self.bloodpreaseure)
        txtbloodpreaseure.grid(row=2,column=3)
        txtbloodpreaseure.place(x=360,y=90)
       
        lblStorage=Label(Dataframeleft,font='arial 9 bold',text='Storage Advice',padx=2,pady=6)
        lblStorage.grid(row=3,column=2,sticky=W)
        lblStorage.place(x=240,y=110)
        txtStorage=Entry(Dataframeleft,font='arial 9 bold',width=15,textvariable=self.StorageAdvice)
        txtStorage.grid(row=3,column=3)
        txtStorage.place(x=360,y=120)
        

        lblPatientID=Label(Dataframeleft,font='arial 9 bold',text='Patient ID',padx=2,pady=6)
        lblPatientID.grid(row=4,column=2,sticky=W)
        lblPatientID.place(x=240,y=140)
        txtPatientID=Entry(Dataframeleft,font='arial 9 bold',width=15,textvariable=self.patientid)
        txtPatientID.grid(row=4,column=3)
        txtPatientID.place(x=360,y=150)
        
        lblPatientNhs=Label(Dataframeleft,font='arial 9 bold',text='Nhs Number',padx=2,pady=6)
        lblPatientNhs.grid(row=5,column=2,sticky=W)
        lblPatientNhs.place(x=240,y=170)
        txtPatientNhs=Entry(Dataframeleft,font='arial 9 bold',width=15,textvariable=self.Nhsnumber)
        txtPatientNhs.grid(row=5,column=3)
        txtPatientNhs.place(x=360,y=180)

        lblPatientname=Label(Dataframeleft,font='arial 9 bold',text='Patient name',padx=2,pady=6)
        lblPatientname.grid(row=6,column=2,sticky=W)
        lblPatientname.place(x=240,y=200)
        txtPatientname=Entry(Dataframeleft,font='arial 9 bold',width=15,textvariable=self.Patientname)
        txtPatientname.grid(row=6,column=3)
        txtPatientname.place(x=360,y=210)

        lblPatientbirthday=Label(Dataframeleft,font='arial 9 bold',text='Patient Birthday',padx=2,pady=6)
        lblPatientbirthday.grid(row=7,column=2,sticky=W)
        lblPatientbirthday.place(x=240,y=230)
        txtPatientbirthday=Entry(Dataframeleft,font='arial 9 bold',width=15,textvariable=self.patientbirthday)
        txtPatientbirthday.grid(row=6,column=3)
        txtPatientbirthday.place(x=360,y=240)
        
        lblMedicine=Label(Dataframeleft,font='arial 9 bold',text='Medicine Prescritpion',padx=2,pady=6)
        lblMedicine.grid(row=8,column=2,sticky=W)
        lblMedicine.place(x=225,y=260)
        txtMedicine=Entry(Dataframeleft,font='arial 9 bold',width=15,textvariable=self.PrescriptionData)
        txtMedicine.grid(row=8,column=3)
        txtMedicine.place(x=360,y=270)

        lblPatientadress=Label(Dataframeleft,font='arial 9 bold',text='Patient Adress',padx=2,pady=6)
        lblPatientadress.grid(row=7,column=2,sticky=W)
        lblPatientadress.place(x=500,y=50)
        txtPatientadress=Entry(Dataframeleft,font='arial 9 bold',width=15,textvariable=self.PatientAdress)
        txtPatientadress.grid(row=6,column=3)
        txtPatientadress.place(x=600,y=55)

        self.txtPrescription=Text(Dataframeright,font='arial 9 bold',width=45,height=16,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)

        btnPrescription=Button(text='Prescription',font='arial 9 bold',width=15,padx=2,pady=6,bg='blue',fg='white',command=self.prescription)
        btnPrescription.place(x=40,y=463)

        btnPrescriptiondata=Button(text='PrescriptionData',font='arial 9 bold',width=15,padx=2,pady=6,bg='blue',fg='white', command=self.prescription_data)
        btnPrescriptiondata.place(x=170,y=463)

        btnPrescriptionupdate=Button(text='Update',font='arial 9 bold',width=15,padx=2,pady=6,bg='blue',fg='white',command=self.update)
        btnPrescriptionupdate.place(x=300,y=463)

        btnPrescriptiondelete=Button(text='Delete',font='arial 9 bold',width=15,padx=2,pady=6,bg='blue',fg='white',command=self.delete)
        btnPrescriptiondelete.place(x=430,y=463)

        btnPrescriptionclear=Button(text='Clear',font='arial 9 bold',width=15,padx=2,pady=6,bg='blue',fg='white',command=self.clear)
        btnPrescriptionclear.place(x=560,y=463)
       
        btnPrescriptionexit=Button(text='Exit',font='arial 9 bold',width=15,padx=2,pady=6,bg='blue',fg='white',command=self.exit)
        btnPrescriptionexit.place(x=690,y=463)

        

        scroll_x=Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y=Scrollbar(Detailsframe,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(Detailsframe,columns=('nameoftablets','ref','dose','rooftablets','lot','issuedata','expdate','dailydose','storage','nhsnumber','pname','dob','adress','date'),xscrollcommand=scroll_y.set,yscrollcommand=scroll_x.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        


        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)
        self.hospital_table.heading("nameoftablets",text="nameoftablets")
        self.hospital_table.heading("ref",text="ref")
        self.hospital_table.heading("dose",text="dose")
        self.hospital_table.heading("rooftablets",text="rooftablets")
        self.hospital_table.heading("lot",text="lot")
        self.hospital_table.heading("issuedata",text="issuedata")
        self.hospital_table.heading("expdate",text="expdate")
        self.hospital_table.heading("dailydose",text="dailydose")
        self.hospital_table.heading("nhsnumber",text="nhsnumber")
        self.hospital_table.heading("pname",text="pname")
        self.hospital_table.heading("dob",text="dob")
        self.hospital_table.heading("adress",text="adress")
        self.hospital_table.heading("date",text="date")

        self.hospital_table.column('nameoftablets',width=100)
        self.hospital_table.column('ref',width=100)
        self.hospital_table.column('dose',width=100)
        self.hospital_table.column('rooftablets',width=100)
        self.hospital_table.column('lot',width=100)
        self.hospital_table.column('issuedata',width=100)
        self.hospital_table.column('expdate',width=100)
        self.hospital_table.column('dailydose',width=100)
        self.hospital_table.column('nhsnumber',width=100)
        self.hospital_table.column('pname',width=100)
        self.hospital_table.column('dob',width=100)
        self.hospital_table.column('adress',width=100)
        self.hospital_table.column('date',width=100)
        self.hospital_table.pack(fill=BOTH,expand=1)
        
        self.hospital_table.bind("ButtonRealese-1",self.get_cursor)

        self.fetch_data()

    def prescription_data(self):
        nameoftablets = self.Nameoftablets.get()
        ref = self.ref.get()
        daily_dose = self.DailyDose.get()
        dob = self.DOB.get()
        dose = self.Dose.get()
        exp_date = self.ExpDate.get()
        further_information = self.Furtherinformation.get()
        how_to_use_medication = self.Howtousemedication.get()
        issue_data = self.Issuedata.get()
        lot = self.Lot.get()
        nhs_number = self.Nhsnumber.get()
        patient_address = self.PatientAdress.get()
        patient_name = self.Patientname.get()

        if nameoftablets == '' or ref == '':
            messagebox.showerror('Error', 'All fields are required')
        else:
            conn = mysql.connector.connect(host='localhost', username='root', password='123456789', database='Mydata')
            my_cursor = conn.cursor()
            try:
             my_cursor.execute('INSERT INTO hospital (nameoftablets, ref, dose, lot, issuedata, expdate, dailydose, nhsnumber, pname, adress) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (
             nameoftablets, ref, dose, lot, issue_data, exp_date, daily_dose,nhs_number, patient_name, patient_address))
             conn.commit()
             messagebox.showinfo("Success", "Data inserted successfully!")
             self.fetch_data()  # Update the displayed data
            except Exception as e:
                messagebox.showerror("Error", str(e))
            conn.close()

    def update(self):
        try:
            conn = mysql.connector.connect(host='localhost', username='root', password='123456789', database='Mydata')
            my_cursor = conn.cursor()
            query = 'UPDATE hospital SET Nameoftablets = %s WHERE ref = %s'  # Replace condition_column with the appropriate column name
            # Assuming you want to update based on some condition, replace condition_column with the appropriate column name and provide the condition value
            update_values = (self.Nameoftablets.get(), self.ref.get())  # Replace 'new_tablet_name' with the new tablet name and 'condition_value' with the appropriate value
            my_cursor.execute(query, update_values)
            conn.commit()
            messagebox.showinfo("Success", "Data updated successfully")
        except Exception as e:
            messagebox.showwarning("Error", f"An error occurred: {str(e)}")
       


    def fetch_data(self):
     conn = mysql.connector.connect(host='localhost', username='root', password='123456789', database='Mydata')
     my_cursor=conn.cursor()
     my_cursor.execute("select * from hospital")
     rows=my_cursor.fetchall()
     if len(rows)!=0:
        self.hospital_table.delete(*self.hospital_table.get_children()) # Corrected typo
        for i in rows:
            self.hospital_table.insert("",END,values=i)
        conn.commit()
     conn.close()

    def get_cursor(self):
       cursor_row=self.hospital_table.focus()
       content=self.hospital_table.item(cursor_row)
       row=content["values"]
       self.Nameoftablets.set(row[0])

    def prescription(self):
       self.txtPrescription.insert(END,"name of tablets : "+self.Nameoftablets.get()+'\n\n')
       self.txtPrescription.insert(END,"Reference No : "+self.ref.get()+"\n\n")
       self.txtPrescription.insert(END,"Dose: "+self.Dose.get()+"\n\n")
       self.txtPrescription.insert(END,"Number of tablets : "+self.numberoftablets.get()+"\n\n")
       self.txtPrescription.insert(END,"Lot : "+self.Lot.get()+"\n\n")
       self.txtPrescription.insert(END,"Issue Date : "+self.Issuedata.get()+"\n\n")
       self.txtPrescription.insert(END,"Exo date : "+self.ExpDate.get()+"\n\n")
       self.txtPrescription.insert(END,"Daily dose : "+self.DailyDose.get()+"\n\n")
       self.txtPrescription.insert(END,"Side effect : "+self.Sideeffect.get()+"\n\n")
       self.txtPrescription.insert(END,"Further information : "+self.Furtherinformation.get()+"\n\n")
       self.txtPrescription.insert(END,"Storage advice :"+self.StorageAdvice.get()+"\n\n")
       self.txtPrescription.insert(END,"DrivingUsingMachine :"+self.Drivingusinmachine.get()+"\n\n")
       self.txtPrescription.insert(END,"Patient ID : "+self.patientid.get()+"\n\n")
       self.txtPrescription.insert(END,"NHS number : "+self.Nhsnumber.get()+"\n\n")
       self.txtPrescription.insert(END,"Patient Name : "+self.Patientname.get()+"\n\n")
       self.txtPrescription.insert(END,"Date of Birthay : "+self.patientbirthday.get()+"\n\n")
       self.txtPrescription.insert(END,"Patient adress : "+self.PatientAdress.get()+"\n\n")
    def delete(self):
        try:
            conn = mysql.connector.connect(host='localhost', username='root', password='123456789', database='Mydata')
            my_cursor = conn.cursor()
            
            query = "DELETE FROM hospital WHERE ref=%s"
            ref_value = self.ref.get()  # Assuming self.ref.get() returns the reference value to delete
            
            my_cursor.execute(query, (ref_value,))  # Pass parameters as a tuple
            
            conn.commit()
            conn.close()
            
            self.fetch_data()  # Assuming this method fetches and updates the displayed data
            messagebox.showinfo("Delete", "Patient has been deleted successfully")
        
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Error deleting patient: {e}")

    def clear(self):
       self.Nameoftablets.set("")
       self.ref.set("")
       self.Dose.set("")
       self.numberoftablets.set("")
       self.Lot.set("")
       self.Issuedata.set("")
       self.ExpDate.set("")
       self.DailyDose.set("")
       self.Sideeffect.set("")
       self.Furtherinformation.set("")
       self.StorageAdvice.set("")
       self.Drivingusinmachine.set("")
       self.Howtousemedication.set("")
       self.patientid.set("")
       self.Nhsnumber.set("")
       self.Patientname.set("")
       self.patientbirthday.set("")
       self.PatientAdress.set("")
       self.bloodpreaseure.set("")
       self.NoOftablets.set("")
       self.PrescriptionData.set("")
       self.txtPrescription.delete("1.0", END)
       

    def exit(self):
       exit=messagebox.askyesno("Hospital management system","Confirm you want to exit")
       if exit>0:
          root.destroy()
          return
root=Tk()
ob=Hospital(root)
root.mainloop()


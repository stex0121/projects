from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import _mysql_connector



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
        comNametablet=ttk.Combobox(Dataframeleft,font='arial,12,bold',width=33)
        comNametablet['values']=('Corona vacacine','Acetaminophen','Adderall','Amlodipine','Ativan')
        comNametablet.grid(row=0,column=1)

        lbldose=Label(Dataframeleft,font='arial 9 bold',text='Dose',padx=2,pady=6)
        lbldose.grid(row=2,column=0,sticky=W)
        txtdose=Entry(Dataframeleft,font='arial 9 bold',width=15)
        txtdose.grid(row=2,column=1)
        txtdose.place(x=80,y=44)
        
        lblRefNo=Label(Dataframeleft,font='arial 9 bold',text='Refferent NO:',padx=2,pady=6)
        lblRefNo.grid(row=3,column=0,sticky=W)
        txtRefNo=Entry(Dataframeleft,font='arial 9 bold',width=15)
        lblRefNo.place(x=-20,y=265)
        txtRefNo.grid(row=3,column=1)
        txtRefNo.place(x=80,y=270)

        lblNoOftablets=Label(Dataframeleft,font='arial 9 bold',text='No of tablets',padx=2,pady=6)
        lblNoOftablets.grid(row=3,column=0,sticky=W)
        txtNoOftablets=Entry(Dataframeleft,font='arial 9 bold',width=15)
        txtNoOftablets.grid(row=3,column=1)
        txtNoOftablets.place(x=80,y=78)
        
        lbllot=Label(Dataframeleft,font='arial 9 bold',text='Lot',padx=2,pady=6)
        lbllot.grid(row=4,column=0,sticky=W)
        txtlot=Entry(Dataframeleft,font='arial 9 bold',width=15)
        txtlot.grid(row=4,column=1)
        txtlot.place(x=80,y=106)

        lblissuedate=Label(Dataframeleft,font='arial 9 bold',text='Issue Date',padx=2,pady=6)
        lblissuedate.grid(row=5,column=0,sticky=W)
        txtissuedate=Entry(Dataframeleft,font='arial 9 bold',width=15)
        txtissuedate.grid(row=6,column=1)
        txtissuedate.place(x=80,y=136)
        
        lblExpdate=Label(Dataframeleft,font='arial 9 bold',text='Exp Date',padx=2,pady=6)
        lblExpdate.grid(row=6,column=0,sticky=W)
        txtExpdate=Entry(Dataframeleft,font='arial 9 bold',width=15)
        txtExpdate.grid(row=6,column=1)
        txtExpdate.place(x=80,y=164)
        
        lblDailyDose=Label(Dataframeleft,font='arial 9 bold',text='Daily Dose:',padx=2,pady=4)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtlblDailyDose=Entry(Dataframeleft,font='arial 9 bold',width=15)
        txtlblDailyDose.grid(row=7,column=1)
        txtlblDailyDose.place(x=80,y=196)
        
        lblsideeffect=Label(Dataframeleft,font='arial 9 bold',text='Side effect:',padx=2,pady=6)
        lblsideeffect.grid(row=8,column=0,sticky=W)
        txtsideeffect=Entry(Dataframeleft,font='arial 9 bold',width=15)
        txtsideeffect.grid(row=8,column=1)
        txtsideeffect.place(x=80,y=226)
        
        lblfurtherinfo=Label(Dataframeleft,font='arial 9 bold',text='Further information',padx=2)
        lblfurtherinfo.grid(row=1,column=2,sticky=W)
        lblfurtherinfo.place(x=240,y=60)
        txtfurtherinfo=Entry(Dataframeleft,font='arial 9 bold',width=15)
        txtfurtherinfo.grid(row=1,column=3)
        txtfurtherinfo.place(x=360,y=60)
       
        lblbloodpreaseure=Label(Dataframeleft,font='arial 9 bold',text='Blood Preassure',padx=2,pady=6)
        lblbloodpreaseure.grid(row=2,column=2,sticky=W)
        lblbloodpreaseure.place(x=240,y=80)
        txtbloodpreaseure=Entry(Dataframeleft,font='arial 9 bold',width=15)
        txtbloodpreaseure.grid(row=2,column=3)
        txtbloodpreaseure.place(x=360,y=90)
       
        lblStorage=Label(Dataframeleft,font='arial 9 bold',text='Storage Advice',padx=2,pady=6)
        lblStorage.grid(row=3,column=2,sticky=W)
        lblStorage.place(x=240,y=110)
        txtStorage=Entry(Dataframeleft,font='arial 9 bold',width=15)
        txtStorage.grid(row=3,column=3)
        txtStorage.place(x=360,y=120)
        

        lblPatientID=Label(Dataframeleft,font='arial 9 bold',text='Patient ID',padx=2,pady=6)
        lblPatientID.grid(row=4,column=2,sticky=W)
        lblPatientID.place(x=240,y=140)
        txtPatientID=Entry(Dataframeleft,font='arial 9 bold',width=15)
        txtPatientID.grid(row=4,column=3)
        txtPatientID.place(x=360,y=150)
        
        lblPatientNhs=Label(Dataframeleft,font='arial 9 bold',text='Nhs Number',padx=2,pady=6)
        lblPatientNhs.grid(row=5,column=2,sticky=W)
        lblPatientNhs.place(x=240,y=170)
        txtPatientNhs=Entry(Dataframeleft,font='arial 9 bold',width=15)
        txtPatientNhs.grid(row=5,column=3)
        txtPatientNhs.place(x=360,y=180)

        lblPatientname=Label(Dataframeleft,font='arial 9 bold',text='Patient name',padx=2,pady=6)
        lblPatientname.grid(row=6,column=2,sticky=W)
        lblPatientname.place(x=240,y=200)
        txtPatientname=Entry(Dataframeleft,font='arial 9 bold',width=15)
        txtPatientname.grid(row=6,column=3)
        txtPatientname.place(x=360,y=210)

        lblPatientbirthday=Label(Dataframeleft,font='arial 9 bold',text='Patient Birthday',padx=2,pady=6)
        lblPatientbirthday.grid(row=7,column=2,sticky=W)
        lblPatientbirthday.place(x=240,y=230)
        txtPatientbirthday=Entry(Dataframeleft,font='arial 9 bold',width=15)
        txtPatientbirthday.grid(row=6,column=3)
        txtPatientbirthday.place(x=360,y=240)
        
        lblMedicine=Label(Dataframeleft,font='arial 9 bold',text='Medicine Prescritpion',padx=2,pady=6)
        lblMedicine.grid(row=8,column=2,sticky=W)
        lblMedicine.place(x=225,y=260)
        txtMedicine=Entry(Dataframeleft,font='arial 9 bold',width=15)
        txtMedicine.grid(row=8,column=3)
        txtMedicine.place(x=360,y=270)

        lblPatientadress=Label(Dataframeleft,font='arial 9 bold',text='Patient Adress',padx=2,pady=6)
        lblPatientadress.grid(row=7,column=2,sticky=W)
        lblPatientadress.place(x=500,y=50)
        txtPatientadress=Entry(Dataframeleft,font='arial 9 bold',width=15)
        txtPatientadress.grid(row=6,column=3)
        txtPatientadress.place(x=600,y=55)

        self.txtPrescription=Text(Dataframeright,font='arial 9 bold',width=45,height=16,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)

        btnPrescription=Button(text='Prescription',font='arial 9 bold',width=15,padx=2,pady=6,bg='blue',fg='white')
        btnPrescription.place(x=40,y=463)

        btnPrescriptiondata=Button(text='PrescriptionData',font='arial 9 bold',width=15,padx=2,pady=6,bg='blue',fg='white', command=self.prescription_data)
        btnPrescriptiondata.place(x=170,y=463)

        btnPrescriptionupdate=Button(text='Update',font='arial 9 bold',width=15,padx=2,pady=6,bg='blue',fg='white')
        btnPrescriptionupdate.place(x=300,y=463)

        btnPrescriptiondelete=Button(text='Delete',font='arial 9 bold',width=15,padx=2,pady=6,bg='blue',fg='white')
        btnPrescriptiondelete.place(x=430,y=463)

        btnPrescriptionclear=Button(text='Clear',font='arial 9 bold',width=15,padx=2,pady=6,bg='blue',fg='white')
        btnPrescriptionclear.place(x=560,y=463)
       
        btnPrescriptionexit=Button(text='Exit',font='arial 9 bold',width=15,padx=2,pady=6,bg='blue',fg='white')
        btnPrescriptionexit.place(x=690,y=463)

        

        scroll_x=Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y=Scrollbar(Detailsframe,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(Detailsframe,columns=('nameoftablets','ref','dose','rooftablets','lot','issuedata','expdate','dailydose','storage','nhsnumber','pname','dob','adress','date'),xscrollcommand=scroll_y.set,yscrollcommand=scroll_x.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        


        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)
        
        self.hospital_table.heading('nameoftablets',text='nameoftablet')
        self.hospital_table.heading('ref',text='Reference No')
        self.hospital_table.heading('dose',text='Dose')
        self.hospital_table.heading('rooftablets',text='No of tablets')
        self.hospital_table.heading('lot',text='Lot')
        self.hospital_table.heading('issuedata',text='Issue data')
        self.hospital_table.heading('expdate',text='Exp date')
        self.hospital_table.heading('dailydose',text='Daily dose')
        self.hospital_table.heading('nhsnumber',text='NHS number')
        self.hospital_table.heading('pname',text='{Patient name}')
        self.hospital_table.heading('dob',text='DOB')
        self.hospital_table.heading('adress',text='Adress')
        self.hospital_table.heading('date',text='Daily date')
        

        self.hospital_table['show']='headings'
        self.hospital_table.pack(fill=BOTH,expand=1)

    def prescription_data(self):
        if self.Nameoftablets.get()=='' or self.ref.get()=='':
            messagebox.showerror('error','all fields are requierd')
        else:
            messagebox.showinfo("DB STVARI!")                                                                                                
            conn=_mysql_connector.connect(host='localhost',username='database',password='',database='Mydata')
            my_cursor=conn.cursor()
            my_cursor.execute('Insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)')(
                                                                                                 self.Nameoftablets.get(), 
                                                                                                 self.ref.get(),
                                                                                                 self.DailyDose.get(),
                                                                                                 self.DOB.get(),
                                                                                                 self.Dose.get(),
                                                                                                 self.ExpDate.get(),
                                                                                                 self.Furtherinformation.get(),
                                                                                                 self.Howtousemedication.get(),
                                                                                                 self.Issuedata.get(), 
                                                                                                 self.Lot.get(),
                                                                                                 self.Nhsnumber.get(),
                                                                                                 self.PatientAdress.get(),
                                                                                                 self.Patientname.get()
                                                                                                )

            conn.comit()
            conn.close()
root=Tk()
ob=Hospital(root)
root.mainloop()
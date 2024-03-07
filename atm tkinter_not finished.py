from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class atm:

    password=2213
   

  
        
    def __init__(self,root):
     
    
        self.root=root
        root.title('ATM SYSTEM')
        root.geometry('774x760+200+0')
        root.configure(bg='#fff')
        root.resizable(False,False)
        #######################FRAME############################################
        def input_pin():
            pinNo = self.txtreceipt.get("1.0","end-1c")
            if {(pinNo!=int('2213'))}:
              self.txtreceipt.delete('1.0',END)
              self.txtreceipt.insert(END,'\t\t\t  ATM  ' + '\n\n')
              self.txtreceipt.insert(END,'Withdraw cash\t\t\t Loan ' + '\n\n')
              self.txtreceipt.insert(END,'Balance\t\t\tRequest a new pin ' + '\n\n')
              self.txtreceipt.insert(END,'Mini statement\t\t\t Print statement' + '\n\n')
            
        def clear():
             self.txtreceipt.delete('1.0',END)
            
        def cancel():
            cancel=messagebox.askyesno('ATM','Confirm if you want to cancel')
            if cancel>0:
                 self.root.destroy()
                 return
             
        def withdrawcash():
             input_pin()
             self.txtreceipt.delete('1.0',END)
             self.txtreceipt.focus_set()
        def loan():
             input_pin()  
             self.txtreceipt.delete('1.0',END)
             self.txtreceipt.insert(END,'Loan RSD')
             self.txtreceipt.focus_set()    
        def deposit():
             input_pin()  
             self.txtreceipt.delete('1.0',END)
             self.txtreceipt.focus_set()    
        def requestnewpin():
             input_pin()
             self.txtreceipt.delete('1.0',END)
             self.txtreceipt.insert(END,'\t\t\t  New pin will be avaible in 24 h  ' + '\n\n') 
             self.txtreceipt.insert(END,'\t\t\t Thank you for patient...  ' + '\n\n')
             self.txtreceipt.insert(END,'Withdraw cash\t\t\t Loan ' + '\n\n')
             self.txtreceipt.insert(END,'Balance\t\t\tRequest a new pin ' + '\n\n')
             self.txtreceipt.insert(END,'Mini statement\t\t\t Print statement' + '\n\n') 
                        
        Main=Frame(root,bd=20,width=784,height=700,relief=RIDGE)
        Main.grid()
        Top1=Frame(Main,bd=7,width=734,height=300,relief=RIDGE)
        Top1.grid(row=1,column=0,padx=12)
        Top2=Frame(Main,bd=7,width=734,height=300,relief=RIDGE)
        Top2.grid(row=0,column=0,padx=8)
        Top2left=Frame(Top2,bd=5,width=190,height=300,relief=RIDGE)
        Top2left.grid(row=0,column=0,padx=8)
        Top2mid=Frame(Top2,bd=5,width=200,height=300,relief=RIDGE)
        Top2mid.grid(row=0,column=1,padx=8)
        Top2right=Frame(Top2,bd=5,width=190,height=300,relief=RIDGE)
        Top2right.grid(row=0,column=2,padx=8)

      
#########################################################################################
        ##############################WIDGET####################################
        self.txtreceipt=Text(Top2mid,height=17,width=42,bd=12,font='arial 9 bold')
        self.txtreceipt.grid(row=0,column=0)
        button1=Button(Top2left,text='>>>>>',font='arial 35 bold',command=withdrawcash)
        button1.place(x=0,y=0)
        button2=Button(Top2left,text='>>>>>',font='arial 35 bold',command=deposit)
        button2.place(x=0,y=100)
        button3=Button(Top2left,text='>>>>>',font='arial 35 bold')
        button3.place(x=0,y=200)
        button4=Button(Top2right,text='<<<<<',font='arial 35 bold',command=loan)
        button4.place(x=0,y=0)
        button5=Button(Top2right,text='<<<<<',font='arial 35 bold',command=requestnewpin)
        button5.place(x=0,y=100)
        button6=Button(Top2right,text='<<<<<',font='arial 35 bold')
        button6.place(x=0,y=200)
       #########################################################################
            ##########################PIN NUMBERS BUTTONS#########################
        

        
        def insert_value1():
            value1=1
            self.txtreceipt.insert(END,value1)
        pin1=Button(root,text='1',font='arial  20 bold',relief=SOLID,command=insert_value1)
        pin1.place(x=200,y=350)
        def insert_value2():
            value2=2
            self.txtreceipt.insert(END,value2)
        pin2=Button(root,text='2',font='arial  20 bold',relief=SOLID,command=insert_value2)
        pin2.place(x=275,y=350)
        def insert_value3():
            value3=3
            self.txtreceipt.insert(END,value3)
        pin3=Button(root,text='3',font='arial  20 bold',relief=SOLID,command=insert_value3)
        pin3.place(x=350,y=350)
        def insert_value4():
            value4=4
            self.txtreceipt.insert(END,value4)
        pin4=Button(root,text='4',font='arial 20 bold',relief=SOLID,command=insert_value4)
        pin4.place(x=200,y=425)
        def insert_value5():
            value5=5
            self.txtreceipt.insert(END,value5)
        pin5=Button(root,text='5',font='arial  20 bold',relief=SOLID,command=insert_value5)
        pin5.place(x=275,y=425)
        def insert_value6():
            value6=6
            self.txtreceipt.insert(END,value6)
        pin6=Button(root,text='6',font='arial  20 bold',relief=SOLID,command=insert_value6)
        pin6.place(x=350,y=425)
        def insert_value7():
            value7=7
            self.txtreceipt.insert(END,value7)
        pin7=Button(root,text='7',font='arial 20 bold',relief=SOLID,command=insert_value7)
        pin7.place(x=200,y=500)
        def insert_value8():
            value8=8
            self.txtreceipt.insert(END,value8)
        pin8=Button(root,text='8',font='arial  20 bold',relief=SOLID,command=insert_value8)
        pin8.place(x=275,y=500)
        def insert_value9():
            value9=9
            self.txtreceipt.insert(END,value9)
        pin9=Button(root,text='9',font='arial  20 bold',relief=SOLID,command= insert_value9)
        pin9.place(x=350,y=500)
        def insert_value():
                value0=0
                self.txtreceipt.insert(END,value0)
        pin0=Button(root,text='0',font='arial  20 bold',relief=SOLID,command=insert_value)
        pin0.place(x=275,y=570)
        ########################################################################
        #######################ENTER CANCEL AND CLEAR BUTTONS
        
        Cancel=Button(root,text='CANCEL',font='arial 20 bold',relief=SOLID,bg='yellow',command=cancel)
        Cancel.place(x=450,y=425)
        Clear=Button(root,text='CLEAR',font='arial  20 bold',relief=SOLID,bg='green',command=clear)
        Clear.place(x=450,y=500)

    
        
        Enter=Button(root,text='ENTER',font='arial  20 bold',relief=SOLID,bg='red',command=input_pin)
        Enter.place(x=450,y=350)


        #########################################################Function################################
    
                
        



        ##################################################################################################
    
    

if __name__=='__main__':
            root=Tk()
            app=atm(root)
            root.mainloop()
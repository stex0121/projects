from tkinter import *
from tkinter import messagebox

class LoanCalculator:

    def __init__(self):
        self.window=Tk()
        self.window.title("Loan_Calculator")

        Label(self.window,text="Annual Interest  Rate").grid(row=1,column=1,sticky=W)
        Label(self.window,text="Number of Years").grid(row=2,column=1,sticky=W) 
        Label(self.window,text="Loan Amount").grid(row=3,column=1,sticky=W) 
        Label(self.window,text="Monthly Payment").grid(row=4,column=1,sticky=W) 
        Label(self.window,text="Total Payment").grid(row=5,column=1,sticky=W)  

        self.annualinterestrateVar=StringVar()
        Entry(self.window,textvariable=self.annualinterestrateVar,justify=RIGHT).grid(row=1,column=2)
        self.numberofyearsVar=StringVar()
        Entry(self.window,textvariable=self.numberofyearsVar,justify=RIGHT).grid(row=2,column=2)
        self.loanamountVar=StringVar()
        Entry(self.window,textvariable=self.loanamountVar,justify=RIGHT).grid(row=3,column=2)
        self.montlypaymentVar=StringVar()
        Entry(self.window,textvariable=self.montlypaymentVar,justify=RIGHT).grid(row=4,column=2,sticky=E)
        self.totalpaymentVar=StringVar()
        Entry(self.window,textvariable=self.totalpaymentVar,justify=RIGHT).grid(row=5,column=2,sticky=E)

        Button(self.window,text="Calculate Payment",command=self.calculatepayment).grid(row=6,column=2,sticky=E)
        Button(self.window,text="Clear",command=self.clearfields).grid(row=6,column=1,sticky=W)
        
        self.window.mainloop()

    def calculatepayment(self):
        try:
            loanamount=float(self.loanamountVar.get())
            annualinterestrate=float(self.annualinterestrateVar.get())
            monthlyinterestrate=annualinterestrate/1200
            numberofyears=int(self.numberofyearsVar.get())

            montlypayment=self.getmontlypayment(loanamount,monthlyinterestrate,numberofyears)
            self.montlypaymentVar.set(f"${montlypayment:,.2f}")

            totalpayment=montlypayment*12*numberofyears
            self.totalpaymentVar.set(f"${totalpayment:,.2f}")
        except ValueError:
            messagebox.showerror("Error","Invalid input. Please enter valid numbers")
    
    def getmontlypayment(self,loanamount,montlyinterestrate,numberofyears):
        return loanamount*montlyinterestrate/(1-1/(1+montlyinterestrate)**(numberofyears*12))
    
    def clearfields(self):
        self.annualinterestrateVar.set("")
        self.numberofyearsVar.set("")
        self.loanamountVar.set("")
        self.montlypaymentVar.set("")


LoanCalculator()
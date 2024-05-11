from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class atm:
    password = 2213
    balance=20000
    button1_clicked = False
    button2_clicked = True
    button4_clicked = False

    def __init__(self, root):
        self.root = root
        root.title('ATM SYSTEM')
        root.geometry('774x760+200+0')
        root.configure(bg='#fff')
        root.resizable(False, False)
        global pinNo
        #######################FRAME############################################
        def input_pin():
               
            pinNo = self.txtreceipt.get("1.0", "end-1c")
            if int(pinNo) == self.password:
                self.txtreceipt.delete('1.0', END)
                self.txtreceipt.insert(END, '\t\t\t  ATM  ' + '\n\n')
                self.txtreceipt.insert(END, 'Withdraw cash\t\t\t Loan ' + '\n\n')
                self.txtreceipt.insert(END, '\t\t\tRequest a new pin ' + '\n\n')
                self.txtreceipt.insert(END, 'Mini statement\t\t\t Print statement' + '\n\n')
            
            if self.button1_clicked:
                amount = int(pinNo) 
                remaining_balance = self.balance - amount
                self.txtreceipt.insert(END, f"Amount: {amount}\n")
                self.txtreceipt.insert(END, f"Remaining balance RSD: {remaining_balance}\n")
            elif self.button4_clicked:
                loan = int(pinNo)
                new_balance = loan + self.balance
                self.txtreceipt.insert(END, f"New balance: {new_balance}\n")
            else:
                # Handle other cases or provide a default action
                pass

                                    
                                


        
        
        
            
            
        
        def clear():
            self.txtreceipt.delete('1.0', END)
            
        def cancel():
            cancel = messagebox.askyesno('ATM', 'Confirm if you want to cancel')
            if cancel > 0:
                self.root.destroy()

        def withdrawcash():
            self.button1_clicked = True
            self.button2_clicked = False
            self.button4_clicked = False
            self.txtreceipt.delete('1.0', END)
            self.txtreceipt.focus_set()

        def deposit():
            self.button1_clicked = False
            self.button2_clicked = True
            self.button4_clicked = False
            self.txtreceipt.delete('1.0', END)
            self.txtreceipt.focus_set()

        def loan():
            self.button1_clicked = False
            self.button2_clicked = False
            self.button4_clicked = True
            self.txtreceipt.delete('1.0', END)
            self.txtreceipt.focus_set()

        def mini_statement():
        
                    recent_transactions = [
                    {"type": "Withdrawal", "amount": 1000},
                    {"type": "Deposit", "amount": 20000},
                    {"type": "Withdrawal", "amount": 11200}
                    ]

                        # Clear the text widget
                    self.txtreceipt.delete('1.0', END)

                        # Display the heading for the mini statement
                    self.txtreceipt.insert(END, "Mini Statement\n\n")

                        # Display each transaction in the mini statement
                    for transaction in recent_transactions:
                            transaction_type = transaction["type"]
                            transaction_amount = transaction["amount"]
                            self.txtreceipt.insert(END, f"{transaction_type}: {transaction_amount}\n")

                        # Optionally, you can also display the current balance at the end of the mini statement
                        # For demonstration purposes, let's assume self.balance holds the current balance
                    self.txtreceipt.insert(END, f"\nCurrent Balance: {self.balance}\n")
        

        def requestnewpin():
            self.txtreceipt.delete('1.0', END)
            self.txtreceipt.insert(END, '\t\t\t  New pin will be available in 24 h  ' + '\n\n')
            self.txtreceipt.insert(END, '\t\t\t Thank you for your patience...  ' + '\n\n')
            self.txtreceipt.insert(END, 'Withdraw cash\t\t\t Loan ' + '\n\n')
            self.txtreceipt.insert(END, '\t\t\tRequest a new pin ' + '\n\n')
            self.txtreceipt.insert(END, 'Mini statement\t\t\t Print statement' + '\n\n')

        Main = Frame(root, bd=20, width=784, height=700, relief=RIDGE)
        Main.grid()
        Top1 = Frame(Main, bd=7, width=734, height=300, relief=RIDGE)
        Top1.grid(row=1, column=0, padx=12)
        Top2 = Frame(Main, bd=7, width=734, height=300, relief=RIDGE)
        Top2.grid(row=0, column=0, padx=8)
        Top2left = Frame(Top2, bd=5, width=190, height=300, relief=RIDGE)
        Top2left.grid(row=0, column=0, padx=8)
        Top2mid = Frame(Top2, bd=5, width=200, height=300, relief=RIDGE)
        Top2mid.grid(row=0, column=1, padx=8)
        Top2right = Frame(Top2, bd=5, width=190, height=300, relief=RIDGE)
        Top2right.grid(row=0, column=2, padx=8)
        
        ##############################WIDGET####################################
        
        self.txtreceipt = Text(Top2mid, height=17, width=42, bd=12, font='arial 9 bold')
        self.txtreceipt.grid(row=0, column=0)
        
        button1 = Button(Top2left, text='>>>>>', font='arial 35 bold', command=withdrawcash)
        button1.place(x=0, y=0)
        button2 = Button(Top2left, text='>>>>>', font='arial 35 bold', command=deposit)
        button2.place(x=0, y=100)
        button3 = Button(Top2left, text='>>>>>', font='arial 35 bold',command=mini_statement)
        button3.place(x=0, y=200)
        button4 = Button(Top2right, text='<<<<<', font='arial 35 bold', command=loan)
        button4.place(x=0, y=0)
        button5 = Button(Top2right, text='<<<<<', font='arial 35 bold', command=requestnewpin)
        button5.place(x=0, y=100)
        button6 = Button(Top2right, text='<<<<<', font='arial 35 bold')
        button6.place(x=0, y=200)
        
        #######################PIN NUMBERS BUTTONS#########################
        
        def insert_value(value):
            self.txtreceipt.insert(END, value)
        
        def create_pin_button(value, x, y):
            btn = Button(root, text=value, font='arial 20 bold', relief=SOLID, command=lambda: insert_value(value))
            btn.place(x=x, y=y)
        
        create_pin_button('1', 200, 350)
        create_pin_button('2', 275, 350)
        create_pin_button('3', 350, 350)
        create_pin_button('4', 200, 425)
        create_pin_button('5', 275, 425)
        create_pin_button('6', 350, 425)
        create_pin_button('7', 200, 500)
        create_pin_button('8', 275, 500)
        create_pin_button('9', 350, 500)
        create_pin_button('0', 275, 570)
        
        #######################ENTER CANCEL AND CLEAR BUTTONS
        
        Cancel = Button(root, text='CANCEL', font='arial 20 bold', relief=SOLID, bg='yellow', command=cancel)
        Cancel.place(x=450, y=425)
        
        Clear = Button(root, text='CLEAR', font='arial 20 bold', relief=SOLID, bg='green', command=clear)
        Clear.place(x=450, y=500)
        
        Enter = Button(root, text='ENTER', font='arial 20 bold', relief=SOLID, bg='red', command=input_pin)
        Enter.place(x=450, y=350)

if __name__ == '__main__':
    root = Tk()
    app = atm(root)
    root.mainloop()

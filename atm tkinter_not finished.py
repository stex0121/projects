from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog

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
        transactions = []
        
        #######################FRAME############################################
        def input_pin():
            pinNo = self.txtreceipt.get("1.0", "end-1c")
            if int(pinNo) == self.password:
                self.txtreceipt.delete('1.0', END)
                self.txtreceipt.insert(END, '\t\t  E-banking Bankomat  ' + '\n\n')
                self.txtreceipt.insert(END, 'Podizanje novca(UNOS)\t Uplata novca(UNOS) ' + '\n\n')
                self.txtreceipt.insert(END, ' Izvestaj o racunu/Balans\t\t\t  ' + 'Zahtev za novi pin \n\n')
                
                
            if self.button1_clicked:  # Assuming self.button1_clicked indicates a withdrawal
                amount = int(pinNo)
                if amount <= self.balance:  # Check if the withdrawal amount is less than or equal to the current balance
                    remaining_balance = self.balance - amount
                    self.balance = remaining_balance  # Update the balance
                    self.txtreceipt.delete('1.0', END)
                    self.txtreceipt.insert(END, f"Trenutni Balanas stanja na racunu  RSD: {remaining_balance}\n")
                    self.txtreceipt.insert(END, 'Hvala vam sto koristite nase usluge.  ' + '\n\n')
                    self.txtreceipt.insert(END, 'Podizanje novca\t\t\t Uplata novca ' + '\n\n')
                    self.txtreceipt.insert(END, ' Izvestaj o racunu/Balans\t\t\t  ' + 'Zahtev za novi pin \n\n')
                else:
                    self.txtreceipt.delete('1.0', END)
                    self.txtreceipt.insert(END, "Nemate dovoljno sredstava na racunu za ovu transakciju.\n")
                
                        
            elif self.button4_clicked:  # Assuming self.button4_clicked indicates a deposit
                deposit_amount = int(pinNo)
                new_balance = self.balance + deposit_amount
                self.balance = new_balance  # Update the balance
                self.txtreceipt.delete('1.0', END)
                self.txtreceipt.insert(END, f"Novo stanje na racunu: {new_balance}\n")
                self.txtreceipt.insert(END, 'Podizanje novca\t\t\t Uplata novca ' + '\n\n')
                self.txtreceipt.insert(END, ' Izvestaj o racunu/Balans\t\t\t  ' + 'Zahtev za novi pin \n\n')
    
            else:
                if int(pinNo) != self.password:
                    self.txtreceipt.insert(END, '\t\t Pogresan pin,pokusajte opet...Hvala ' + '\n\n')

        def clear():
            self.txtreceipt.delete('1.0', END)
            
        def cancel():
            cancel = messagebox.askyesno('ATM', 'Da li zelite da izadjete')
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
        # Clear the text widget
            self.transactions = []
            self.txtreceipt.delete('1.0', END)

            # Display the heading for the mini statement
            self.txtreceipt.insert(END, "Mali izvestaj o racunu\n\n")

            # Display each transaction in the mini statement
            for transaction in self.transactions:
                transaction_type = transaction["type"]
                transaction_amount = transaction["amount"]
                self.txtreceipt.insert(END, f"{transaction_type}: {transaction_amount}\n")
          
        def change_pin():
        # Get the new PIN from the user
            new_pin = simpledialog.askstring("New PIN", "Enter your new PIN:")
        
            # If the user cancels or enters an empty PIN, return without changing the PIN
            if new_pin is None or new_pin == "":
                return

            # Get the confirmation PIN from the user
            confirm_pin = simpledialog.askstring("Confirm PIN", "Confirm your new PIN:")
            
            # If the user cancels or enters an empty PIN, return without changing the PIN
            if confirm_pin is None or confirm_pin == "":
                return

            # Check if the new PIN and confirmation PIN match
            if new_pin == confirm_pin:
                # Update the PIN
                atm.password = new_pin
                print("PIN changed successfully!")
            else:
                messagebox.showerror("Error", "PINs do not match. Please try again.")

                def check_confirmation(new_pin, confirm_pin, dialog):
                    if new_pin == confirm_pin:
                        self.password = new_pin
                        print("PIN changed successfully!")
                        dialog.destroy()  # Close the confirmation dialog
                    else:
                        messagebox.showerror("Error", "PINs do not match. Please try again.")
        def mini_statement():
            self.transactions=[]
            # Clear the text widget
            self.txtreceipt.delete('1.0', END)
            
            # Display the heading for the mini statement
            self.txtreceipt.insert(END, "Mini Statement\n\n")
        
            # Display each transaction in the mini statement
            for transaction in self.transactions:
                transaction_type = transaction["type"]
                transaction_amount = transaction["amount"]
                self.txtreceipt.insert(END, f"{transaction_type}: {transaction_amount}\n")

            # Display the current balance
            self.txtreceipt.insert(END, f"\Trenutni Balans: {self.balance}")
          

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
        button2 = Button(Top2left, text='>>>>>', font='arial 35 bold', command=mini_statement)
        button2.place(x=0, y=100)
        button3 = Button(Top2left, text='>>>>>', font='arial 35 bold')
        button3.place(x=0, y=200)
        button4 = Button(Top2right, text='<<<<<', font='arial 35 bold', command=loan)
        button4.place(x=0, y=0)
        button5 = Button(Top2right, text='<<<<<', font='arial 35 bold', command=change_pin)
        button5.place(x=0, y=100)
        button6 = Button(Top2right, text='<<<<<', font='arial 35 bold')
        button6.place(x=0, y=200)
        
        #######################PIN NUMBERS BUTTONS#########################
        
        def insert_value(value):
            self.txtreceipt.insert(END, value)
        
        def create_pin_button(value, x, y):
            btn = Button(root, text=value, font='arial 20 bold', relief=SOLID, command=lambda: insert_value(value))
            btn.place(x=x, y=y)
        
        create_pin_button('1', 250, 350)
        create_pin_button('2', 325, 350)
        create_pin_button('3', 400, 350)
        create_pin_button('4', 250, 425)
        create_pin_button('5', 325, 425)
        create_pin_button('6', 400, 425)
        create_pin_button('7', 250, 500)
        create_pin_button('8', 325, 500)
        create_pin_button('9', 400, 500)
        create_pin_button('0', 325, 570)
        
        #######################ENTER CANCEL AND CLEAR BUTTONS
        
        Cancel = Button(root, text='CANCEL', font='arial 20 bold', relief=SOLID, bg='yellow', command=cancel)
        Cancel.place(x=450, y=425)
        
        Clear = Button(root, text='CLEAR', font='arial 20 bold', relief=SOLID, bg='green', command=clear)
        Clear.place(x=450, y=500)
        
        Enter = Button(root, text='ENTER', font='arial 20 bold', relief=SOLID, bg='red', command=input_pin)
        Enter.place(x=450, y=350)
    def authenticate(self, entered_pin):
        return entered_pin == self.password
if __name__ == '__main__':
    root = Tk()
    app = atm(root)
    root.mainloop()

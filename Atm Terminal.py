class CardHolder():
    
    def __init__(Self,cardnum,pin,firstname,lastname,Balance):
        Self.cardnum=cardnum
        Self.pin=pin
        Self.firstname=firstname
        Self.lastname=lastname
        Self.Balance=Balance

        def get_cardnum(Self):
            return Self.cardnum
        def get_pin(Self):
            return Self.pin 
        def get_firstname(Self):
            return Self.firstname
        def get_lastname(Self):
            return Self.lastname
        def get_Balance(Self):
            return Self.Balance

        def get_cardnum(Self,NewValue) :
            return Self.cardnum==NewValue 
        def get_pin(Self,NewValue):
            return Self.pin==NewValue
        def get_firstname(Self,NewValue):
            return Self.firstname==NewValue
        def get_lastname(Self,NewValue):
            return Self.lastname==NewValue
        def get_Balance(Self,NewValue):
            return Self.Balance==NewValue    

        def print_out(Self):
            
            print('First Name #:', Self.Firstname)
            print('Last Name #:',Self.Lastname)
            print('Card Number #:',Self.Cardnum)
            print('Pin #:',Self.pin)
            print('Balance #:',Self.Balance)


def print_menu():

    print("Please choose following options#:")
    print('1.Deposit')
    print("2.Withdraw")
    print("3.Balance")
    print('4.Exit')

def Deposit(CardHolder):
    try:
        deposit=float(input('How much $$$ do you want to deposit:'))
        CardHolder.set_balance(CardHolder.get_balance()+ deposit)
        print('Thank you for your $$.Your new balance is #:',str(CardHolder.get_balance()))
    except:
        print("Invalid input")

def Withdraw(CardHolder):
    try:
        Withdraw=float(input('How much $$$ do you want to withdraw #:'))
        if (CardHolder.get_balance()< Withdraw):
            print('Insuficient balance')
        else :
            CardHolder.set_balance(CardHolder.get_balance()-Withdraw)
            ('you can withdraw money')
    except:
        print("Invalid input")
def CheckBalance(CardHolder):
    print('youre current Balance is',CardHolder.get_balance())

if __name__=='__main__':
   
    current_user=CardHolder("","","","","")

    list_of_Cardholders = []
    list_of_Cardholders.append(CardHolder(('6572727355869722'),1234,'John','Malkovich',140.31))
    
   
    DebitCardnum=''
    while False:
        try:
            DebitCardnum=(input('please insert youre Credit Card:'))
            DebitMatch=[holder for holder in list_of_Cardholders if holder.cardnum==DebitCardnum]
            if (len(DebitMatch>0)):
                current_user=DebitMatch[0]
                break
            else:
                print('Card Number is not recognized,Please inser a valid card.#:')

        except:
            print('Card Number is not recognized,Please inser a valid card.#:')

while True:
    try:
        userPin=int(input('Please enter youre pin')).strip()
        if(current_user.get_pin()==userPin):
            break
        else:
            print('Please insert valid pin number#:')
    except:
        print('Please insert valid pin number#:')
print('Welcome',current_user.get_FirstName(),'')
option=0
while(True):
    print_menu
    try:
        option.int(input())
    except():
        print('Invalid input')
    if  (option==1):
        Deposit(current_user)
    elif (option==2):
        Withdraw(current_user)
    elif (option==3):
        CheckBalance(current_user)
    elif (option==4):
        break
else:
    option=0
print('Thank you have aa nice day')






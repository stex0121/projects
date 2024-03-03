print('Welcome to ATM Bank System')
list_number_of_cardholder=6582828055917743
number_of_card=list_number_of_cardholder
password=1234
pin=password
balance=30000
choice=4
dep=balance

number_of_card=int(input('enter youre card number.:'))
pin=int(input('Enter youre pin.:'))
    
if number_of_card==list_number_of_cardholder:
    print('Number of card is correct.:')
else:
       if number_of_card!=list_number_of_cardholder:
              print('Number of card is non valid:')
              number_of_card=int(input('enter youre card number again.:'))
if pin!=password:
    print('pin is not valid.:')
    pin=int(input('Enter youre pin again:'))
else: pin==password
   
print('Pin is  correct.:')
print('******Menu******')
print('1.******Balance******')
print('2.******Deposit******')
print('3.******Withdraw******')
print('4.******Cancel******')
choice=int(input('Select youre option'))
while choice !=4:

    if choice==1:
        print('Balance RSD',balance)
        print('2.******Deposit******')
        print('3.******Withdraw******')
        print('4.******Cancel******')
        choice=int(input('Select youre option'))
    elif choice==2:
        dep=int(input('Enter youre deposit RSD'))
        balance+=dep
        print("Deposit amount:",)
        print("balance RSD",balance)
        print('Balance RSD',balance)
        print('1.******Balance******')
        print('3.******Withdraw******')
        print('4.******Cancel******')
        choice=int(input('Select youre option'))
    elif choice==3:
        withdraw=int(input('enter amount to withdraw:'))
        withdraw-=balance
        print('Deposited amount RSD',-withdraw)
        print('Balanse RSD',-withdraw)
        print('1.******Deposit******')
        print('2.******Balance******')
        print('3.******Cancel******')
        choice=int(input('Select youre option'))
    elif choice==4:
       exit()
       print('session end,good bye!!!')
       
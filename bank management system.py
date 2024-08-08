import random
import mysql.connector as sql
import datetime

# Database connection setup
try:
    mydb = sql.connect(
        host="",
        user="",
        password="",
        database=""
    )
    print("Connected to MySQL database!")
except sql.Error as e:
    print(f"Error connecting to MySQL database: {e}")

cursor = mydb.cursor()

def db_query(query_str):
    cursor.execute(query_str)
    result = cursor.fetchall()
    return result

def createcustomertable():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            username VARCHAR(20) NOT NULL,
            password VARCHAR(20) NOT NULL,
            name VARCHAR(20) NOT NULL,
            age INTEGER NOT NULL,
            city VARCHAR(20) NOT NULL,
            balance INTEGER NOT NULL DEFAULT,  # Default balance set to 0
            account_number INTEGER NOT NULL,
            status BOOLEAN NOT NULL DEFAULT FALSE,
            PRIMARY KEY (username)
        )
    ''')
    mydb.commit()

def update_existing_users():
    cursor.execute("UPDATE customers SET balance = 0 WHERE balance IS NULL;")
    mydb.commit()

class Bank:
    def __init__(self, username, account_number):
        self.username = username
        self.account_number = account_number
        self.create_transaction_table()

    def create_transaction_table(self):
        db_query(f"CREATE TABLE IF NOT EXISTS {self.username}_transaction ("
                 "timedate VARCHAR(30),"
                 "account_number INTEGER,"
                 "remarks VARCHAR(30),"
                 "amount INTEGER)")
        mydb.commit()

    def balanceinquiry(self):
        temp = db_query(f"SELECT balance FROM customers WHERE username='{self.username}'")
        print(f"Query result: {temp}")  # Debugging line
        
        if temp:
            print(f"{self.username}'s Balance is {temp[0][0]}")
        else:
            print(f"No balance information found for user: {self.username}")

    def deposit(self, amount):
        temp = db_query(f"SELECT balance FROM customers WHERE username='{self.username}'")
        if temp:
            new_balance = amount + temp[0][0]
            db_query(f"UPDATE customers SET balance = '{new_balance}' WHERE username = '{self.username}'")
            self.balanceinquiry()
            db_query(f"INSERT INTO {self.username}_transaction VALUES ("
                     f"'{datetime.datetime.now()}',"
                     f"'{self.account_number}',"
                     f"'Amount Deposited',"
                     f"'{amount}')")
            mydb.commit()
            print(f"{self.username}, Amount Successfully Deposited into Your Account.")
        else:
            print(f"No balance information found for user: {self.username}")

    def withdraw(self, amount):
        temp = db_query(f"SELECT balance FROM customers WHERE username='{self.username}'")
        if temp:
            if amount > temp[0][0]:
                print("Not Enough Balance! Please Deposit More Money.")
            else:
                new_balance = temp[0][0] - amount
                db_query(f"UPDATE customers SET balance = '{new_balance}' WHERE username = '{self.username}'")
                self.balanceinquiry()
                db_query(f"INSERT INTO {self.username}_transaction VALUES ("
                         f"'{datetime.datetime.now()}',"
                         f"'{self.account_number}',"
                         f"'Amount Withdrawn',"
                         f"'{amount}')")
                mydb.commit()
                print(f"{self.username}, Amount Successfully Withdrawn from Your Account.")
        else:
            print(f"No balance information found for user: {self.username}")

    def transfer(self, receive_account_number, amount):
        temp = db_query(f"SELECT balance FROM customers WHERE username='{self.username}'")
        if temp:
            if amount > temp[0][0]:
                print("Not Enough Balance! Please Deposit More Money.")
            else:
                temp2 = db_query(f"SELECT balance FROM customers WHERE account_number = '{receive_account_number}'")
                if temp2:
                    new_sender_balance = temp[0][0] - amount
                    new_receiver_balance = amount + temp2[0][0]
                    db_query(f"UPDATE customers SET balance = '{new_sender_balance}' WHERE username = '{self.username}'")
                    db_query(f"UPDATE customers SET balance = '{new_receiver_balance}' WHERE account_number = '{receive_account_number}'")
                    receiver_username = db_query(f"SELECT username FROM customers WHERE account_number='{receive_account_number}'")
                    self.balanceinquiry()
                    db_query(f"INSERT INTO {receiver_username[0][0]}_transaction VALUES ("
                             f"'{datetime.datetime.now()}',"
                             f"'{self.account_number}',"
                             f"'Transfer From {self.account_number}',"
                             f"'{amount}')")
                    db_query(f"INSERT INTO {self.username}_transaction VALUES ("
                             f"'{datetime.datetime.now()}',"
                             f"'{self.account_number}',"
                             f"'Transfer to {receive_account_number}',"
                             f"'{amount}')")
                    mydb.commit()
                    print(f"{self.username}, Amount Successfully Transferred to {receive_account_number}.")
                else:
                    print(f"Receiver account number {receive_account_number} does not exist.")
        else:
            print(f"No balance information found for user: {self.username}")


class Customer:
    def __init__(self, username, password, name, age, city, account_number):
        self.username = username
        self.password = password
        self.name = name
        self.age = age
        self.city = city
        self.account_number = account_number

    def createuser(self):
        db_query(f"INSERT INTO customers (username, password, name, age, city, balance, account_number, status) VALUES ("
                 f"'{self.username}',"
                 f"'{self.password}',"
                 f"'{self.name}',"
                 f"'{self.age}',"
                 f"'{self.city}',"
                 f"0, "
                 f"'{self.account_number}',"
                 f"FALSE)")
        mydb.commit()
        print("User successfully created.")

def SignUp():
    username = input("Create Username: ")
    temp = db_query(f"SELECT username FROM customers WHERE username='{username}';")
    
    if temp:
        print("Username is not available. Please choose a different username.")
        SignUp()  # Recursively call SignUp until a unique username is chosen.
    else:
        print("Username is available. Please proceed.")
        password = input("Enter Your Password: ")
        name = input("Enter Your Name: ")
        age = input("Enter Your Age: ")
        city = input("Enter Your City: ")
        
        while True:
            account_number = random.randint(10000000, 99999999)
            temp = db_query(f"SELECT account_number FROM customers WHERE account_number='{account_number}';")
            if temp:
                continue  # If account number exists, generate a new one.
            else:
                print("Your Account number:", account_number)
                break
        
        cobj = Customer(username, password, name, age, city, account_number)
        cobj.createuser()  # Insert user data into the database.
        
        bobj = Bank(username, account_number)
        bobj.create_transaction_table()  # Create transaction table for the user.

def SignIn():
    global user
    username = input("Enter Your Username: ")
    temp = db_query(f"SELECT username FROM customers WHERE username='{username}';")
    
    if temp:
        while True:
            password = input("Enter Your Password: ")
            temp = db_query(f"SELECT password FROM customers WHERE username='{username}';")
            
            if temp and temp[0][0] == password:
                print('Signed In Successfully')
                user = username
                return username  # Return the username if sign-in is successful.
            else:
                print("Wrong password. Please try again!")
    else:
        print("Username does not exist. Please enter a valid username.")

def main():
    global user
    status = False
    print("Welcome To Banking System Project")

    while True:
        try:
            register = int(input("1. Sign Up\n"
                                 "2. Sign In\n"))

            if register == 1:
                SignUp()
            elif register == 2:
                SignIn()
                if user:  # Ensure user is set before breaking out
                    status = True
                    break
            else:
                print("Please Enter a Valid Input From The Options.")
        except ValueError:
            print("Invalid Input. Please Try Again.")

    account_number = db_query(f"SELECT account_number FROM customers WHERE username='{user}'")
    if not account_number:
        print("User not found.")
        return

    account_number = account_number[0][0]
    print(f"Welcome {user.capitalize()}! Choose Your Banking Service\n")

    while status:
        try:
            facility = int(input("1. Balance\n"
                                 "2. Deposit\n"
                                 "3. Withdraw\n"
                                 "4. Transfer\n"))

            if facility >= 1 and facility <= 4:
                bank_obj = Bank(user, account_number)

                if facility == 1:
                    bank_obj.balanceinquiry()
                elif facility == 2:
                    while True:
                        try:
                            amount = int(input("Enter Amount to Deposit: "))
                            bank_obj.deposit(amount)
                            mydb.commit()
                            break
                        except ValueError:
                            print("Invalid Input. Please Enter a Valid Number.")
                elif facility == 3:
                    while True:
                        try:
                            amount = int(input("Enter Amount to Withdraw: "))
                            bank_obj.withdraw(amount)
                            mydb.commit()
                            break
                        except ValueError:
                            print("Invalid Input. Please Enter a Valid Number.")
                elif facility == 4:
                    while True:
                        try:
                            receive = input("Enter Receiver's Account Number: ")
                            amount = int(input("Enter Amount to Transfer: "))
                            bank_obj.transfer(receive, amount)
                            mydb.commit()
                            break
                        except ValueError:
                            print("Invalid Input. Please Enter a Valid Number.")
            else:
                print("Please Enter a Valid Input From The Options.")
        except ValueError:
            print("Invalid Input. Please Try Again.")

if __name__ == "__main__":
    main()
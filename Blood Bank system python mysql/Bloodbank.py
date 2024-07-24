from database import *

class BloodBank:
    @staticmethod
    def patient_details(patient_name, patient_age, patient_blood_type):
        try:
            query = f"""
                INSERT INTO patient (patient_name, patient_age, patient_blood_type)
                VALUES ("{patient_name}", {patient_age}, "{patient_blood_type}")
            """
            db_query(query)
            mydb.commit()
            print(f"Patient details added successfully for {patient_name}")
        except Exception as e:
            print(f"Error inserting donor details: {e}")

    @staticmethod
    def donor_details(donor_name, donor_age, donor_blood_type):
        try:
            query = f"""
                INSERT INTO donor (donor_name, donor_age, donor_blood_type)
                VALUES ("{donor_name}", {donor_age}, "{donor_blood_type}")
            """
            db_query(query)
            mydb.commit()
            print(f"Donor details added successfully for {donor_name}")
        except Exception as e:
            print(f"Error inserting donor details: {e}")

    @staticmethod
    def request_blood(hospital_name, patient_name, patient_age, patient_blood_type, donor_name, donor_age, donor_blood_type):
        try:
            query = f"""
                INSERT INTO request (hospital_name, patient_name, patient_age, patient_blood_type, donor_name, donor_age, donor_blood_type)
                VALUES ("{hospital_name}", "{patient_name}", {patient_age}, "{patient_blood_type}", "{donor_name}", {donor_age}, "{donor_blood_type}")
            """
            db_query(query)
            mydb.commit()
            print(f"Request for blood from {donor_name} to {patient_name} at {hospital_name} processed successfully.")
        except Exception as e:
            print(f"Error requesting blood: {e}")

class Inventory:
    @staticmethod
    def add_blood(blood_type, quantity=1):
        try:
            query = f"""
                SELECT quantity FROM inventory WHERE blood_type="{blood_type}"
            """
            result = db_query(query)
            if result and len(result) > 0:
                current_quantity = result[0][0]
                new_quantity = current_quantity + quantity
                update_query = f"""
                    UPDATE inventory SET quantity={new_quantity} WHERE blood_type="{blood_type}"
                """
            else:
                update_query = f"""
                    INSERT INTO inventory (blood_type, quantity) VALUES ("{blood_type}", {quantity})
                """
            db_query(update_query)
            mydb.commit()
        except Exception as e:
            print(f"Error adding blood: {e}")

    @staticmethod
    def deduct_blood(blood_type, quantity=1):
        try:
            query = f"""
                SELECT quantity FROM inventory WHERE blood_type="{blood_type}"
            """
            result = db_query(query)
            if result and len(result) > 0:
                current_quantity = result[0][0]
                if current_quantity < quantity:
                    print(f"Sorry, insufficient {blood_type} blood available.")
                else:
                    new_quantity = current_quantity - quantity
                    update_query = f"""
                        UPDATE inventory SET quantity={new_quantity} WHERE blood_type="{blood_type}"
                    """
                    db_query(update_query)
                    mydb.commit()
            else:
                print(f"No {blood_type} blood found in inventory.")
        except Exception as e:
            print(f"Error deducting blood: {e}")

    @staticmethod
    def show_inventory():
        try:
            query = """
                SELECT blood_type, quantity FROM inventory
            """
            result = db_query(query)
            if result:
                print("Current Inventory:")
                for row in result:
                    print(f"{row[0]}: {row[1]}")
            else:
                print("Inventory is empty.")
        except Exception as e:
            print(f"Error fetching inventory: {e}")
    
# Example usage
if __name__ == "__main__":
    print("Welcome to Anlave Blood Bank")
    options = int(input("Choose The Available Options: \n"
                        "1. Add Donor Details\n"
                        "2. Request Blood\n"
                        "3. Add Patient Details\n"
                        "4. Show Inventory\n"
                        "5. Add Blood\n"
                        "6. Deduct Blood\n"))

    if options == 1:
        donor_name = input("Enter Donor Name: ")
        donor_age = int(input("Enter Donor Age: "))
        donor_blood_type = input("Enter Donor Blood Type: ")
        BloodBank.donor_details(donor_name, donor_age, donor_blood_type)
        
    elif options == 2:
        hospital_name = input("Enter Hospital Name: ")
        patient_name = input("Enter Patient Name: ")
        patient_age = int(input("Enter Patient Age: "))
        patient_blood_type = input("Enter Patient Blood Type: ")
        donor_name = input("Enter Donor Name: ")
        donor_age = int(input("Enter Donor Age: "))
        donor_blood_type = input("Enter Donor Blood Type: ")
        
        BloodBank.request_blood(hospital_name, patient_name, patient_age, patient_blood_type, donor_name, donor_age, donor_blood_type)
        Inventory.show_inventory()
    elif options == 3:
            hospital_name = input("Enter A Hospital Name: ")
            patient_name = input("Enter A Patient Name: ")
            patient_age = int(input("Enter a Patient Age: "))
            patient_blood_type = input("""Choose Patient Blood type:
            1. A+
            2. A-
            3. B+
            4. B-
            5. O+
            6. O-
            7. AB+
            8. AB- : """)
            BloodBank.patient_details(patient_name,patient_age,patient_blood_type)
    elif options == 4:
        Inventory.show_inventory() 
    elif options == 5:
        blood_type=input("Enter Blood Type to add: ")
        quantity=int(input("Enter Quantity to add:"))
        Inventory.add_blood(blood_type,quantity)
        Inventory.show_inventory()
    elif options == 6:
        blood_type=input("Enter Blood Type to deduct: ")
        quantity=int(input("Enter Quantity to add:"))
        Inventory.deduct_blood(blood_type,quantity)
        Inventory.show_inventory() 
    else:
        print("Enter valid input from 1 to 6.")

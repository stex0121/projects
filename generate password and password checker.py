import random
import string

# Function to generate a password
def generate_password(min_length, numbers=True, special_characters=True):
    # Define character sets
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    
    characters = letters
    # Include digits if requested
    if numbers:
        characters+=digits
    # Include special characters if requested
    if special_characters:
        characters+=special
    # Initialize password and flags
    password=""
    meets_criteria=False
    has_number=False
    has_special=False
    # Loop until the password meets criteria and has minimum length
    while not meets_criteria or len(password)<min_length:
        # Choose a random character from the character set
        new_char=random.choice(characters)
        # Add the character to the password
        password+=new_char
        # Check if the character is a number or special character
        if new_char in digits:
            has_number=True
        elif new_char in special:
            has_special=True
        # Check if the password meets criteria
        meets_criteria=True
        if numbers:
            meets_criteria=has_number
        if special_characters:
            meets_criteria=meets_criteria and has_special

    return password

def check_password_strength(password):
    strength=0
    length=len(password)
    # Check if password meets criteria for strength
    if length>=8:
        strength+=1
    if any(char.isdigit() for char in password):
        strength+=1
    if any(char.isupper() for char in password):
        strength+=1
    if any(char in string.punctuation for char in password):
        strength+=1
    # Determine password strength based on length and criteria
    if length>=12 and strength>=3:
        return "Strong"
    elif length >= 8 and strength >= 2:
        return "Medium"
    else:
        return "Weak"
# Main function
if __name__ == "__main__":
    # Prompt user for password requirements
    min_length=int(input("Enter the minimum length: "))
    has_number=input("Do you want to include numbers? (y/n): ").lower() == "y"
    has_special=input("Do you want to include special characters? (y/n): ").lower() == "y"
    # Generate password based on requirements
    password=generate_password(min_length, has_number, has_special)
    print("Generated Password:",password)
    print("Password Strength:",check_password_strength(password))
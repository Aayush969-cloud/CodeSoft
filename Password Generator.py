# Task 3
import random
import string

# Function to generate a password
def generate_password(length):
    # Defining possible characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password using the specified length
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

# Main function to run the password generator
def password_generator():
    try:
        # Prompt the user to specify the password length
        length = int(input("Enter the desired password length: "))
        
        if length < 6:
            print("Password length should be at least 6 characters for better security.")
        else:
            # Generate the password
            password = generate_password(length)
            
            # Display the generated password
            print(f"Generated Password: {password}")
    
    except ValueError:
        print("Invalid input! Please enter a valid number.")

# Run the password generator
password_generator()

# Task 5
# Contact Information Manager

# Dictionary to store contacts, where name is the key and other details are values
contacts = {}

# Function to add a new contact
def add_contact():
    name = input("Enter contact name: ").strip().title()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()
    address = input("Enter home address: ").strip()
    
    if name in contacts:
        print("Contact already exists.")
    else:
        contacts[name] = {'Phone': phone, 'Email': email, 'Address': address}
        print(f"Contact '{name}' added successfully!")

# Function to display all contacts
def view_contacts():
    if len(contacts) == 0:
        print("No contacts available.")
    else:
        print("\nContact List:")
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['Phone']}")

# Function to search for a contact by name or phone number
def search_contact():
    search = input("Enter name or phone number to search: ").strip().title()
    found = False
    
    for name, info in contacts.items():
        if search in name or search in info['Phone']:
            print(f"\nFound Contact: Name: {name}, Phone: {info['Phone']}, Email: {info['Email']}, Address: {info['Address']}")
            found = True
            break
    
    if not found:
        print("No contact found.")

# Function to update a contact
def update_contact():
    name = input("Enter the name of the contact to update: ").strip().title()
    
    if name in contacts:
        print(f"\nCurrent details for {name}:")
        print(f"Phone: {contacts[name]['Phone']}")
        print(f"Email: {contacts[name]['Email']}")
        print(f"Address: {contacts[name]['Address']}")
        
        phone = input("Enter new phone number (leave blank to keep current): ").strip()
        email = input("Enter new email (leave blank to keep current): ").strip()
        address = input("Enter new address (leave blank to keep current): ").strip()
        
        # Update only fields that are not left blank
        if phone:
            contacts[name]['Phone'] = phone
        if email:
            contacts[name]['Email'] = email
        if address:
            contacts[name]['Address'] = address
        
        print(f"Contact '{name}' updated successfully!")
    else:
        print("Contact not found.")

# Function to delete a contact
def delete_contact():
    name = input("Enter the name of the contact to delete: ").strip().title()
    
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully!")
    else:
        print("Contact not found.")

# Main function to run the contact manager
def contact_manager():
    while True:
        print("\nOptions:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the Contact Manager application
contact_manager()

contacts = {}

def add_contact(name, number):
    contacts[name] = number
    print(f"contacts {name} added successfully ")

def view_contacts():
    if contacts:
        print("\n--- contact list ---")
        for name, number in contacts.items():
          print(f"{name}: {number} ")
    else:
        print("No contact found.")

def delete_contact(name):
    if name in contacts:
        del contacts [name]
        print(f"Contact {name} deleted successfully. ") 
    else:
        print("contact not found.")

while True:
    print ("\n---- Contact Book ----")
    print("1. Add contact")
    print("2. View contats")
    print("3. Delete contact")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter name: ")
        number = input("Enter number: ")
        add_contact(name , number)
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        name = input("Enter name to delete :")
        delete_contact(name)
    elif choice == '4':
        print("Exiting contact book... Godbye!")

        break 
    else:
        print("Invalid choice . please try again !")

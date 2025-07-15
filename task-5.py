def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    address = input("Enter address: ").strip()
    contacts[name] = {'Phone': phone, 'Email': email, 'Address': address}
    print(f"Contact for {name} added successfully.")

def view_contacts():
    if not contacts:
        print("No contacts available.")
    else:
        for name, details in contacts.items():
            print(f"\nName: {name}")
            for key, value in details.items():
                print(f"{key}: {value}")

def search_contact():
    name = input("Enter name to search: ").strip()
    if name in contacts:
        print(f"\nContact found for {name}:")
        for key, value in contacts[name].items():
            print(f"{key}: {value}")
    else:
        print("Contact not found.")

def update_contact():
    name = input("Enter the name to update: ").strip()
    if name in contacts:
        print("Enter new details (leave blank to keep old value):")
        phone = input(f"New phone ({contacts[name]['Phone']}): ").strip()
        email = input(f"New email ({contacts[name]['Email']}): ").strip()
        address = input(f"New address ({contacts[name]['Address']}): ").strip()

        if phone:
            contacts[name]['Phone'] = phone
        if email:
            contacts[name]['Email'] = email
        if address:
            contacts[name]['Address'] = address
        print(f"Contact for {name} updated.")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter the name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact for {name} deleted.")
    else:
        print("Contact not found.")

def main():
    while True:
        print("\n--- Contact Book ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()

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
            print("Exiting Contact Book.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
    